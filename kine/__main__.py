import click
import pathlib
import sys
import toml
import shutil
import tarfile
import os.path
import kine
import typing_extensions
import types
import importlib
import os
import pipdeptree
import importlib.metadata as import_meta
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse


class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        urlparts = urlparse(self.path)
        request_file_path = urlparts.path.strip("/")

        if not os.path.exists(request_file_path):
            self.path = "index.html"

        return super().do_GET()


def get_library_root(library: types.ModuleType):
    return pathlib.Path(getattr(library, "__path__", [library.__file__])[-1])


kine_path = get_library_root(kine)
typing_extensions_path = get_library_root(typing_extensions)


def get_all_dependancies(deps: list[str]) -> list[str]:
    libs = pipdeptree.get_installed_distributions(True, True)

    tree = pipdeptree.PackageDAG.from_pkgs(libs)
    dep_tree = tree.filter(deps, [])

    import_names: list[str] = []

    for pkg in dep_tree:
        pkg: pipdeptree.DistPackage

        name: str = pkg.project_name

        distro = import_meta.distribution(name)

        files = distro.files

        if not files:
            raise Exception(f"Cannot find path data for package {name}")

        library_files = [file for file in files if not file.parts[0].endswith("dist-info")]

        lib_name = library_files[-1].parts[0]
        import_names.append(lib_name.removesuffix(".py"))

    return import_names


@click.group()
def cli():
    """Cli for building Kine webassembly projects."""


@cli.command()
@click.argument("name")
@click.pass_context
def new(ctx: click.Context, name: str):
    """Creates a new project with the foldername of NAME"""

    try:
        os.mkdir(name)
    except FileExistsError:
        return print("Folder already exists with that name")

    os.chdir(name)
    init((name,))


@cli.command()
@click.argument("name")
def init(name: str | None = None):
    """Initializes a project in the current directory with NAME or the current directories name"""

    cwd = pathlib.Path.cwd()
    config_file = cwd / "kine.toml"
    build_dir = cwd / "build"
    src_dir = cwd / "src"
    index_file = cwd / "index.html"

    config_file.write_text(
        f"""[project]
name = "{name}"
dependancies = []
"""
    )

    build_dir.mkdir(exist_ok=True)
    src_dir.mkdir(exist_ok=True)
    init_file = src_dir / "__init__.py"
    init_file.write_text(
        """from kine import *
from kine.renderers.wasm import *

from .app import app

async def main():
    await start_wasm(app())
"""
    )

    app_file = src_dir / "app.py"
    app_file.write_text(
        """from kine import *
from kine.renderers.wasm import *

@component
def app(cx: Scope):
    return cx.render(div[
        p[
            "Hello, World!"
        ]
    ])
"""
    )

    index_file.write_text(
        """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.jsdelivr.net/pyodide/v0.21.3/full/pyodide.js"></script>
    <title>{{name}}</title>
</head>
<body>
    <div id="main"></div>
    <script>{{script}}</script>
</body>
</html>
"""
    )


@cli.command()
def clean():
    """Cleans the build directory and all build artifacts"""

    build_dir = pathlib.Path.cwd() / "build"

    shutil.rmtree(build_dir)
    build_dir.mkdir()


@cli.command()
@click.pass_context
def build(ctx: click.Context):
    """Builds the project"""

    ctx.invoke(clean)

    cwd = pathlib.Path.cwd()
    config_file = cwd / "kine.toml"
    build_dir = cwd / "build"
    src_dir = cwd / "src"
    index_file = cwd / "index.html"

    config = toml.loads(config_file.read_text())

    modules = [
        (src_dir, build_dir / "src.tar.gz"),
        (kine_path, build_dir / "kine.tar.gz"),
        (typing_extensions_path, build_dir / "typing_extensions.tar.gz"),
    ]

    deps = config["project"]["dependancies"]

    for lib_name in get_all_dependancies(deps):
        modules.append((get_library_root(importlib.import_module(lib_name)), build_dir / f"{lib_name}.tar.gz"))

    for input_folder, output_file in modules:
        with tarfile.open(output_file, "w:gz") as tar:
            tar.add(input_folder, arcname=os.path.basename(input_folder))

    module_names = [f'"{module.name}"' for _, module in modules]
    module_imports = f"[{', '.join(module_names)}]"

    script = f"""
async function loadModule(pyodide, name) {{
    let res = await fetch(`${{document.location.origin}}/${{name}}`);
    let buff = await res.arrayBuffer();

    pyodide.unpackArchive(buff, "gztar");
}}
let pyodide;

async function main() {{
    pyodide = await loadPyodide({{args:["-OO"]}});

    for (mod of {module_imports}) {{
        await loadModule(pyodide, mod);
    }};

    pyodide.runPythonAsync("from src import main; await main()")
}}
main();
"""

    index = index_file.read_text().replace("{{name}}", config["project"]["name"]).replace("{{script}}", script)
    build_index = build_dir / "index.html"
    build_index.write_text(index)


@cli.command()
@click.option("--port", "-p", default=8080, type=int, help="The port to run the http server on")
@click.option("--host", "-h", default="127.0.0.1", help="The host to run the http server on")
def serve(port: int, host: str):
    """Runs a http server with the built web app"""

    os.chdir("build")
    httpd = ThreadingHTTPServer((host, port), Handler)

    print(f"Running server on http://{host}:{port}")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.shutdown()


cli()

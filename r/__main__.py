import argparse
import pathlib
import toml
import shutil
import tarfile
import os.path
import r
import typing_extensions
import types
import importlib
import os
from http.server import HTTPServer
from http.server import SimpleHTTPRequestHandler
from urllib.parse import urlparse

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        urlparts = urlparse(self.path)
        request_file_path = urlparts.path.strip('/')

        if not os.path.exists(request_file_path):
            self.path = 'index.html'

        return SimpleHTTPRequestHandler.do_GET(self)

cwd = pathlib.Path.cwd()
config_file = cwd / "r.toml"
build_dir = cwd / "build"
src_dir = cwd / "src"
index_file = cwd / "index.html"

def get_library_root(library: types.ModuleType):
    return pathlib.Path(getattr(library, "__path__", [library.__file__])[-1])

r_path = get_library_root(r)
typing_extensions_path = get_library_root(typing_extensions)

parser = argparse.ArgumentParser("r")
parser.add_argument("command")

args = parser.parse_args()

def wasm_init(name: str | None = None):
    name = name or cwd.name

    config_file.write_text(
f"""[project]
name = "{name}"
dependancies = []
""")

    build_dir.mkdir(exist_ok=True)
    src_dir.mkdir(exist_ok=True)
    init_file = src_dir / "__init__.py"
    init_file.write_text(
"""import asyncio
from r import *
from r.renderers.wasm import *

from .app import app

async def main():
    await start_wasm(app())
""")

    app_file = src_dir / "app.py"
    app_file.write_text(
"""import asyncio
from r import *
from r.renderers.wasm import *

@component
def app(cx: Scope):
    return cx.render(div[
        p[
            "Hello, World!"
        ]
    ])
""")

    index_file.write_text("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.jsdelivr.net/pyodide/v0.21.3/full/pyodide.js"></script>
    <title>{name}</title>
</head>
<body>
    <div id="main"></div>
    <script>{script}</script>
</body>
</html>
""")

def wasm_clean():
    shutil.rmtree(build_dir)
    build_dir.mkdir()

def wasm_build() -> None:
    wasm_clean()
    config = toml.loads(config_file.read_text())

    modules = [
        (src_dir, build_dir / "src.tar.gz"),
        (r_path, build_dir / "r.tar.gz"),
        (typing_extensions_path, build_dir / "typing_extensions.tar.gz")
    ]

    for dep in config["project"]["dependancies"]:
        modules.append((get_library_root(importlib.import_module(dep)), build_dir / f"{dep}.tar.gz"))

    for input_folder, output_file in modules:
        with tarfile.open(output_file, "w:gz") as tar:
            tar.add(input_folder, arcname=os.path.basename(input_folder))

    module_imports = "\n\t".join(f"await loadModule(pyodide, \"{name.name}\");" for _, name in modules)

    script = f"""
async function loadModule(pyodide, name) {{
    let res = await fetch(`${{document.location.origin}}/${{name}}`);
    let buff = await res.arrayBuffer();

    pyodide.unpackArchive(buff, "gztar");
}}

async function main() {{
    let pyodide = await loadPyodide();

    {module_imports}

    pyodide.runPythonAsync("from src import main; await main()")
}}
main();
"""

    index = index_file.read_text().format(name=config["project"]["name"], script=script)
    build_index = build_dir / "index.html"
    build_index.write_text(index)

if args.command == "build":
    wasm_build()
elif args.command == "init":
    wasm_init()
elif args.command == "serve":
    os.chdir("build")
    httpd = HTTPServer(('', 8000), Handler)
    print("Serving app on port 8000 ...")
    httpd.serve_forever()

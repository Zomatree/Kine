regenerate-interpreter:
    tsc .\kine\renderers\web\interpreter.ts --lib es6,dom,dom.iterable --outFile .\kine\renderers\web\interpreter.js --downlevelIteration
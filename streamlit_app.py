import streamlit as st
import os
from inspect import getmembers, isfunction
import importlib.util

# Use filenames from ./examples as examples.
# TODO: Find author of the file and add it here.
examples = [
    f for f in os.listdir("examples") if not f.startswith("_") and f != "overview.py"
]
examples.insert(0, "overview.py")
examples_names = [e.rstrip(".py").replace("_", " ").title() for e in examples]
examples_dict = dict(zip(examples_names, examples))

example = st.sidebar.radio("Examples", list(examples_dict.keys()))
spec = importlib.util.spec_from_file_location(
    "module.name", f"examples/{examples_dict[example]}"
)
example_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(example_module)

# Use function names in ./examples/overview.py as methods.
methods = [m for m in getmembers(example_module, isfunction)]
methods_names = [m[0].replace("_", " ").title() for m in methods]
methods_dict = dict(zip(methods_names, methods))
method = st.sidebar.radio("Method", list(methods_dict.keys()))
methods_dict[method][1]()

"""
pyenv activate py3.11_virtualenv_test
"""
from main_supervisor2 import *


if not yx_debug:
    script_callbacks.on_ui_tabs(on_ui_tabs)
else:
    demo = on_ui_tabs()
    demo[0][0].launch()

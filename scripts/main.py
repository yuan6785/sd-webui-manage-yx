"""
pyenv activate py3.11_virtualenv_test
"""
# from scripts.main_supervisor2 import *
from scripts.main_finally import *


if not yx_debug:
    script_callbacks.on_ui_tabs(on_ui_tabs)
else:
    demo = on_ui_tabs()
    demo[0][0].queue(concurrency_count=3)
    demo[0][0].launch()

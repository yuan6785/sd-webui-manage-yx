"""
pyenv activate py3.11_virtualenv_test
"""
# from scripts.main_supervisor2 import *
from scripts.main_finally import *


if not yx_debug:
    script_callbacks.on_ui_tabs(on_ui_tabs)
else:
    demo = on_ui_tabs()
    demo[0][0].queue(concurrency_count=3)  # 加这个非常重要，否则有时候会界面出现卡死的情况，无法重试
    demo[0][0].launch()

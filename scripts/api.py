"""
可以参考dreambooth和controlnet的api.py
"""
from typing import Union

import numpy as np
from fastapi import FastAPI, Body
import copy
import pydantic
import sys

import gradio as gr

from modules.api.models import *
from modules.api import api

from scripts import external_code
from scripts.processor import *


def server_manage_yx_api(_: gr.Blocks, app: FastAPI):
    @app.get("/servermanageyx/version")
    async def version():
        return {"version": '1.0'}


try:
    import modules.script_callbacks as script_callbacks

    script_callbacks.on_app_started(server_manage_yx_api)
except:
    pass

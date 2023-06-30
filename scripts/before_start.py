"""
sd启动前的一些配置
"""
# This helper script scans folders for wildcards and embeddings and writes them
# to a temporary file to expose it to the javascript side

import glob
from pathlib import Path

import gradio as gr
import yaml
from modules import script_callbacks, scripts, sd_hijack, shared
import requests
from gradio import Blocks
from fastapi import FastAPI
from typing import Optional, Dict, Any
import os


def on_ui_settings():
    """
    @des: 启动时候动态设置配置项
    参考:
    /Users/yuanxiao/workspace/0yxgithub/stable-diffusion-webui/modules/shared.py
    参考
    /Users/yuanxiao/workspace/0yxgithub/stable-diffusion-webui/modules/script_callbacks.py
    环境变量参考: 直接容器内读云函数环境变量 https://www.alibabacloud.com/help/zh/function-compute/latest/environment-variables
    >>> import os
    >>> os.environ.get("FC_FUNCTION_NAME", "unknown")
    'sd1'
    >>> os.environ.get("FC_SERVICE_NAME", "unknown")
    'machine-learning'
    >>> 
    """
    # 从这里/Users/yuanxiao/workspace/0yxgithub/userful_scripts/project_pre/yxpre/pre_make.py生成拷贝过来---重要---
    domain_map_name = {"6": "chenmin", "7": "duanyi", "8": "huangzhipeng", "9": "lihai", "10": "lvxing", "11": "mahaiteng", "12": "wangjiaxin", "13": "zhaoyue", "14": "wangluo", "15": "sunfuxing", "16": "daixinxin", "17": "yangguoqing", "18": "zhaozilong", "19": "jiaokun", "20": "lijie", "21": "liyonggang", "22": "panzhonghao", "23": "yuganfeng", "24": "zhaolili", "25": "wangxiaoqing", "26": "zhanghongzhi", "27": "hehuaying", "28": "jixiaomin", "29": "lvshanshan",
                    "30": "wangshijie", "31": "dongboyan", "32": "lixue", "33": "zhaoliang", "34": "gaohong", "35": "fengdehai", "36": "yangwenyuan", "37": "huangdannuo", "38": "liuzhenxing", "39": "zhengmingyu", "40": "lizheng", "41": "zhanglian", "42": "luzhenyu", "43": "hejie", "44": "yaozhiqian", "45": "zhangqing", "46": "jiashuting", "47": "gaiwenxing", "48": "zhangtianzi", "49": "zhangyu", "50": "wangqi", "51": "zhangwei", "52": "lifang", "53": "liangkuan", "54": "sunjian", "1":"yuanxiao"}
    # 获取当前ubuntu服务器的主机名
    try:
        # 获取环境变量FC_FUNCTION_NAME的值
        func_name = os.environ.get("FC_FUNCTION_NAME", "")
        serv_name = os.environ.get("FC_SERVICE_NAME", "")
        if serv_name == "machine-learning":
            domain_no = func_name.replace("sd", "").strip()
        elif serv_name == "stable-diffusion-fun-2":
            domain_no = str(int(func_name.replace("sd", "").strip()) + 50)
        else:
            domain_no = "-1"
    except:
        domain_no = "-1"
    username = domain_map_name.get(domain_no, "unknown")
    outputs_root = "outputs"  # outputs---输出到nas, test_outputs---会输出到云函数的容器文件夹下面
    shared.opts.set("outdir_samples", f"")   # 系统配置选项
    shared.opts.set("outdir_txt2img_samples", f"{outputs_root}/{username}/txt2img-images")   # 系统配置选项
    shared.opts.set("outdir_img2img_samples", f"{outputs_root}/{username}/img2img-images")   # 系统配置选项
    shared.opts.set("outdir_extras_samples", f"{outputs_root}/{username}/extras-images")   # 系统配置选项
    shared.opts.set("outdir_grids", f"")   # 系统配置选项
    shared.opts.set("outdir_txt2img_grids", f"{outputs_root}/{username}/txt2img-grids")   # 系统配置选项
    shared.opts.set("outdir_img2img_grids", f"{outputs_root}/{username}/img2img-grids")   # 系统配置选项
    # print("动态设置输出路径配置项完成-------by yx")
        


script_callbacks.on_ui_settings(on_ui_settings) 

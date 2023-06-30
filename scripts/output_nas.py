# This helper script scans folders for wildcards and embeddings and writes them
# to a temporary file to expose it to the javascript side
print(a)
import glob
from pathlib import Path

import gradio as gr
import yaml
from modules import script_callbacks, scripts, sd_hijack, shared
import requests
from gradio import Blocks
from fastapi import FastAPI
from typing import Optional, Dict, Any
import socket
try:
    from modules.paths import extensions_dir, script_path

    # Webui root path
    FILE_DIR = Path(script_path)

    # The extension base path
    EXT_PATH = Path(extensions_dir)
except ImportError:
    # Webui root path
    FILE_DIR = Path().absolute()
    # The extension base path
    EXT_PATH = FILE_DIR.joinpath('extensions')

# 插件物理路径
EXT_INNER_PATH = Path(scripts.basedir())


# 从这里/Users/yuanxiao/workspace/0yxgithub/userful_scripts/project_pre/yxpre/pre_make.py生成拷贝过来---重要---
domain_map_name = {"6": "chenmin", "7": "duanyi", "8": "huangzhipeng", "9": "lihai", "10": "lvxing", "11": "mahaiteng", "12": "wangjiaxin", "13": "zhaoyue", "14": "wangluo", "15": "sunfuxing", "16": "daixinxin", "17": "yangguoqing", "18": "zhaozilong", "19": "jiaokun", "20": "lijie", "21": "liyonggang", "22": "panzhonghao", "23": "yuganfeng", "24": "zhaolili", "25": "wangxiaoqing", "26": "zhanghongzhi", "27": "hehuaying", "28": "jixiaomin", "29": "lvshanshan",
                   "30": "wangshijie", "31": "dongboyan", "32": "lixue", "33": "zhaoliang", "34": "gaohong", "35": "fengdehai", "36": "yangwenyuan", "37": "huangdannuo", "38": "liuzhenxing", "39": "zhengmingyu", "40": "lizheng", "41": "zhanglian", "42": "luzhenyu", "43": "hejie", "44": "yaozhiqian", "45": "zhangqing", "46": "jiashuting", "47": "gaiwenxing", "48": "zhangtianzi", "49": "zhangyu", "50": "wangqi", "51": "zhangwei", "52": "lifang", "53": "liangkuan", "54": "sunjian"}


def on_ui_settings():
    """
    @des: 启动时候动态设置配置项
    参考:
    /Users/yuanxiao/workspace/0yxgithub/stable-diffusion-webui/modules/shared.py
    参考
    /Users/yuanxiao/workspace/0yxgithub/stable-diffusion-webui/modules/script_callbacks.py
    """
    # 获取sd云函数的域名
    with gr.Blocks(analytics_enabled=False) as output_demo:
        pass
    #
    # shared.opts.set("outdir_samples", f"")   # 系统配置选项
    # shared.opts.set("outdir_txt2img_samples",
    #                 f"outputs/{username}/txt2img-images")   # 系统配置选项
    # shared.opts.set("outdir_img2img_samples",
    #                 f"outputs/{username}/img2img-images")   # 系统配置选项
    # shared.opts.set("outdir_extras_samples",
    #                 f"outputs/{username}/extras-images")   # 系统配置选项
    # shared.opts.set("outdir_grids", f"")   # 系统配置选项
    # shared.opts.set("outdir_txt2img_grids",
    #                 f"outputs/{username}/txt2img-grids")   # 系统配置选项
    # shared.opts.set("outdir_img2img_grids",
    #                 f"outputs/{username}/img2img-grids")   # 系统配置选项
    # # print("动态设置输出路径配置项完成-------by yx")


# script_callbacks.on_ui_tabs(on_ui_settings)

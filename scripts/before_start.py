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
import json
from gradio import Blocks
from fastapi import FastAPI
from typing import Optional, Dict, Any
import os
from xpinyin import Pinyin


# def get_domain_by_config_bak(domain_no):
#     """
#     @des: 从配置中心读取域名配置--废弃
#     """
#     username_pinyin = "unknown"
#     try:
#         config_sub_domain = "conf.private.playdayy.cn"
#         url = f"https://{config_sub_domain}/api/Config/app/com.playdayy.sd.serverless-enter?env=CN-PRD"
#         headers = {
#             'Authorization': 'Basic Y29tLnBsYXlkYXl5LnNkLnNlcnZlcmxlc3MtZW50ZXI6QUgxbERuejRmUyN3cDNLMw==',
#             'User-Agent': 'Apifox/1.0.0 (https://www.apifox.cn)',
#             'Accept': '/',
#             'Host': f'{config_sub_domain}',
#             'Connection': 'keep-alive'
#         }
#         retry_count = 3
#         while retry_count > 0:
#             try:
#                 response = requests.get(url, headers=headers, timeout=(30, 30))
#                 break
#             except:
#                 retry_count -= 1
#                 continue
#         # data = response.content.decode("utf-8")
#         # print(data)
#         # print(response.json()[0])
#         for item in response.json():
#             if str(item['value']) == str(domain_no):
#                 username = item['key']
#                 # 取拼音
#                 username_pinyin = Pinyin().get_pinyin(username).replace('-', '')
#                 break
#     except:
#         pass
#     return username_pinyin


def get_domain_by_config(domain_no):
    """
    @des: 从ezconfig配置中心读取域名配置---只用于云函数版本
          需要配置环境变量
    """
    username_pinyin = "unknown"
    try:
        #
        if 1:
            #
            env_config_file = "/share/sdwebui_public/public/custom_envs_config.json"
            if os.path.exists(env_config_file):
                with open(env_config_file, "r") as f:
                    env_config = f.read()
                evv_config_json = json.loads(env_config)
            else:
                raise Exception("env_config_file not exists")
            #
            sd_users_env = evv_config_json.get("sd_aliyun_func_users", {})
            #
            os.environ['EZCONFIG_ENV'] = sd_users_env.get("EZCONFIG_ENV", '')
            os.environ['EZCONFIG_APPID'] =  sd_users_env.get("EZCONFIG_APPID", '')
            os.environ['EZCONFIG_SECRET'] =  sd_users_env.get("EZCONFIG_SECRET", '')
            os.environ['EZCONFIG_HOST'] =  sd_users_env.get("EZCONFIG_HOST", '')
        # 这一句必须放在os.environ配置后面
        from ezconfig_client import loader
        res = loader.get_latest_config()
        # {'version': 7, 'config_data': {'userServerKV': {'张三': 27, '李四': 43, ...}, 'version': '1.0.1'}, ...}
        config_data = res.get("config_data", {})
        userServerKV = config_data.get("userServerKV", {})
        for k, v in userServerKV.items():
            if str(v) == str(domain_no):
                username = k
                # 取拼音
                username_pinyin = Pinyin().get_pinyin(username).replace('-', '')
                return username_pinyin
    except:
        pass 
    return "unknown"


def set_nas_output():
    """
    @des: 启动时候动态设置配置项
    环境变量参考: 直接容器内读云函数环境变量 https://www.alibabacloud.com/help/zh/function-compute/latest/environment-variables
    这个文档里面还可以根据python的sdk配置环境变量，可实现动态设置环境变量，如果每个人对应的域名是不固定的，就可以按这个方式来设置。
    ---------------------
    通过SDK配置环境变量
    以Python SDK为例，环境变量的参数为environmentVariables，参数取值以字典形式存储。创建、更新、获取环境变量的示例代码如下。

    创建环境变量
    # coding: utf-8
    import fc2
    import os

    client = fc2.Client(
        endpoint='your endpoint', # 接入点信息。具体信息，请参见https://www.alibabacloud.com/help/en/function-compute/latest/endpoints。
        # 阿里云账号AccessKey拥有所有API的访问权限，建议您使用RAM用户进行API访问或日常运维。
        # 建议不要把AccessKey ID和AccessKey Secret保存到工程代码里，否则可能导致AccessKey泄露，威胁您账号下所有资源的安全。
        # 本示例以将AccessKeyID和AccessKeySecret保存在环境变量中实现身份验证为例。
        # 运行本示例前请先在本地环境中设置环境变量ALIBABA_CLOUD_ACCESS_KEY_ID和ALIBABA_CLOUD_ACCESS_KEY_SECRET。
        # 在FC Runtime运行环境下，配置执行权限后，ALIBABA_CLOUD_ACCESS_KEY_ID和ALIBABA_CLOUD_ACCESS_KEY_SECRET环境变量会自动被设置。
        accessKeyID=os.getenv('ALIBABA_CLOUD_ACCESS_KEY_ID'), # AccessKey ID，阿里云身份验证，在RAM控制台创建。
        accessKeySecret=os.getenv('ALIBABA_CLOUD_ACCESS_KEY_SECRET') # AccessKey Secret，阿里云身份验证，在RAM控制台创建。

    client.create_service('test')

    client.create_function(
        'test', 'test_env', 'python3',  'main.handler',
        codeDir='/path/to/code/', environmentVariables={'testKey': 'testValue'})

    #test 服务名
    #test_env 函数名
    #python3  Runtime类型
    #main.handler 请求处理程序
    #codeDir 代码目录
    #environmentVariables 要配置的环境变量

    res = client.get_function('test', 'test_env')

    print(res.data)
    更新环境变量
    client.update_function(
        'test', 'test_env', 'python3',  'main.handler',
        codeDir='/path/to/code/', environmentVariables={'newKey': 'newValue'})
    res = client.get_function('test', 'test_env')
    print res.data            
    获取环境变量
    resp = client.get_function('test', 'test_env')
    env = func['environmentVariables']
    在代码中使用环境变量
    假设配置的环境变量为{"key":"val"}，以下为各运行环境读取并打印此环境变量值的方法。

    Node.jsPythonJavaPHPC

    import os
    value = os.environ.get('key')
    print(value)
    """
    # 从这里/Users/yuanxiao/workspace/0yxgithub/userful_scripts/project_pre/yxpre/pre_make.py生成拷贝过来---重要---
    # domain_map_name = {"6": "chenmin", "7": "duanyi", "8": "huangzhipeng", "9": "lihai", "10": "lvxing", "11": "mahaiteng", "12": "wangjiaxin", "13": "zhaoyue", "14": "wangluo", "15": "sunfuxing", "16": "daixinxin", "17": "yangguoqing", "18": "zhaozilong", "19": "jiaokun", "20": "lijie", "21": "liyonggang", "22": "panzhonghao", "23": "yuganfeng", "24": "zhaolili", "25": "wangxiaoqing", "26": "zhanghongzhi", "27": "hehuaying", "28": "jixiaomin", "29": "lvshanshan",
    #                    "30": "wangshijie", "31": "dongboyan", "32": "lixue", "33": "zhaoliang", "34": "gaohong", "35": "fengdehai", "36": "yangwenyuan", "37": "huangdannuo", "38": "liuzhenxing", "39": "zhengmingyu", "40": "lizheng", "41": "zhanglian", "42": "luzhenyu", "43": "hejie", "44": "yaozhiqian", "45": "zhangqing", "46": "jiashuting", "47": "gaiwenxing", "48": "zhangtianzi", "49": "zhangyu", "50": "wangqi", "51": "zhangwei", "52": "lifang", "53": "liangkuan", "54": "sunjian"}
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
    # username = domain_map_name.get(domain_no, "unknown")
    username = get_domain_by_config(domain_no)
    outputs_root = "outputs"  # outputs---输出到nas, test_outputs---会输出到云函数的容器文件夹下面
    shared.opts.set("outdir_samples", f"")   # 系统配置选项
    shared.opts.set("outdir_txt2img_samples",
                    f"{outputs_root}/{username}/txt2img-images")   # 系统配置选项
    shared.opts.set("outdir_img2img_samples",
                    f"{outputs_root}/{username}/img2img-images")   # 系统配置选项
    shared.opts.set("outdir_extras_samples",
                    f"{outputs_root}/{username}/extras-images")   # 系统配置选项
    shared.opts.set("outdir_grids", f"")   # 系统配置选项
    shared.opts.set("outdir_txt2img_grids",
                    f"{outputs_root}/{username}/txt2img-grids")   # 系统配置选项
    shared.opts.set("outdir_img2img_grids",
                    f"{outputs_root}/{username}/img2img-grids")   # 系统配置选项
    # print("动态设置输出路径配置项完成-------by yx")


# 暂不启用
script_callbacks.on_ui_settings(set_nas_output)

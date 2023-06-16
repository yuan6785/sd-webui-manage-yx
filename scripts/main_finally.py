"""
pyenv activate py3.11_virtualenv_test
"""
from scripts.public import *


def on_ui_tabs():
    with gr.Blocks(analytics_enabled=False) as depth_lib_1:
        # if 0: # 测试
        #     gr.Markdown(
        #         """
        #     # Hello World!
        #     Start typing below to see the output.
        #     """)
        #     inp = gr.Textbox(placeholder="What is your name?")
        #     out = gr.Textbox()
        #     # inp.change(welcome, inp, out)
        #     # 创建按钮
        #     btn = gr.Button(value="提交")
        #     # 绑定按钮事件
        #     btn.click(welcome, inputs=[inp], outputs=[out])
        if 1:
            # 用于显示日志的html框
            btn = gr.Button(value="查看日志")
            html = gr.HTML("")
            with gr.Row(visible=False):
                html_not_log_error = gr.HTML("""""")
            # 绑定按钮事件---#参考/Users/yuanxiao/workspace/0yxgithub/userful_scripts/gradio_test/test_html_display_log.py
            btn.click(fn=get_sd_log, inputs=[], outputs=[html])
            btn.click(fn=None, _js=gundongttiao_js,
                      inputs=[], outputs=[html_not_log_error])
        if 0:
            # 用于显示日志的html框
            html1 = gr.HTML("""
            <a id="yxyxyx_viewlog_hreda111" href='.' target='_blank'>查看日志(新标签页)</a>
            """)
            depth_lib_1.load(_js=getlog_js)
        if 1: # 保活:  会导致前端页面报错 Uncaught (in promise) TypeError: Cannot read ，但不影响啥
            # input
            text_input1 = gr.Textbox(lines=1, label="保活时间(分钟),默认15分钟,最大不超过120分钟")
            text_output1 = gr.Textbox(lines=1, label="保活输出")
            with gr.Row(visible=False):
                greet_btn = gr.Button("隐藏保活操作按钮", elem_id='yxyx_keepalive_298432423')
                greet_btn.click(fn=keepalive_output, inputs=None, outputs=[
                                text_output1], api_name="greet123af")
                stop_btn = gr.Button("停止保活", elem_id='yxyx_keepalive_675675')
                stop_btn.click(fn=stop_keepalive, inputs=None, outputs=[
                                text_output1], api_name="3123123fdsfds")
                html_not_error = gr.HTML("""""")
            greet_btn1 = gr.Button("更新保活时间", elem_id='yxyx_keepalive_12deqe')
            greet_btn1.click(fn=None, inputs=[
                            text_input1], outputs=[html_not_error], _js=get_window_url_params, api_name="greet1fds312")
            # demo加载的时候执行js函数
            depth_lib_1.load(fn=None, inputs=[text_input1],
                    outputs=[html_not_error],  _js=get_window_url_params)
        if 0:
            # 重启服务按钮
            btn_reboot = gr.Button(value="重启服务(重启后请刷新浏览器)")
            # 重启日志输出
            html_reboot = gr.HTML("")
            # 绑定按钮事件
            btn_reboot.click(reboot_sd, inputs=[], outputs=[html_reboot])
        if 0:
            # 重启服务按钮
            btn_reboot1 = gr.Button(value="重启实例(重启后请刷新浏览器)")
            # 重启日志输出
            html_reboot1 = gr.HTML("")
            # 绑定按钮事件
            btn_reboot1.click(reboot_sd_instance, inputs=[], outputs=[html_reboot1])
    return [(depth_lib_1, "server manage", "depth_lib_1")]  # 界面上的选项

用于sdwebui的插件,用于sd的重启，日志查看等等


https://gradio.app/custom-CSS-and-JS/   自定义css和js

gradio.html可以自由些html，嵌套iframe等

https://github.com/gradio-app/gradio/discussions/2932   js文件加载



下面是一个定制html的例子

#########################################3
您无法通过 加载脚本gr.HTML，但您可以在页面加载时运行 JavaScript 函数，从而将您的 JavaScript 代码设置为globalThis，从而对整个页面可见
import gradio as gr

html = """
<html>
  <body>
    <h1>My First JavaScript</h1>
    <button type="testButton" onclick="testFn()"> Start </button>
    <p id="demo"></p>

  </body>
</html>
"""

scripts = """
async () => {
   // set testFn() function on globalThis, so you html onlclick can access it
    globalThis.testFn = () => {
      document.getElementById('demo').innerHTML = "Hello"
    }
}
"""

with gr.Blocks() as demo:   
    input_mic = gr.HTML(html)
    out_text  = gr.Textbox()
    # run script function on load,
    demo.load(None,None,None,_js=scripts)

if __name__ == "__main__":   
    demo.launch()
#########################################3
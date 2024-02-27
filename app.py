import gradio as gr

def greet(name):
    return "Hello, hola " + name + "!!"

iface = gr.Interface(fn=greet, inputs="text", outputs="text")
iface.launch()
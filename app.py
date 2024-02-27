import gradio as gr

def greet(name):
    return "Hello, hola, aloha " + name + "!!"

iface = gr.Interface(fn=greet, inputs="text", outputs="text")
iface.launch(auth=("admin", "pass1234"))
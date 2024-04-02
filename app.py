import gradio as gr
import time
from baf import bafta
#Funciones adicionales

def authenticate(username, password):
    usuarios = [("usuario1", "contraseña1"), ("usuario2", "contraseña2")]
    for u, p in usuarios:
        if username == u and password == p:
            return True
    return False

#Función principal
def greet(name):
    tokens = bafta()
    print(tokens)
    return "Tervetuloa " + name + tokens + "!!"

iface = gr.Interface(fn=greet, inputs="text", outputs="text")

iface.launch()
#iface.launch(auth=("admin", "pass1234"))
#iface.launch(auth=authenticate)
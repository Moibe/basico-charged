import gradio as gr

#Funciones adicionales

def authenticate(username, password):
    usuarios = [("usuario1", "contraseña1"), ("usuario2", "contraseña2")]
    for u, p in usuarios:
        if username == u and password == p:
            return True
    return False

#Función principal
def greet(name):
    return "Hello, hola, aloha " + name + "!!"

iface = gr.Interface(fn=greet, inputs="text", outputs="text")


iface.launch(share=True)
#iface.launch(auth=("admin", "pass1234"))
#iface.launch(auth=authenticate)
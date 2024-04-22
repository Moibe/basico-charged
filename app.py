import gradio as gr
import time
import flux_capacitor

#Funciones adicionales
def authenticate(username, password):
    usuarios = [("usuario1", "contraseña1"), ("usuario2", "contraseña2")]
    for u, p in usuarios:
        if username == u and password == p:
            return True
    return False

#Función principal
def runpy(access, content):

    print("Welcome...")
    print("Initializing app and servers...")
    
    tokens_now, result = flux_capacitor.do(access, content)
        
    return tokens_now, result

with gr.Blocks() as demo: 

    input_userfile = gr.Text(label="Userfile")
    input_content = gr.Text(label="content")
    btn = gr.Button(value="Submit")
    output_tokens = gr.Text(label="Tokens")
    output_resultado = gr.Text(label="Resultado")

    #Actions
    btn.click(runpy, inputs=[input_userfile, input_content], outputs=[output_tokens, output_resultado])

#iface = gr.Interface(fn=runpy, inputs=["text", "text"], outputs=["text, text"])

demo.launch()
#iface.launch(auth=("admin", "pass1234"))
#iface.launch(auth=authenticate)
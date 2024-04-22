import time
import nodes
import gradio_client

def saldoParaAccion(tokens):
  #Donde 1 es el cobro por acción, es decir, tiene capacidad por lo menos de realizar una acción.
   if tokens >= 1: 			
    return True

   else:
    print("Not enough tokens to perform the action, add more.")
    return False


def getResult(content): 

    print("Processing content: ", content)
    time.sleep(1)

    if nodes.work == "picswap":
      print("Work specs ok, action: ",  nodes.work)
      time.sleep(1)

      #Aquí es donde ya no será un llamado de api si no la app itself. Listo OK!.
      result = f"y el resultado es: Tervetuluo {content} !"
      #Revisa si la app en cuestión podría regresar algún resultado extraño además del esperado. Esto se revisa en la otra App.
      return result
    
    else: 
      print("Work specs aren't correct. Please fix or contact app.")
      #Regresa cero si el trabajo no se realizó por haber especificado incorrectamente el Work.
      return 0
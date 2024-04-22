import theApp
import nodes
import sulkuGateway
import time

#Flux capacitor une la Autenticación y la App.
def do(access, content):

	print("Entré a flux_capacitor.do...")
	time.sleep(8)
	#AUTENTICACIÓN#
 	#Obten cantidad de tokens dispobibles vía Sulku para ese usuario.
	resultado = sulkuGateway.getTokens(access)

	#Un try para convertirlo en entero porque quizá bajo alguna circunstancia no sea un número lo que regresa y marcará error al aplicarle int().
	try:
		resultado = int(resultado)
	except ValueError:
		# Manejar el error de conversión a entero
		print("Error 401: return value is not int.")
		
	except Exception as e:
		# Manejar otros errores genéricos
		print("Error 402: Unexpected error convertirng the result:", e)
		
	#Si el resultado es un entero, es token.
	if isinstance(resultado, int): 
		#El númmero si es un entero.
		tokens = resultado
		continuar = True
		print("Access granted.")
		print("Your amount of available tokens is: ", tokens)
	else: 
		print("Message:", resultado)
		continuar = False

	#ACCIÓN#
	print("Performing action, processing...")
	if continuar is True and theApp.saldoParaAccion(tokens):
		resultado = theApp.getResult(content)
		print("Process completed.")
	else: 
		print(f"Message: Not enough tokens to perform {nodes.work} action.")
		resultado = 0
      
	#CHARGE TOKENS
	#Si se generó un resultado de AI entonces si hay que debitar el token correspondiente basado en la regla propia de la app.
	if resultado != 0:
		sulkuGateway.debitTokens(access, nodes.work)
	else:
		"No tokens will be charged because no outcome was produced."
		
	return tokens, resultado
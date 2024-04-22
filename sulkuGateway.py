import time
import nodes
import requests
import gradio_client

def getTokens(sulkukey):

    print("Entre a SulkiGateway...")
    time.sleep(7)

    print("A punto de hacer llamado a cliente de API via Sulku...")
    time.sleep(3)
    try:
        client = gradio_client.Client("Moibe/sulku", nodes.hf_token, verbose=False)
        resultado = client.predict(sulkukey, api_name="/getTokens")
        
        return resultado
    
    # except gradio_client.exceptions.APIError as e:
    #     print(f"Error 404 calling the API: {e}")
    #     return None
    except requests.exceptions.RequestException as e:
        print(f"Error 405: Network error, {e}")
        return None


def debitTokens(sulkukey, work):
     
    client = gradio_client.Client(nodes.validator, nodes.hf_token, verbose=False)
        
    tokens = client.predict(
            sulkukey,
            work,
            api_name="/debitTokens"
    ) 

    print(f"Available tokens now: {tokens}.")   
    time.sleep(1) 

    return tokens

import paramiko
import time
import os

def bafta():

  ssh = paramiko.SSHClient()
  ssh.load_host_keys("itrst")

  #Ahora obtendremos nuestra secret key para poder entrar a ese servidor.
  # Obtiene la ruta del directorio actual
  project_dir = os.getcwd()
  # Crea la ruta completa al archivo `id_rsa`
  key_filename = os.path.join(project_dir, "go")

  #Imprimo el path del id_rsa, en éste casi también interno al proyecto, pero podría ser con las que debe tener el equipo, intrucciones abajo*
  print(key_filename)

  #*Instrucciones para obtener la llave de donde usualmente están las llaves en cada tipo de sistema operativo de forma general.
  #por eso obtiene la ruta del directorio de usuario de ese sistema operativo.
  #key_filename = os.path.expanduser(os.path.join("~", ".ssh", "id_rsa"))
  #key_filename = "/id_rsa"
  #print("Path a key_filename es: ", key_filename)


  #key_filename = "~/.ssh/id_rsa"
  #print(key_filename)
  #print("Esto es key_filename:", key_filename)
  #private_key = paramiko.RSAKey.from_private_key_file(key_filename)

  #Conexión hacia el servidor con tus credenciales.
  #Al tener una key no requieres el password.
  ssh.connect("opal2.opalstack.com", username="moibe", key_filename=key_filename)
  #Una vez que tenemos la conexión ssh, creamos un sftp (SSH File Transfer Protocol)
  sftp = ssh.open_sftp()

  # Listar archivos en el directorio actual
  #sftp.listdir("./")

  print(ssh)

  #Cargado de archivo, origen (aquí está within the project) y el destino final y nombre de a donde irá.
  #sftp.put("./brisenoestrello.txt" , "/home/moibe/apps/holocards/vallecanales.txt")

  # Ruta del archivo remoto
  archivo_remoto = "/home/moibe/apps/holocards/vallecanales.txt"

  with sftp.open(archivo_remoto, 'rb') as archivo:
    # Leer el contenido del archivo como bytes
    contenido_bytes = archivo.read()

    # Decodificar los bytes a Unicode usando la codificación UTF-8
    contenido_unicode = contenido_bytes.decode('utf-8')

    # Agregar el texto "- Revisado." al string
    contenido_final = int(contenido_unicode) - 1

    contenido_final = str(contenido_final)

    # Imprimir el contenido
    print(contenido_final)

    # Abrir el archivo remoto en modo escritura
  with sftp.open(archivo_remoto, 'w') as archivo:
    # Escribir el contenido final en el archivo
    archivo.write(contenido_final)

  sftp.close()
  ssh.close()

  return contenido_final
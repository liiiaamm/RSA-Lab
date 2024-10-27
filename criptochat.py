import sys
import os 
import re
import rsa
RESET = "\033[0m"
OKBLUE = "\033[94m" #Inputs en azul
OKGREEN = "\033[92m" #Prints en verde
OKRED = "\033[91m" #Errores en rojo


class UserNotFoundError(Exception):
    pass


def leer_ficheros(fichero:str):
    """
    Lee las líneas de un archivo y devuelve una lista de las mismas sin espacios en blanco.

    Args:
        fichero (str): La ruta del archivo que se desea leer.

    Returns:
        list: Lista de cadenas de texto representando cada línea del archivo sin espacios al inicio y final.
    """
    datos = []
    with open(fichero,"r") as f:
        datos.extend([line.strip() for line in f])
    return datos 

def cargar_claves(usuario1,usuario2):
    """
    Verifica si existen las claves de los usuarios especificados y carga las claves del primer usuario (públicas y privada)
    y del segundo usuario (pública) si están disponibles.

    Args:
        usuario1 (str): Nombre del primer usuario para cargar sus claves públicas y privada.
        usuario2 (str): Nombre del segundo usuario para cargar su clave pública.

    Raises:
        UserNotFoundError: Si alguno de los archivos de claves no existe.

    Returns:
        list: Lista con las claves de usuario, o None si algún archivo de claves no existe.
    """
    usuario1_pr = f"Usuarios/priv_{usuario1}.txt"
    usuario1_pb = f"Usuarios/pub_{usuario1}.txt"
    usuario2_pb = f"Usuarios/pub_{usuario2}.txt"
    usuarios = [usuario1_pr,usuario1_pb,usuario2_pb]

    try:
        if not all([os.path.isfile(archivo) for archivo in usuarios]):
            raise UserNotFoundError()  
    except UserNotFoundError as error:
        print(f"{OKRED}Algún usuario introducido no se encuentra en la base de datos{RESET}")
        return None


    claves = []
    pattern = r".+\/(.+)\.txt"
    for usuario in usuarios:
        datos = leer_ficheros(usuario)
        claves.append(datos)
    return claves


def interactions(claves):
    """
    Permite la interacción del usuario para cifrar o descifrar mensajes mediante RSA, utilizando las claves 
    previamente cargadas.

    Args:
        claves (list): Lista de claves de los usuarios que se usarán para cifrar y descifrar.

    Raises:
        ValueError: Si ocurre un error al intentar descifrar un mensaje no válido.

    Returns:
        None: No retorna ningún valor.
    """
    usuario_pr_1 = claves[0]
    usuario_pb_1 = claves[1]
    usuario_pb_2 = claves[2]
 
    while True:
        accion =  input(f"{OKBLUE}Desea cifrar (C), descifrar (D) o salir (S)?{RESET}")
        if accion == "C":
            mensaje = input(f"{OKBLUE}Escribe el mensaje a cifrar: {RESET}")
            cifrado = rsa.cifrar_cadena_rsa(mensaje,int(usuario_pb_2[0]),int(usuario_pb_2[1]),int(usuario_pb_2[2]))
            print(f"{OKGREEN}Tu mensaje cifrado es: \n {' '.join(map(str, cifrado))}{RESET}")
        elif accion == "D":
            mensaje_cifrado = input(f"{OKBLUE}Escribe el mensaje cifrado(recuerda introdirlo con el formato número espacio número): {RESET}").split(" ")
            mensaje_cifrado_int = [int(numero) for numero in mensaje_cifrado]
            try:
                descrifrado = rsa.descifrar_cadena_rsa(mensaje_cifrado_int,int(usuario_pb_1[0]),int(usuario_pr_1[0]),int(usuario_pb_1[2]))
                print(f"{OKGREEN}Tu mensaje descrifrado es: \n {descrifrado}{RESET}")
            except ValueError:
                pass
        elif accion == "S":
            print(OKGREEN,"Saliendo del programa",RESET)
            break
        else: 
            print(OKRED, "Introduzca una opción válida", RESET)


if __name__ == "__main__":
    """
    Punto de entrada principal del programa. Verifica que se introduzcan dos usuarios y 
    carga sus claves correspondientes para interactuar con el programa de cifrado/descifrado.
    """
    if len(sys.argv) != 3:
        print(OKRED,"Uso: python criptochat.py <usuario1> <usuario2>",RESET)
        sys.exit(1)

    usuario1 = sys.argv[1]
    usuario2 = sys.argv[2]

    claves = cargar_claves(usuario1,usuario2)
    if claves is not None:
        interactions(claves)
    

    



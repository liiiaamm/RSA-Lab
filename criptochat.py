import sys
import os 

RESET = "\033[0m"
OKBLUE = "\033[94m" #Inputs en azul
OKGREEN = "\033[92m" #Prints en verde
OKRED = "\033[91m" #Errores en rojo


class UserNotFoundError(Exception):
    pass


def leer_ficheros(fichero:str):
    datos = []
    with open(fichero,"r") as f:
        datos.append(f.read())

    return datos 

def cargar_claves(usuario1,usuario2):
    usuario1_pr = f"Usuarios/priv_{usuario1}.txt"
    usuario1_pb = f"Usuarios/pub_{usuario1}.txt"
    usuario2_pb = f"Usuarios/pub_{usuario2}.txt"
    usuarios = [usuario1_pr,usuario1_pb,usuario2_pb]

    if  not (os.path.isfile(usuario1_pb) and os.path.isfile(usuario1_pr) and os.path.isfile(usuario2_pb)):
        raise UserNotFoundError("El usuario introducido no está en el sistema")

    claves = {}
    pattern = r".+\/(.+)\.txt"
    for usuario in usuarios:
        datos = leer_ficheros(usuario)
        claves[usuario] = datos #esto se cambiaria por lo comentado
    print(claves)
    return claves


def interactions(clavesU1,clavesU2):
    while True:
        accion =  input(f"{OKBLUE}Desea cifrar (C), descifrar (D) o salir (S)?{RESET}")
        if accion == "C":
            mensaje = input(f"{OKBLUE}Escribe el mensaje a cifrar: {RESET}")
        elif accion == "D":
            mensaje_cifrado = input(f"{OKBLUE}Escribe el mensaje cifrado: {RESET}")
        elif accion == "S":
            print(OKGREEN,"Saliendo del programa",RESET)
            break
        else: 
            print(OKRED, "Introduzca una opción válida", RESET)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(OKRED,"Uso: python criptochat.py <usuario1> <usuario2>",RESET)
        sys.exit(1)

    usuario1 = sys.argv[1]
    usuario2 = sys.argv[2]

    try:
        clavesU1,clavesU2 = cargar_claves(usuario1,usuario2)
    except UserNotFoundError as UNFE:
        print(OKRED, f"Error de Usuario: {UNFE}", RESET)
        sys.exit(1)

    interactions(clavesU1,clavesU2)


import sys

RESET = "\033[0m"
OKBLUE = "\033[94m" #Inputs en azul
OKGREEN = "\033[92m" #Prints en verde
OKRED = "\033[91m" #Errores en rojo

class UserNotFoundError(Exception):
    pass


def cargar_claves(usuario1,usuario2):
    """
    Comprueba si los usuarios existen y carga las claves publico/privadas del usuario 1 y las publicas del usuario 2
    """
    if usuario1 == "no_existe" or usuario2 == "no_existe":
        raise UserNotFoundError("El usuario introducido no está en el sistema")
    clavesU1 = {'publica': 'clave_publica_usuario1', 'privada': 'clave_privada_usuario1'}
    clavesU2 = {'publica': 'clave_publica_usuario2'}
    return clavesU1,clavesU2


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


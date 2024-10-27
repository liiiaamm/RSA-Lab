import rsa 
import os 
import sys

RESET = "\033[0m"
OKBLUE = "\033[94m" #Inputs en azul
OKGREEN = "\033[92m" #Prints en verde
OKRED = "\033[91m" #Errores en rojo
OKPURPLE = "\033[35m"

DIRECTORIO ="Usuarios"

class InfMayorSup(Exception):
    pass


def print_titulo():
    """
    Crea un título en grande con la palabra criptografía de color morado.
    
    Args:
        None
    
    Raises:
        None
    
    Returns:
        None
    """
    print(rf"""{OKPURPLE}    __  ____   ____  ____  ______   ___    ____  ____    ____  _____  ____   ____ 
   /  ]|    \ |    ||    \|      | /   \  /    ||    \  /    ||     ||    | /    |
  /  / |  D  ) |  | |  o  )      ||     ||   __||  D  )|  o  ||   __| |  | |  o  |
 /  /  |    /  |  | |   _/|_|  |_||  O  ||  |  ||    / |     ||  |_   |  | |     |
/   \_ |    \  |  | |  |    |  |  |     ||  |_ ||    \ |  _  ||   _]  |  | |  _  |
\     ||  .  \ |  | |  |    |  |  |     ||     ||  .  \|  |  ||  |    |  | |  |  |
 \____||__|\_||____||__|    |__|   \___/ |___,_||__|\_||__|__||__|   |____||__|__|
                                                                                  
                                                {RESET}""")
    

def inputs() -> tuple[str, int, int, int]:
    """
    Solicita al usuario su nombre y tres valores numéricos relacionados con la generación de una clave RSA:
    - Un límite inferior para la selección de números primos.
    - Un límite superior para la selección de números primos.
    - Un valor de padding.

    Realiza las siguientes validaciones:
    - Convierte los límites y el padding a valores absolutos enteros.
    - Verifica que el límite inferior sea menor que el límite superior.
    
    Returns:
        tuple: Una tupla que contiene el nombre (str), el límite inferior (int), el límite superior (int), 
        y el valor de padding (int).
    
    Raises:
        ValueError: Si los valores ingresados para los límites o el padding no pueden ser convertidos a enteros.
        InfMayorSup: Si el límite inferior es mayor o igual al límite superior.
    """
    nombre = input(f"{OKBLUE}Cual es tu nombre?:{RESET} \n")
    lim_inf = input(f"{OKBLUE}Introduce el valor mínimo del primo usado para generar tu clave RSA:{RESET} \n")
    lim_sup = input(f"{OKBLUE}Introduce el valor máximo del primo usado para generar tu clave RSA:{RESET} \n")
    padding = input(f"{OKBLUE}Introduce el número de cifras padding para la comunicación:{RESET} \n")

    try:
        lim_inf = abs(int(lim_inf))
        lim_sup = abs(int(lim_sup))
    except:
        raise ValueError("Los valores ingresados para los límites no pueden ser convertidos a enteros")

    if lim_inf >= lim_sup:
        raise InfMayorSup("El límite inferior es mayor o igual que el superior")

    try:
        padding = abs(int(padding))

    except:
        raise ValueError("El padding no ha sido introducido correctamente")

    return nombre, lim_inf,lim_sup,padding


def crear_directorios(directorio: str) -> None:
    """
    Crea un directorio en la ruta especificada. Si el directorio ya existe, se notifica al usuario.
    
    Args:
        directorio (str): La ruta del directorio que se desea crear.
    
    Raises:
        FileExistsError: Si el directorio ya existe.
        Exception: Si ocurre algún otro error durante la creación del directorio.
    
    Returns:
        None: No retorna ningún valor.
    """
    try:
        os.mkdir(directorio)
        print(f"Directorio '{directorio}' creado correctamente")
    except FileExistsError:
        print(f"{OKRED}Directorio '{directorio}' ya existe.{RESET}")
    except Exception as e:
        print(f"{OKRED}Un error ha ocurrido: {e}{RESET}")


def crear_ficheros_en_ruta(directorio: str, nombre: str, n: int, e: int, padding: int, d: int) -> None:
    """
    Crea dos archivos en la ruta especificada, uno público y otro privado, y escribe los valores correspondientes
    para la generación de claves RSA.

    Args:
        directorio (str): La ruta del directorio donde se crearán los archivos.
        nombre (str): El nombre base para los archivos.
        n (int): Valor 'n' para el archivo público.
        e (int): Valor 'e' para el archivo público.
        padding (int): Número de cifras de padding.
        d (int): Valor 'd' para el archivo privado.

    Returns:
        None: No retorna ningún valor, pero crea dos archivos en la ruta especificada.
    
    Creates:
        pub_{nombre}.txt: Archivo que contiene los valores 'n', 'e' y 'padding'.
        priv_{nombre}.txt: Archivo que contiene el valor 'd'.
    """
    nombre_pb = f"pub_{nombre}.txt"
    nombre_pr = f"priv_{nombre}.txt"
    ruta_pb = os.path.join(directorio,nombre_pb)
    ruta_pr = os.path.join(directorio,nombre_pr)
    with open(ruta_pb,"w") as pb:
        pb.write(f"{str(n)}\n")
        pb.write(f"{str(e)}\n")
        pb.write(f"{str(padding)}\n")
    
    with open(ruta_pr,"w") as pr:
        pr.write(f"{str(d)}\n")

if __name__ == "__main__":
    print_titulo()
    try:
        nombre,lim_inf,lim_sup,padding = inputs()
    except ValueError as VE:
        print(f"{OKRED} Error de valor: {VE}{RESET}")
        sys.exit(1)
    except InfMayorSup as IMS:
        print(f"{OKRED} Error de límites: {IMS}{RESET}")
        sys.exit(1)
    n,e,d = rsa.generar_claves(lim_inf,lim_sup)
    crear_directorios(DIRECTORIO)
    crear_ficheros_en_ruta(DIRECTORIO,nombre,n,e,padding,d)


    

    
    
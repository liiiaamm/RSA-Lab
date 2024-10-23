import sys 
import rsa 
import os 
class InfMayorSup(Exception):
    pass
def print_titulo():
    print(r"""    __  ____   ____  ____  ______   ___    ____  ____    ____  _____  ____   ____ 
   /  ]|    \ |    ||    \|      | /   \  /    ||    \  /    ||     ||    | /    |
  /  / |  D  ) |  | |  o  )      ||     ||   __||  D  )|  o  ||   __| |  | |  o  |
 /  /  |    /  |  | |   _/|_|  |_||  O  ||  |  ||    / |     ||  |_   |  | |     |
/   \_ |    \  |  | |  |    |  |  |     ||  |_ ||    \ |  _  ||   _]  |  | |  _  |
\     ||  .  \ |  | |  |    |  |  |     ||     ||  .  \|  |  ||  |    |  | |  |  |
 \____||__|\_||____||__|    |__|   \___/ |___,_||__|\_||__|__||__|   |____||__|__|
                                                                                  
                                                """)
    

def inputs()-> tuple:
    nombre = input("Cual es tu nombre?: \n")
    lim_inf = input("Introduce el valor mínimo del primo usado para generar tu clave RSA: \n")
    lim_sup = input("Introduce el valor máximo del primo usado para generar tu clave RSA: \n")
    padding = input("Introduce el número de cifras padding para la comunicación: \n")

    try:
        lim_inf = abs(int(lim_inf))
        lim_sup = abs(int(lim_sup))
    except ValueError:
        print("Los límites no han sido introducidos correctamente")

    try: 
        if lim_inf >= lim_sup:
            raise InfMayorSup()


    except InfMayorSup:
        print("El límite inferior es mayor que el superior")

    try:
        padding = abs(int(padding))

    except ValueError:
        print("El padding no ha sido introducido correctamente")

    return nombre, lim_inf,lim_sup,padding

def crear_directorios(directorio:str):
    
    try:
        os.mkdir(directorio)
        print(f"Directorio '{directorio}' creado correctamente")
    except FileExistsError:
        print(f"Directorio '{directorio}' ya existe.")
   
    except Exception as e:
        print(f"Un error ha ocurrido: {e}")

def crear_ficheros_en_ruta(directorio:str,nombre:str,n:int,e:int,padding:int,d:int):
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
    nombre,lim_inf,lim_sup,padding = inputs()
    n,e,d = rsa.generar_claves(lim_inf,lim_sup)
    directorio ="Usuarios"
    crear_directorios(directorio)
    crear_ficheros_en_ruta(directorio,nombre,n,e,padding,d)
    



    

    
    

    
    
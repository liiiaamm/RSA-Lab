import sys 
import rsa 
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


if __name__ == "__main__":
    print_titulo()
    nombre,lim_inf,lim_sup,padding = inputs()
    n,e,d = rsa.generar_claves(lim_inf,lim_sup)
    with open(f"pub_{nombre}.txt","w") as pb:
        pb.write(n)
        pb.write(e)
        pb.write(padding)
    
    with open(f"priv_{nombre}.txt","w") as pr:
        pr.write(d)

    
    
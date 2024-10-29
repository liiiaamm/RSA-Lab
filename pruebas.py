import rsa
import time
import random
import rsa


mensaje_descifrado = rsa.cifrar_cadena_rsa("hola me llamo liam",362267027,65537,2)
print(mensaje_descifrado)
print(rsa.descifrar_cadena_rsa(mensaje_descifrado))
t2 = time.time()

362267027
65537
2


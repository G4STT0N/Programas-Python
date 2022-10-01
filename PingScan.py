import os
import sys
import platform
from datetime import datetime

print(" ")
print(" ")
print(" ░█▀▀█ ▀█▀ ░█▄─░█ ░█▀▀█  ░█▀▀▀█ ░█▀▀█ ─█▀▀█ ░█▄─░█ ")
print(" ░█▄▄█ ░█─ ░█░█░█ ░█─▄▄  ─▀▀▀▄▄ ░█─── ░█▄▄█ ░█░█░█ ")
print(" ░█─── ▄█▄ ░█──▀█ ░█▄▄█  ░█▄▄▄█ ░█▄▄█ ░█─░█ ░█──▀█")
print(" ")

ip = input("[*] Ingresa la Clase: ")
ipDividida = ip.split('.')

try:
    red = ipDividida[0]+'.'+ipDividida[1]+'.'+ipDividida[2]+'.'
    comienzo = int(input("[*] Ingresa el Numero de Comienzo de la SubRed: "))
    fin = int(input("[*] Ingresa el Numero en el que Deseas Acabar el Barrido: "))
except:
    print("[!] Error")
    sys.exit(1)


if (platform.system()=="Windows"):
    ping = "ping -n 1"
else :
    ping = "ping -c 1"
    
tiempoInicio = datetime.now()
print("[*] El escaneo se está realizando desde",red+str(comienzo),"hasta",red+str(fin))
print(" ")
for subred in range(comienzo, fin+1):
    direccion = red+str(subred)
    response = os.popen(ping+" "+direccion)
    for line in response.readlines():
        if ("ttl" in line.lower()):
            print(direccion," | ESTATUS -> ACTIVO")
            break
            
tiempoFinal = datetime.now()
tiempo = tiempoFinal - tiempoInicio
print(" ")
print("[*] El escaneo ha durado %s"%tiempo)
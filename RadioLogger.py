from threading import Timer
from datetime import datetime
import requests
import os

############################## VARIABLES ################################################
# Poner las Variables entre comillas -> 'variable'

name = 'CASUPA 94.1' # NOMBRE DE LA RADIO

url = 'http://stm1.ifantasy.com.br:7256/;' # URL DE LA RADIO

############################### CODIGO ##################################################


dt = datetime.now()
fecha = dt.strftime('%d-%m-%Y, %H-%M-%S')

print('')
print('')
print ('██████╗░░█████╗░██████╗░██╗░█████╗░  ██╗░░░░░░█████╗░░██████╗░░██████╗░███████╗██████╗░')
print ('██╔══██╗██╔══██╗██╔══██╗██║██╔══██╗  ██║░░░░░██╔══██╗██╔════╝░██╔════╝░██╔════╝██╔══██╗')
print ('██████╔╝███████║██║░░██║██║██║░░██║  ██║░░░░░██║░░██║██║░░██╗░██║░░██╗░█████╗░░██████╔╝')
print ('██╔══██╗██╔══██║██║░░██║██║██║░░██║  ██║░░░░░██║░░██║██║░░╚██╗██║░░╚██╗██╔══╝░░██╔══██╗')
print ('██║░░██║██║░░██║██████╔╝██║╚█████╔╝  ███████╗╚█████╔╝╚██████╔╝╚██████╔╝███████╗██║░░██║')
print ('╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░╚════╝░  ╚══════╝░╚════╝░░╚═════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝')
print('')
print('Nombre de la Radio -> ' + name)
print('')
print('URL -> ' + url)
print('')
print('Nombre del Archivo -> ' + fecha)
print('')
print('STATUS:')
print ('GRABANDO ...')

tiempo = 3600  #segundos para el STOP -> 1 hora = 3600 segundos

def timeout():
    print ('STOP') 
    os.system("taskkill /IM cmd.exe")
    
t = Timer(tiempo, timeout)

def grabar():
    r = requests.get(url, stream=True)
    with open(str(fecha)+'.mp3', 'wb') as f:
        try:
            for block in r.iter_content(1024):
                f.write(block)
        except KeyboardInterrupt:
            pass

t.start()
grabar()


# By: Gaston Ferreira
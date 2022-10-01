#!/usr/bin/python3 

import shlex, subprocess

print()
print()
print('░██████╗░░░░██████╗░██╗████████╗░██████╗')
print('██╔════╝░░░░██╔══██╗██║╚══██╔══╝██╔════╝')
print('██║░░██╗░░░░██████╦╝██║░░░██║░░░╚█████╗░')
print('██║░░╚██╗░░░██╔══██╗██║░░░██║░░░░╚═══██╗')
print('╚██████╔╝██╗██████╦╝██║░░░██║░░░██████╔╝')
print('░╚═════╝░╚═╝╚═════╝░╚═╝░░░╚═╝░░░╚═════╝░')
print()
print()

user = subprocess.check_output(["whoami"],universal_newlines=True)
print ('[*]Usuario Actual del Sistema: ', user)

uname = subprocess.check_output(["uname"],universal_newlines=True)
print ('[*]Tipo de Kernel: ', uname)

date = subprocess.check_output(["date"],universal_newlines=True)
print ('[*]Fecha y Hora: ', date)

pwd = subprocess.check_output(["pwd"],universal_newlines=True)
print ('[*]Directorio Actual: ', pwd)

hostnamectl = subprocess.check_output(["hostnamectl"],universal_newlines=True)
print ('[*]Informacion del Host: ')
print (hostnamectl)


ifconfig = subprocess.check_output(["ifconfig"],universal_newlines=True)
print ('[*]Informacion Ethernet: ')
print (ifconfig)

print ('[*]Puertos Escuchando : ')
subprocess.call(shlex.split('ss exclude ESTABLISHED exclude CLOSED  -s'))








 


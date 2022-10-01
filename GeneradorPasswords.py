import random
from werkzeug.security import generate_password_hash

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

print()

rango = int(input("Nuemro de Contraseñas Max(100): "))
print()
longitud = int(input("Longitud de Contraseñas Max(86): "))
print()

minus = "abcdefghijklmnopqrstuvwxyz"
mayus = minus.upper()
numeros = "0123456789"
simbolos = "@()[]{}+*.:,;/-_'¡!€%$&="

base = minus + mayus + numeros + simbolos


for _ in range(rango):
    muestra = random.sample(base, longitud)
    password = "".join(muestra)
    password_Encrip = generate_password_hash(password)
    print("{} => {}".format(password, password_Encrip))
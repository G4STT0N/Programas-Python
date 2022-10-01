import os 
import time

print("")
print("░█████╗░██╗░░░██╗████████╗░█████╗░  ██████╗░███████╗███╗░░██╗██╗░█████╗░██╗░█████╗░")
print("██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗  ██╔══██╗██╔════╝████╗░██║██║██╔══██╗██║██╔══██╗")
print("███████║██║░░░██║░░░██║░░░██║░░██║  ██████╔╝█████╗░░██╔██╗██║██║██║░░╚═╝██║██║░░██║")
print("██╔══██║██║░░░██║░░░██║░░░██║░░██║  ██╔══██╗██╔══╝░░██║╚████║██║██║░░██╗██║██║░░██║")
print("██║░░██║╚██████╔╝░░░██║░░░╚█████╔╝  ██║░░██║███████╗██║░╚███║██║╚█████╔╝██║╚█████╔╝")
print("╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░░╚════╝░  ╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝╚═╝░╚════╝░╚═╝░╚════╝░")
print("")
print("")
print("")
print("EL EQUIPO SE REINICIARA EN: " + "4" + " HORA")

time.sleep(14400) # set segundos para el renicio

# 1 hora = 3600 segundos
# 2 hora = 7200 segundos
# 3 hora = 10800 segundos
# 4 hora = 14400 segundos
# 5 hora = 18000 segundos
# 6 hora = 21600 segundos
# 1 dia = 86400 segundos

print("Reiniciando en 5 segundos")
time.sleep(5)
print("REINICIANDO")
os.system("shutdown /r /t 1") # Orden para el reinicio


 
# cd Documents/GitHub/pantallaCam/Scripts && activate && cd .. && color f
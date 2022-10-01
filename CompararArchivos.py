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

archivo1 = input("Ruta del Archivo 1: ")
archivo2 = input("Ruta del Archivo 1: ")
print()

f1 = open(archivo1, "r")   
f2 = open(archivo2, "r")   
  
i = 0
C = 0
NC = 0  

for line1 in f1: 
    i += 1
      
    for line2 in f2: 
          
        
        if line1 == line2:
            C = C + 1

            print("Linea ", i, ": CONSIDENCIA")

            print("\tArchivo 1:", line1, end='') 
            print("\tArchivo 2:", line2, end='')      
            print()

        else:
            NC = NC + 1

            print("Linea", i, ": NO CONSIDE") 

            print("\tArchivo 1:", line1, end='') 
            print("\tArchivo 2:", line2, end='')
            print()

        break

f1.close()                                        
f2.close()  
 
print("CONSIDENCIAS: ", C,)        
print("NO CONCIDENCIAS: ", NC,)

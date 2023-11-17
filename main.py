import random

names_string = input("Ingresa los nombres: (Separalos con una coma y espacio): ")
names = names_string.split(", ")
#print(random.choice(names)) Forma rapida de hacerlo
x = len(names) #Calculas cuantos nombres tiene la lista
n = random.randint(0,x-1) #Eliges un numero del 0 al numero de personas
W_Pays = names[n] 

print(f"{W_Pays} invita hoy!")

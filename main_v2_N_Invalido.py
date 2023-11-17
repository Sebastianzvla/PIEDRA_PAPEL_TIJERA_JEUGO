import random

piedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''

tijera = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''
invalido = " \n MANO INVALIDA \n"

Mano = [piedra, papel, tijera, invalido]
n = input("Elige tu mano (1. Piedra)(2.Papel)(3.Tijera): ")

if int(n) < 0 and inr(n) > 3:
  print("Numero invalido")
  n = 4
  

Tu_Mano = int(n)-1
print(Mano[Tu_Mano])

R_PC = random.randint(0,2)
print(Mano[int(R_PC)]+ "Mano de la computadora")

if Tu_Mano == R_PC:
    print("Empate")
elif Tu_Mano == 0 and R_PC == 2:
    print("Ganaste")
elif Tu_Mano == 1 and R_PC == 0:
    print("Ganaste")
elif Tu_Mano == 2 and R_PC == 1:
    print("Ganaste")
else:
    print("Perdiste")

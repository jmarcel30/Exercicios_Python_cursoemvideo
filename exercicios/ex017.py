#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. 
#Calcule e mostre o comprimento da hipotenusa.


# Jeito sem importação 
#co = float(input("Digite o comprimento do cateto oposto"))
#ca = float(input("Digite o comprimento do cateto adjacente"))
#h1 = (co ** 2 + ca ** 2) ** (1/2)
#print(f"A hiputenusa vai medir {h1:.2f}")
import math
co = float(input("Digite o comprimento do cateto oposto"))
ca = float(input("Digite o comprimento do cateto adjacente"))
h1 = math.hypot(co, ca)
print(f"A hiputenusa vai medir {h1:.2f}")
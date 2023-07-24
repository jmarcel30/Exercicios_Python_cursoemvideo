#Crie um algaritmo  que leia  um numero e mostre o seu dobre
# o seu triplo e sua raiz quadrada.

numero = int(input('Digite um numero'))

dobro = numero * 2
triplo = numero *3

quadadra = numero ** (1/2)

print(f'O mumero digitado é {numero} e o dobro dele é {dobro} e o triplo dele é {triplo} e sua raiz quadrada é {quadadra:,.2f}')
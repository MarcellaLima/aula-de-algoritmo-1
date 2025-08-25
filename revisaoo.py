#num1

a = float(input("Digite um numero: "))
b = float(input("Digite outro numero: "))

print("Maior: ", max(a,b))

#correção part1

num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))

if num1>num2:
    print(f"O numero{num1} é maior")
elif num1==num2:
    print(f"São iguais")
else: 
    print(f"O numero{num2} é maior")

#outraforma

def maior(num1,num2):
    if num1>num2:
        print(f"O numero{num1} é maior")
    elif num1>num2:
        print(f"O numero{num2} é maior")
    else:
        print(f"São iguais")

#outraforma

def maior(num1,num2):
    if num1>num2:
        return num1
    elif num1<num2:
        return num2
    else:
        return None
    
num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))

resultado = maior(num1,num2)
                  
if resultado == None:
    print("São iguais")
else:

    print(f"O numero maior é", resultado)

#num2

# Pede ao usuário para digitar um número
numero = int(input("Digite um número: "))

# Cabeçalho da tabuada
print(f"Tabuada do {numero}:")

for i in range(1, 11):
  # Calcula o resultado e imprime
  resultado = numero * i
  print(f"{numero} x {i} = {resultado}")

#num3

def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

#num4

numeros = [10, 20, 30, 40]

soma = 0

contagem = 0

print("A média de cada número é:")

for numero in numeros:
    soma = soma + numero
    
    contagem = contagem + 1
    
    media = soma / contagem
    
    print(f"Número: {numero} -> Média: {media}")



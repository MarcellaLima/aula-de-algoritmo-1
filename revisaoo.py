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
#Lista de exercícios

#Q.01
num = []
for i in range(5):
    n = int(input("Digite o  número inteiro: "))
    num.append(n)
print("Os números digitados foram: ", num)

#Q.02
num = []
for i in range (10):
    n = int(input("Digite um valor: "))
    num.append(n)
    num.sort(reverse=True)
print("Os números em ordem inversa são: ", num)

#Q.03
notas = []
for i in range(4):
    n = float(input("Digite a nota: "))
    notas.append(n)
média = sum(notas)/len(notas)
print("A média das notas é: ", média)

#Q.04
num=[]
par=[]
impar=[]
for i in range(20):
    n= int(input("Digite um número:"))
    num.append(n)
    if n%2==0:
        par.append(n)
    else:
        impar.append(n)
print("Números digitados: ", num)
print("Números pares: ", par)
print("Números ímpares: ", impar)

#Q.05
medias = []
for i in range(10):
    print(f"Aluno {i+1}:")
    notas = []
    for j in range(4):
        nota = float(input(f"Digite a nota {j+1}: "))
        notas.append(nota)  
    media = sum(notas) / 4
    medias.append(media)
#Número de aprovados
aprovados = 0
for media in medias:
    if media >= 7:
        aprovados += 1

print("Número de alunos com média maior ou igual a 7.0:", aprovados)

#Q.06
numeros = []
for i in range(50):
    n=int(input("Digite o valor:"))
    numeros.append(n)
print(numeros)
print (sum(numeros))
print(*(numeros))

#Q.07
idade=[]
altura=[]
for i in range(10):
    print(f"Pessoa {i+1}:")
    id=int(input("Digite a idade:"))
    idade.append(id)
    alt= float(input("Digite a altura:"))
    altura.append(alt)
maior_altura = max(altura)
indice = altura.index(maior_altura)
print(f"A maior altura é {maior_altura} e a idade dessa pessoa é {idade[indice]}")

#Q.08
A = []
for i in range(10):
    num = int(input(f"Digite o {i+1}º número: "))
    A.append(num)
# Calculando a soma dos quadrados
soma_quadrados = 0
for num in A:
    soma_quadrados += num ** 2
# Mostrando o resultado
print("A soma dos quadrados dos elementos é:", soma_quadrados)

#Q.09
lista1 = []
lista2 = []
print("Digite 10 números para a primeira lista:")
for i in range(10):
    num1 = int(input(f"Número {i+1}: "))
    lista1.append(num1)
print("Digite 10 números para a segunda lista:")
for i in range(10):
    num2 = int(input(f"Número {i+1}: "))
    lista2.append(num2)
#Terceira lista intercalando os elementos
lista3 = []
for i in range(20):
    lista3.append(lista1[i])
    lista3.append(lista2[i])
print("A primeira lista é:", lista1)
print("A segunda lista é:", lista2)
print("A terceira lista intercalada é:", lista3)


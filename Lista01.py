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
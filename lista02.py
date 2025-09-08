#Q.01
livros=['O Iluminado', 'O Anticristo', 'A Pediatra']
print(livros)
#Q.02
livros=['O Iluminado', 'O Anticristo', 'A Pediatra']
print('O primeiro livro da lista é:', livros[0])
print('O último livro da lista é:', livros[-1])

#Q.03
livros=['O Iluminado', 'O Anticristo', 'A Pediatra']
livros.append('Harry Potter e a Pedra Filosofal')
livros.append('Cleópatra e Frankeinstein')
print(livros)

#Q.04
livros=['O Iluminado', 'O Anticristo', 'A Pediatra']
livros.insert(1, "Duna")
print(livros)

#Q.05
livros=['O Iluminado', 'O Anticristo', 'A Pediatra']
if 'O Silêncio dos Inocentes' in livros:
    print('O livro foi removido da lista.')
else:
    print('O livro não está na lista.')

#Q.06
numeros=[1, 2, 3, 2, 4, 2, 5]
print('O número 2 aparece', numeros.count(2), 'vezes na lista.')

#Q.07
livros=['O Iluminado', 'O Anticristo', 'A Pediatra']
for livro in livros:
    print("O livro", livro, " é interessante")

#Q.08
idades = [12, 18, 25, 14, 30]
for idade in idades: 
    if idade >= 18:
        print(idade)

#Q.09
valores = [10, 20, 30, 40]
soma=0
for valor in valores:
    soma += valor
print('A soma dos valores é:', soma)

#Q.10
notas=[]
for i in range(2):
    nota1=float(input("Digite a nota do aluno:"))
    nota2=float(input("Digite a nota do aluno:"))
    nota3=float(input("Digite a nota do aluno:"))
nota_aluno = (nota1, nota2, nota3)
notas.append(nota_aluno)
total = 0
contagem = 0
for aluno in notas:
    total += sum(aluno)
    contagem += len(aluno)
media = total / contagem
print(notas)
print("A média das notas é:", media)

#Q.11




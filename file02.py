numero1 = float(input ("Coloque o primeiro número"))
numero2 = float (input ("Coloque o segundo número"))
numero3 = float (input ("Coloque o terceiro número"))
print("Escolha a Operação")
print("1-Soma(+)")
print("2-Subtração (-)")
print("3-Multiplicação (*)")
print("4-Divisão (/)")
opção = input("Digite o número da operação")
if opção == "1":
    resultado = numero1+numero2+numero3
elif opção == "2":
    resultado = numero1 + numero2+numero3
elif opção == "3":
    resultado = numero1*numero2*numero3
elif opção == "4":
    resultado = numero1/numero2/numero3
else:
    resultado= "Opção inválida"
print ("Resultado", resultado)
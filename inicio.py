import math
import random

##Calculos dois numeros
# a = int(input("Digite o primeiro valor: "))
# b = int(input("Digite o segundo valor: "))
# print("Soma: ", a+b, 
#       "\nDiferença: ", a-b, 
#       "\nMédia: ", (a+b)/2, 
#       "\nDistancia: ", math.fabs(a-b), 
#       "\nO maior: ", (a+b+math.fabs(a-b))/2, 
#       "\nO Menor: ", (a+b-math.fabs(a-b))/2)

##Mostrar horas, minutos e segundos dos segundos
# segundos = float(input("Informe os segundos em inteiros: "))
# minutos = segundos//60
# segundos = segundos%60
# horas = minutos//60
# minutos = minutos%60
# print("Horas: ", horas, 
#       "\nMinutos: ", minutos, 
#       "\nSegundos: ", segundos)
##Inverter número
# valor = int(input("Digite um valor de 4 digitos: "))
# digito1 = valor//1000
# resto = valor%1000
# digito2 = resto//100
# resto = resto%100
# digito3 = resto//10
# digito4 = resto%10
# print(digito4*1000+digito3*100+digito2*10+digito1)

##Calculo peso
# altura = float(input("Digite a altura: "))
# sexo = str(input("Digite o sexo (Masculino = M; Feminino = F): "))
# if(sexo == "F" or sexo == "f"):
#     print("Peso ideal feminino: ", 62.1*altura - 44.7)
# elif(sexo == "M" or sexo == "m"):
#     print("Peso ideal masculino: ", 72.7*altura - 58)
# else: print("Sexo inválido")

##Horário do jogo
# hora = int(input("Digite o valor da HORA que INICIOU o jogo: "))
# minuto = int(input("Digite o valor da MINUTO que INICIOU o jogo: "))
# inicio = hora*60+minuto
# hora = int(input("Digite o valor da HORA que FINALIZOU o jogo: "))
# minuto = int(input("Digite o valor da MINUTO que FINALIZOU o jogo: "))
# fim = hora*60+minuto
# if(inicio >= fim):
#     duração = fim+60*24 - inicio
# else: duração = fim - inicio
# print("A duração do jogo foi de",duração//60,"horas e",duração%60,"minutos")

##Número Capicua
# numero = int(input("Digite 4 digitos inteiros: "))

# if(numero < 1111 and numero > 9999): print("Numero inválido!")
# else:
#     numeroInv = numero//1000 + ((numero%1000)//100)*10 + ((numero%100)//10)*100 + (numero%10)*1000
#     if(numero == numeroInv): print("Números capicua!:",numero,numeroInv)
#     else: print("Não são números capcua!",numero,numeroInv)

##Ordem Crescente 3 valores
# valor1 = int(input("Digite o primeiro valor: "))
# valor2 = int(input("Digite o segundo valor: "))
# if(valor2 < valor1):
#     cache = valor1
#     valor1 = valor2
#     valor2 = cache
# valor3 = int(input("Digite o terceiro valor: "))
# if(valor3 < valor1):
#     cache = valor1
#     valor1 = valor3
#     valor3 = valor2
#     valor2 = cache
# if(valor3 < valor2):
#     cache = valor2
#     valor2 = valor3
#     valor3 = cache
# print(valor1, valor2, valor3)

##Ordem Crescente e decrescente 3 valores
# valor1 = int(input("Digite o primeiro valor: "))
# valor2 = int(input("Digite o segundo valor: "))
# valor3 = int(input("Digite o terceiro valor: "))
# maior = valor1
# if(valor2 > maior): maior = valor2
# if(valor3 > maior): maior = valor3
# menor = valor1
# if(valor2 < menor): maior = valor2
# if(valor3 < menor): maior = valor3
# meio = valor1+valor2+valor3 - maior - menor
# print("Crescente:",menor,meio,maior)
# print("Decrescente:",maior,meio,menor)

##Ordem Crescente 4 valores - 1
# valor1 = int(input("Digite o primeiro valor: "))
# valor2 = int(input("Digite o segundo valor: "))
# if(valor2<valor1):
#     cache = valor1
#     valor1 = valor2
#     valor2 = cache
# valor3 = int(input("Digite o terceiro valor: "))
# if(valor3<valor1):
#     cache = valor2
#     valor2 = valor1
#     valor1 = valor3
#     valor3 = cache
# elif(valor3<valor2):
#     cache = valor2
#     valor2 = valor3
#     valor3 = cache
# valor4 = int(input("Digite o quarto valor: "))
# if(valor4<valor1):
#     cache = valor2
#     valor2 = valor1
#     valor1 = valor4
#     valor4 = valor3
#     valor3 = cache
# elif(valor4<valor2):
#     cache = valor2
#     valor2 = valor4
#     valor4 = valor3
#     valor3 = cache
# elif(valor4<valor3):
#     cache = valor3
#     valor3 = valor4
#     valor4 = cache
# print(valor1, valor2, valor3, valor4)

##Ordem Crescente 4 valores - 2
# valor1 = int(input("Digite o primeiro valor: "))
# valor2 = int(input("Digite o segundo valor: "))
# valor3 = int(input("Digite o terceiro valor: "))
# valor4 = int(input("Digite o quarto valor: "))
# if(valor4<valor3): 
#     cache = valor3
#     valor3 = valor4
#     valor4 = cache
# if(valor3<valor2): 
#     cache = valor2
#     valor2 = valor3
#     valor3 = cache
# if(valor2<valor1):
#     cache = valor1
#     valor1 = valor2
#     valor2 = cache
# if(valor4<valor3):
#     cache = valor3
#     valor3 = valor4
#     valor4 = cache
# if(valor3<valor2):
#     cache = valor2
#     valor2 = valor3
#     valor3 = cache
# if(valor4<valor3):
#     cache = valor3
#     valor3 = valor4
#     valor4 = cache
# print(valor1, valor2, valor3, valor4)

##Preço de venda
# custo = float(input("Digite o custo do produto: "))
# if(custo<10): venda = custo*70/100+custo
# if(custo>=10 and custo<30): venda = custo*50/100+custo
# if(custo>=30 and custo<50): venda = custo*40/100+custo
# if(custo>=50): venda = custo*30/100+custo
# print("\nPreço de venda: ",venda)

##Media ponderada
# nota1 = float(input("Digite a primeira nota: "))
# nota2 = float(input("Digite a segunda nota: "))
# nota3 = float(input("Digite a terceira nota: "))
# if(nota2>nota1):
#     cache = nota1
#     nota1 = nota2
#     nota2 = cache
# if(nota3>nota1):
#     cache = nota1
#     nota1 = nota3
#     nota3 = cache
# print("Media: ", (nota1*5+nota2*2.5+nota3*2.5)/(5+2.5+2.5))

##Bhaskara
# a = float(input("Digite o valor de a: "))
# b = float(input("Digite o valor de b: "))
# c = float(input("Digite o valor de c: "))
# delta = b**2 - 4*a*c
# if(delta<0 or a == 0): print("Erro, delta negativo ou divisão por 0")
# else:
#     x1 = (-b + math.sqrt(delta))/(2*a)
#     x2 = (-b - math.sqrt(delta))/(2*a)
#     print(x1, x2)

##Saldo e limite
# saldo = float(input("Informe seu saldo médio: "))
# if(saldo<500): print("Não há limite.")
# elif(saldo>=500 and saldo<1000): print("Limite: ", saldo*8/100)
# else: print("Limite: ", saldo*15/100)

##Seleção aninhada - Quantas raizes?
# a = int(input("Digite o valor de A: "))
# b = int(input("Digite o valor de B: "))
# c = int(input("Digite o valor de C: "))
# delta = b*b - 4*a*c
# if((delta) < 0):
#     print("\nNão há raizes")
# else:
#     if((delta) == 0):
#         x = -b/(2*a)
#         print(f"Possui uma raiz, que é {x}")
#     else:
#         x = (-b + math.sqrt(delta))/(2*a)
#         y = (-b - math.sqrt(delta))/(2*a)
#         print(f"Tem duas raizes, que são: {x}, {y}")

##Seleção aninhada - Condições climáticas
# temp = float(input("Digite a temperatura: "))
# if(temp>30):
#     humid = float(input("Qual a humidade? "))
#     if(humid > (60/100)):
#         print("Tempo quente e humido.")
#     else:
#         print("Tempo quente.")
# else:
#     if(temp<=30 and temp>=20):
#         print("Ameno.")
#     else:
#         if(temp<20 and temp>=10):
#             print("Frio.")
#         else:
#             print("Muito frio.")

##Seleção aninhada
# n1 = float(input("Digite a primeira nota: "))
# n2 = float(input("Digite a segunda nota: "))
# n3 = float(input("Digite a terceira nota: "))
# freq = float(input("Qual a frequencia do aluno? "))
# if(freq<0.75):
#     print(f"Reprovado por faltas! frequencia: {freq}")  
# else:
#     if(n1 > 10 or n2 > 10 or n3 > 10):
#         print("Valor inválido.")
#     else:
#         if(n1 < 0 or n2 < 0 or n3 < 0):
#             print("valor inválido")
#         else:
#             g1 = (n1+n2+n3)/3
#             if(g1 >= 7):
#                 print(f"Aluno aprovado! Media: {g1}")
#             else:
#                 if(g1<4):
#                     print("Aluno reprovado!")
#                 else:
#                     print("Reprovado G1!")
#                     n1 = float(input("Digite a primeira nota: "))
#                     n2 = float(input("Digite a segunda nota: "))
#                     n3 = float(input("Digite a terceira nota: "))
#                     if(n1 > 10 or n2 > 10 or n3 > 10):
#                         print("Valor inválido.")
#                     else:
#                         if(n1 < 0 or n2 < 0 or n3 < 0):
#                             print("valor inválido")
#                         else:
#                             g2 = (n1+n2+n3)/3
#                             media = (g1 + g2) / 2
#                             if(media >= 5):
#                                 print(f"Aluno aprovado em grau 2! Media grau 2: {media}")
#                             else:
#                                 print("Aluno reprovado em grau 2!")

##Seleção aninhada - Notas
# nota = float(input("Digite a nota do aluno de 0 - 100: "))
# if(nota>100 or nota < 0):
#     print("Nota inválida")
# else:
#     if(nota >= 90):
#         print("A")
#     else:
#         if(nota >= 80):
#             print("B")
#         else:
#             if(nota >= 70):
#                 print("C")
#             else:
#                 if(nota >= 60):
#                     print("D")
#                 else:
#                     print("F")

##Seleção aninhada - dia da pascoa em um ano específico
# ano = int(input("Digite um ano entre 1900 e 2099: "))
# if(ano>2099 or ano<1900):
#     print("Valor inválido")
# else:
#     a = ano % 19
#     b = ano % 4
#     c = ano % 7 
#     d = (19 * a + 24) % 30
#     e = (2 * b + 4 * c + 6 * d + 5) % 7
#     dia = 22 + d + e
#     if(ano == 1954 or ano == 1981 or ano == 2049 or ano == 2076):
#         dia = dia - 7
#     else:
#         if(dia>31):
#             print("Data da páscoa:", dia % 31,"de Abril")
#         else:
#             print("Data da páscoa: ", dia, "de Março")

##Dias do calendário - Elif
# mes = int(input("Digite o mês 1 - 12: "))
# if(mes>12 or mes<1):
#     print("Mês inválido")
# elif(mes == 2):
#     dias = 28
# elif(mes == 4 or mes == 6 or mes == 9 or mes == 11):
#     dias = 30
# else:
#     dias = 31
# print(f"Quantidade de dias no mês eh: {dias}")

## Calculo IMC
# peso = float(input("Digite o peso (em kg): "))
# altura = float(input("Digite a altura (em m): "))
# imc = peso/altura**2
# if(imc < 18.6):
#     print("Baixo peso.")
# elif(imc < 25):
#     print("Peso ideal.")
# elif(imc < 30):
#     print("Sobrepeso")
# elif(imc < 35):
#     print("Obesidade grau 1")
# elif(imc < 40):
#     print("Obesidade grau 2")
# else:
#     print("Obesidade grau 3")
# print(f"Seu IMC eh {imc}")

## Pedra, papél e tesoura
# jogador = int(input("Escolha:\n1 - Pedra\n2 - Papel\n3 - Tesoura\n"))
# if(jogador > 3 or jogador < 0):
#     print("Valor inválido!")
# else:
#     computador = random.randint(1,3)
#     print("Computador escolheu: ", computador)
#     if(jogador == computador):
#         print("Deu empate!")

#     elif(jogador == 1):
#         if(computador == 2):
#             print("Computador ganhou! ")
#         else:
#             print("Jogador ganhou!")
#     elif(jogador == 2):
#         if(computador == 3):
#             print("Computador ganhou! ")
#         else:
#             print("Jogador ganhou!")
#     else:
#         if(computador == 1):
#             print("Computador ganhou! ")
#         else:
#             print("Jogador ganhou!")

## Pressão
# sist = int(input("Sistólica: "))
# diast = int(input("Diastólica: "))
# if(sist >= 180 or diast >= 120):
#     print("Crise Hipertensiva.")
# elif(sist >= 140 or diast >= 90):
#     print("Hipertensão Estágio 2.")
# elif(sist >= 130 or diast >= 80):
#     print("Hipertensão Estágio 1.")
# elif(sist >= 120):
#     print("Elevada.")
# else:
#     print("Normal.")
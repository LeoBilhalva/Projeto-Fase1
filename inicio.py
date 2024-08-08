import math

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

# #Inverter número
# valor = int(input("Digite um valor de 4 digitos: "))

# digito1 = valor//1000
# resto = valor%1000
# digito2 = resto//100
# resto = resto%100
# digito3 = resto//10
# digito4 = resto%10

# print(digito4*1000+digito3*100+digito2*10+digito1)

# #Calculo peso
# altura = float(input("Digite a altura: "))
# sexo = str(input("Digite o sexo (Masculino = M; Feminino = F): "))

# if(sexo == "F" or sexo == "f"):
#     print("Peso ideal feminino: ", 62.1*altura - 44.7)
# elif(sexo == "M" or sexo == "m"):
#     print("Peso ideal masculino: ", 72.7*altura - 58)
# else: print("Sexo inválido")


# #Horário do jogo
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
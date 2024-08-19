import string

#Incialização de valores.
meses = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho",
         "Agosto","Setembro","Outubro","Novembro","Dezembro"]

caracteresValidos = "0123456789.,"

somaTemp = 0
qntMesEscaldante = 0

for cont in range(12):

    #Definindo valor para entrar em loop se erro.
    valorInvalido = True
    while (valorInvalido == True):
        contaPontos = 0
        contemLetra = False
        temperatura = str(input(f"Digite a temperatura do mês {meses[cont]} em Celcius: "))

        #Validação da entrada
        #Verificação do tamanho da entrada
        if(len(temperatura) > 10):
            print("Valor muito grande. Deve conter menos de 10 digitos.")
        else:

            #Leitura de cada caracter informado pelo usuário.
            for i in range(len(temperatura)):

                #Contador de pontos
                if temperatura[i] == "." or temperatura[i] == ",":
                    contaPontos += 1

                #Se houver mais de dois sinais de pontuação, sairá dos loop e considerará um erro.
                if contaPontos > 1:
                    print("Valor inserido possui mais de um sinal de pontuação. Por favor, redigite o valor.")
                    break

                #Verifica se o valor contém valores diferentes dos caracteres válidos.
                if temperatura[i] not in caracteresValidos:
                    print("Não deve conter letras, espaços ou caracteres especiais. Utilize somente ',' ou '.'")
                    contemLetra = True
                    break

                #Se o valor inicial for uma vírgula, substitui por um zero e um ponto.
                if temperatura[i] == "," and i == 0:
                    temperatura = "0" + "." + temperatura[1:]
                    print(temperatura)
                
                #Substitui a vírgula por um ponto.
                elif temperatura[i] == ",":
                    temperatura = temperatura[:i] + "." + temperatura[i+1:]
                    print(temperatura)

            #Saída do while se o valor estiver dentro das condições consideradas erros par ao usuário digitar novamente.
            if contemLetra == True or contaPontos > 1:
                continue
            
            #Transformação do str para float para ser possível realizar calculos.
            temperatura = float(temperatura)

            #validação se o valor estiver dentro do intervalo descrito no enunciado.
            if(temperatura < -60 or temperatura > 50):
                print("Valor inválido, informe um valor entre -60 e 50 graus Celcius.")
            else:
                #Incialização dos valores.
                if cont == 0:
                    tempMesMaisQuente = temperatura
                    mesMaisQuente = cont
                    tempMesMenosQuente = temperatura
                    mesMenosQuente = cont

                #Contagem meses escaldantes.
                if temperatura > 33:
                    qntMesEscaldante += 1

                #Identificando mes mais quente.
                if temperatura > tempMesMaisQuente:
                    mesMaisQuente = cont
                    tempMesMaisQuente = temperatura

                #Identificando mes menos quente.
                if temperatura < tempMesMenosQuente:
                    mesMenosQuente = cont
                    tempMesMenosQuente = temperatura

                #Somando valor para coletar a media ao final.
                somaTemp += temperatura

                #Redefinindo valor para sair do loop.
                valorInvalido = False

#Apresentando o resultado
print(f"\nMédia das temperaturas máximas informadas: {somaTemp/(cont+1):.2f}")
print(f"Quantidade de meses escaldantes: {qntMesEscaldante}")
print(f"Mês mais escaldante do ano: {meses[mesMaisQuente]}, com uma temperatura máxima de: {tempMesMaisQuente}")
print(f"Mês menos quente do ano: {meses[mesMenosQuente]}, com uma temperatura máxima de {tempMesMenosQuente}")

# • Temperatura média máxima anual: exibe a média das temperaturas máximas informadas.
# • Quantidade de meses escaldantes: quantidade de meses com temperaturas máximas acima de 33 graus Celsius.
# • Mês mais escaldante do ano: mês que registrou a maior temperatura máxima dentre todos os informados. O mês deve ser escrito na tela por extenso (janeiro a dezembro). 
# • Mês menos quente do ano: mês que registrou a menor temperatura máxima dentre todos os informados. O mês deve ser escrito na tela por extenso (janeiro a dezembro).  
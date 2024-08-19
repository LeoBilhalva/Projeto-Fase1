# Solicitação:
# • Temperatura média máxima anual: exibe a média das temperaturas máximas informadas.
# • Quantidade de meses escaldantes: quantidade de meses com temperaturas máximas acima de 33 graus Celsius.
# • Mês mais escaldante do ano: mês que registrou a maior temperatura máxima dentre todos os informados. O mês deve ser escrito na tela por extenso (janeiro a dezembro). 
# • Mês menos quente do ano: mês que registrou a menor temperatura máxima dentre todos os informados. O mês deve ser escrito na tela por extenso (janeiro a dezembro).  

# Para obtenção dos valores optei por utilizar o formato em str, pois permite realizar uma melhor manipulação dos dados de entrada, como leitura e transformação de caractere por
# caractere, mudar de virgula para pontuação e verificar se o digito está dentro dos caracteres válidos pré-definidos.

# Utilizei os caracteres e dados pré-definidos dos meses, para conseguir apresentar durante a execução do programa usando o contador, e caracteres válidos para
# ter um escopo das entradas válidas no programa.

# Utilizei tecnicas para validação de dados com contadores e booleanos, mesclei os dois para utilizar diferentes tecnicas e práticar o conhecimento. Nada muito especial.

# Utilizei o While pois achei que funcionaria melhor que o for, pois não se possui uma quantidade de repetição fixa prevista.

# Utilizei a tecnica de transformação de str para float, pois é outra funcionalidade que o str nos permite realizar. Essa funcionalidade reforçou minha ideia de utilizar str.

# Os calculos foram procedimentos simples, foi feito uma inicialização prévia para predefinir as entradas da maior e da menor temperatura após a validação da entrada.

# Após analise, não observei mais nada para melhorar. Se identificar, agradeço se houver retorno. Obrigado!
# Meu Github com o projeto e exercicios passados em aula: https://github.com/LeoBilhalva

#Incialização de valores.
meses = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho",
         "Agosto","Setembro","Outubro","Novembro","Dezembro"]

caracteresValidos = "0123456789.,-+"

somaTemp = 0
qntMesEscaldante = 0

for cont in range(12):

    #Definindo valor para entrar em loop se erro.
    reinicio = True
    while (reinicio == True):
        contaPontos = 0
        contNum = 0
        valorErro = False
        temperatura = str(input(f"Digite a temperatura do mês {meses[cont]} em Celcius: "))

        #Validação da entrada.
        #Verificação do tamanho da entrada.
        if(len(temperatura) > 10):
            print("Valor muito grande. Deve conter menos de 10 digitos.")
        elif(len(temperatura) <= 0):
            print("Digite o valor!")
        else:

            #Leitura de cada caracter informado pelo usuário.
            for i in range(len(temperatura)):

                #Verifica se o valor contém valores diferentes dos caracteres válidos.
                if temperatura[i] not in caracteresValidos:
                    print("Não deve conter letras, espaços ou caracteres especiais. Utilize somente ',' ou '.'")
                    valorErro = True
                    break

                #Contar os pontos e substituir virgula por ponto.
                if temperatura[i] == "." or temperatura[i] == ",":
                    contaPontos += 1
                    if temperatura[i] == ",":
                        temperatura = temperatura[:i] + "." + temperatura[i+1:]

                #Se houver mais de dois sinais de pontuação, sairá dos loop e considerará um erro.
                if contaPontos > 1 or (temperatura[i] == "+" and i != 0) or (temperatura[i] == "-" and i != 0):
                    print("Valor inserido possui mais de um sinal de pontuação ou em um local inválido.")
                    valorErro = True
                    break

                #Verificar se contem numeros.
                if contNum == 0 and temperatura[i] in caracteresValidos[:10]:
                    contNum += 1

            #Saída do while se o valor estiver dentro das condições consideradas erros par ao usuário digitar novamente.
            if valorErro == True or contaPontos > 1:
                continue
            elif(contNum == 0):
                print("O valor precisa conter numeros.")
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
                reinicio = False

                #Exibição do valor lido para o usuário.
                print(f"Valor lido para o mês de {meses[i]}: {temperatura}")

#Apresentando o resultado
print(f"\nMédia das temperaturas máximas informadas: {somaTemp/(cont+1):.2f}")
print(f"Quantidade de meses escaldantes: {qntMesEscaldante}")
print(f"Mês mais escaldante do ano: {meses[mesMaisQuente]}, com uma temperatura máxima de: {tempMesMaisQuente}")
print(f"Mês menos quente do ano: {meses[mesMenosQuente]}, com uma temperatura máxima de {tempMesMenosQuente}")
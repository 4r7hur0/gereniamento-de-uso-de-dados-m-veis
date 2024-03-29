''''/*******************************************************************************
Autor: Carlos Arthur Batista Nunes
Componente Curricular: MI de Algoritimos
Concluido em: 24/03/2023
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
******************************************************************************************/'''

#varíaveis contadoras:
contadora_dias = 1
appsusadosdias1 = 0
appsusadosdias2 = 0
appsusadosdias3 = 0
appsusadosdias4 = 0
appsusadosdias5 = 0
appsusadosdias6 = 0
appsusadosdias7 = 0
#Varíaveis acomuladoras:
#Chrome:
dadoschome1 = 0
dadoschome2 = 0
dadoschome3 = 0
dadoschome4 = 0
dadoschome5 = 0
dadoschome6 = 0
dadoschome7 = 0
#Facebook:
dadosfacebook1 = 0
dadosfacebook2 = 0
dadosfacebook3 = 0
dadosfacebook4 = 0
dadosfacebook5 = 0
dadosfacebook6 = 0
dadosfacebook7 = 0
#Instagram:
dadosinstagram1 = 0
dadosinstagram2 = 0
dadosinstagram3 = 0
dadosinstagram4 = 0
dadosinstagram5 = 0
dadosinstagram6 = 0
dadosinstagram7 = 0
#Whatsapp:
dadoswhatsapp1 = 0
dadoswhatsapp2 = 0
dadoswhatsapp3 = 0
dadoswhatsapp4 = 0
dadoswhatsapp5 = 0
dadoswhatsapp6 = 0
dadoswhatsapp7 = 0
#Outros:
dadosoutros1 = 0
dadosoutros2 = 0
dadosoutros3 = 0
dadosoutros4 = 0
dadosoutros5 = 0
dadosoutros6 = 0
dadosoutros7 = 0


#Condições:
cond0 = ('s')
cond1 = ('s')
cond3 = ('S')

# Contadoras para não retonar os dias:
NaoRetorno1 = 0
NaoRetorno2 = 0
NaoRetorno3 = 0
NaoRetorno4 = 0
NaoRetorno5 = 0
NaoRetorno6 = 0
NaoRetorno7 = 0

#entrada de dados:

while not contadora_dias > 7:

    #Bloco responsável por checar se o usuário não digitou um caracter errado:
    try:
        dia = int(input('qual dia da semana [1 a 7]: '))

        #Bloco para evitar que o usuário digite um dia invalido:
        if  1 <= dia <= 7:

            # Bloco para separar os dias da semana. Dia 1:
            if dia == 1:
                #Estrurtura para o usuario não retornar o dia 1:
                if NaoRetorno1 != 1:
                    app = input('''qual o aplicativo?
1.Chrome
2.Facebook
3.Instagram
4.Whatsapp
5.Outros
-> ''').upper()
                    #Bloco responsável por guardar os dados dos aplicativos do dia 1
                    if app == '1' or app == 'CHROME' or app == '2' or app == 'FACEBOOK' or app == '3' or app == 'INSTAGRAM' or app == '4' or app == 'WHATSAPP' or app == '5' or app == 'OUTROS':

                        cond0 = ('S')
                        while not cond0 == ('N'):

                            # Bloco responsável por checar se o usuário não digitou um caracter errado:
                            try:
                                if app == ('CHROME') or app == ('1'):
                                    usodedados = float(input(('quantos bytes usados:')))
                                    dadoschome1 += usodedados
                                    appsusadosdias1 += 1
                                if app == ('FACEBOOK') or app== ('2'):
                                    usodedados = float(input(('quantos bytes usados:')))
                                    dadosfacebook1 += usodedados
                                    appsusadosdias1 += 1
                                if app == ('INSTAGRAM') or app == ('3'):
                                    usodedados = float(input(('quantos bytes usados:')))
                                    dadosinstagram1 += usodedados
                                    appsusadosdias1 += 1
                                if app == ('WHATSAPP') or app == ('4'):
                                    usodedados = float(input(('quantos bytes usados:')))
                                    dadoswhatsapp1 += usodedados
                                    appsusadosdias1 += 1
                                if app == ('OUTROS') or app == ('5'):
                                    usodedados = float(input(('quantos bytes usados:')))
                                    dadosoutros1 += usodedados
                                    appsusadosdias1 += 1
                                cond0 = input('deseja adicionar mais algum aplicativo?[s/n]').upper() # Repetir o loop, caso o usuário digite S.
                                if cond0 == ('S'):
                                    app = input('''qual o aplicativo?
1.Chrome
2.Facebook
3.Instagram
4.Whatsapp
5.Outros
-> ''').upper()
                            except:
                                print('você digitou um caracter invalido. Digite novamente:')
                                continue
                    else:
                        print('você digitou um caracter invalido. Digie novamente.')
                        continue
                else:
                    print('Você não pode retornar os dias.')
                    continue
                NaoRetorno1 += 1
            #Bloco para separar os dias da semana. Dia 2.
            if dia == 2:
                #Estrurtura para o usuario não retornar o dia 2
                if NaoRetorno2 != 2:

                    app = input('''qual o aplicativo?
1.Chrome
2.Facebook
3.Instagram
4.Whatsapp
5.Outros
-> ''').upper()
                    # Bloco responsável por guardar os dados dos aplicativos do dia 2
                    if app == '1' or app == 'CHROME' or app == '2' or app == 'FACEBOOK' or app == '3' or app == 'INSTAGRAM' or app == '4' or app == 'WHATSAPP' or app == '5' or app == 'OUTROS':
                        cond0 = ('S')
                        while not cond0 == ('N'):

                            # Bloco responsável por checar se o usuário não digitou um caracter errado:
                            try:
                                if app == ('CHROME') or app == ('1'):
                                    usodedados = float(input(('quantos bytes usados:')))
                                    dadoschome2 += usodedados
                                    appsusadosdias2 +=1
                                if app == ('FACEBOOK') or app == ('2'):
                                    usodedados = float(input(('quantos bytes usados:')))
                                    dadosfacebook2 += usodedados
                                    appsusadosdias2 += 1
                                if app == ('INSTAGRAM') or app == ('3'):
                                    usodedados = float(input(('quantos bytes usados:')))
                                    dadosinstagram2 += usodedados
                                    appsusadosdias2 += 1
                                if app == ('WHATSAPP') or app == ('4'):
                                    usodedados = float(input(('quantos bytes usados:')))
                                    dadoswhatsapp2 += usodedados
                                    appsusadosdias2 += 1
                                if app == ('OUTROS') or app == ('5'):
                                    usodedados = float(input(('quantos bytes usados:')))
                                    dadosoutros2 += usodedados
                                    appsusadosdias2 += 1
                                cond0 = input('deseja adicionar mais algum aplicativo?[s/n]').upper() # Repetir o loop, caso o usuário digite S
                                if cond0 == 'S' or cond0 == 'N':
                                    if cond0 == ('S'):
                                        app = input('''qual o aplicativo?
1.Chrome
2.Facebook
3.Instagram
4.Whatsapp
5.Outros
-> ''').upper()
                            except:
                                print('você digitou um caracter invalido. Digite novamente:')
                                continue
                    else:
                        print('você digitou um caracter invalido. Digie novamente.')
                        continue
                else:
                    print('Você não pode retornar os dias.')
                    continue
                NaoRetorno2 += 2
            #Bloco para separar os dias da semana. Dia 3.:
            if dia == 3:
                #Estrurtura para o usuario não retornar o dia 3:
                if NaoRetorno3 != 3:

                    app = input('''qual o aplicativo?
1.Chrome
2.Facebook
3.Instagram
4.Whatsapp
5.Outros
-> ''').upper()
                    # Bloco responsável por guardar os dados dos aplicativos do dia 3:
                    if app == '1' or app == 'CHROME' or app == '2' or app == 'FACEBOOK' or app == '3' or app == 'INSTAGRAM' or app == '4' or app == 'WHATSAPP' or app == '5' or app == 'OUTROS':

                        cond0 = ('S')
                        while not cond0 == ('N'):

                            # Bloco responsável por checar se o usuário não digitou um caracter errado:
                            try:
                                if app == ('CHROME') or app == ('1'):
                                    usodedados = float(input(('quantos bytes usados:')))
                                    dadoschome3 += usodedados
                                    appsusadosdias3 +=1
                                if app == ('FACEBOOK') or app == ('2'):
                                    usodedados = float(input(('quantos bytes usados:')))
                                    dadosfacebook3 += usodedados
                                    appsusadosdias3 += 1
                                if app == ('INSTAGRAM') or app == ('3'):
                                    usodedados = float(input(('quantos bytes usados:')))
                                    dadosinstagram3 += usodedados
                                    appsusadosdias3 += 1
                                if app == ('WHATSAPP') or app == ('4'):
                                    usodedados = float(input(('quantos bytes usados:')))
                                    dadoswhatsapp3 += usodedados
                                    appsusadosdias3 += 1
                                if app == ('OUTROS') or app == ('5'):
                                    usodedados = float(input(('quantos bytes usados:')))
                                    dadosoutros3 += usodedados
                                    appsusadosdias3 += 1
                                cond0 = input('deseja adicionar mais algum aplicativo?[s/n]').upper() # Repetir o loop, caso o usuário digite S
                                if cond0 == ('S'):
                                    app = input('''qual o aplicativo?
1.Chrome
2.Facebook
3.Instagram
4.Whatsapp
5.Outros
-> ''').upper()
                            except:
                                print('você digitou um caracter invalido. Digite novamente:')
                                continue
                    else:
                        print('você digitou um caracter invalido. Digie novamente.')
                        continue
                else:
                    print('Você não pode retornar os dias.')
                    continue
                NaoRetorno3 += 3

            #Bloco para separar os dias da semana. Dia 4:
            if dia == 4:
                #Estrurtura para o usuario não retornar o dia 4:
                if NaoRetorno4 != 4:
                    app = input('''qual o aplicativo?
1.Chrome
2.Facebook
3.Instagram
4.Whatsapp
5.Outros
-> ''').upper()
                    # Bloco responsável por guardar os dados dos aplicativos do dia 5:
                    if app == '1' or app == 'CHROME' or app == '2' or app == 'FACEBOOK' or app == '3' or app == 'INSTAGRAM' or app == '4' or app == 'WHATSAPP' or app == '5' or app == 'OUTROS':

                        cond0 = ('S')
                        while not cond0 == ('N'):

                            # Bloco responsável por checar se o usuário não digitou um caracter errado:
                            try:
                                if app == ('CHROME') or app == ('1'):
                                    usodedados = float(input(('quantos bytes usados:')))
                                    dadoschome4 += usodedados
                                    appsusadosdias4 +=1
                                if app == ('FACEBOOK') or app== ('2'):
                                    usodedados = float(input(('quantos bytes usados:')))
                                    dadosfacebook4 += usodedados
                                    appsusadosdias4 += 1
                                if app == ('INSTAGRAM') or app == ('3'):
                                    usodedados = float(input(('quantos bytes usados:')))
                                    dadosinstagram4 += usodedados
                                    appsusadosdias4 += 1
                                if app == ('WHATSAPP') or app == ('4'):
                                    usodedados = float(input(('quantos bytes usados:')))
                                    dadoswhatsapp4 += usodedados
                                    appsusadosdias4 += 1
                                if app == ('OUTROS') or app == ('5'):
                                    usodedados = float(input(('quantos bytes usados:')))
                                    dadosoutros4 += usodedados
                                    appsusadosdias4 += 1
                                cond0 = input('deseja adicionar mais algum aplicativo?[s/n]').upper() # Repetir o loop, caso o usuário digite S
                                if cond0 == ('S'):
                                    app = input('''qual o aplicativo?
1.Chrome
2.Facebook
3.Instagram
4.Whatsapp
5.Outros
-> ''').upper()
                            except:
                                print('você digitou um caracter invalido. Digite novamente:')
                                continue
                    else:
                        print('você digitou um caracter invalido. Digie novamente.')
                        continue
                else:
                    print('Você não pode retornar os dias.')
                    continue
                NaoRetorno4 += 4

            #Bloco para separar os dias da semana. Dia 5
            if dia == 5:

                #Estrurtura para o usuario não retornar o dia 5:
                if NaoRetorno5 != 5:
                    app = input('''qual o aplicativo?
1.Chrome
2.Facebook
3.Instagram
4.Whatsapp
5.Outros
-> ''').upper()
                    # Bloco responsável por guardar os dados dos aplicativos do dia 5:
                    if app == '1' or app == 'CHROME' or app == '2' or app == 'FACEBOOK' or app == '3' or app == 'INSTAGRAM' or app == '4' or app == 'WHATSAPP' or app == '5' or app == 'OUTROS':

                        cond0 = ('S')
                        while not cond0 == ('N'):

                            # Bloco responsável por checar se o usuário não digitou um caracter errado:
                            try:
                                if app == ('CHROME') or app == ('1'):
                                    usodedados = float(input(('quantos bytes usados:')))
                                    dadoschome5 += usodedados
                                    appsusadosdias5 +=1
                                if app == ('FACEBOOK') or app == ('2'):
                                    usodedados = float(input(('quantos bytes usados:')))
                                    dadosfacebook5 += usodedados
                                    appsusadosdias5 +=1
                                if app == ('INSTAGRAM') or app == ('3'):
                                    usodedados = float(input(('quantos bytes usados:')))
                                    dadosinstagram5 += usodedados
                                    appsusadosdias5 += 1
                                if app == ('WHATSAPP') or app == ('4'):
                                    usodedados = float(input(('quantos bytes usados:')))
                                    dadoswhatsapp5 += usodedados
                                    appsusadosdias5 += 1
                                if app == ('OUTROS') or app == ('5'):
                                    usodedados = float(input(('quantos bytes usados:')))
                                    dadosoutros5 += usodedados
                                    appsusadosdias5 += 1
                                cond0 = input('deseja adicionar mais algum aplicativo?[s/n]').upper() # Repetir o loop, caso o usuário digite S
                                if cond0 == ('S'):
                                    app = input('''qual o aplicativo?
1.Chrome
2.Facebook
3.Instagram
4.Whatsapp
5.Outros
-> ''').upper()
                            except:
                                print('você digitou um caracter invalido. Digite novamente:')
                                continue
                    else:
                        print('você digitou um caracter invalido. Digie novamente.')
                        continue
                else:
                    print('Você não pode retornar os dias.')
                    continue
                NaoRetorno5 += 5

            #Bloco para separar os dias da semana. Dia 6:
            if dia == 6:

                #Estrurtura para o usuario não retornar o dia 6:
                if NaoRetorno6 != 6:
                    app = input('''qual o aplicativo?
1.Chrome
2.Facebook
3.Instagram
4.Whatsapp
5.Outros
-> ''').upper()
                    # Bloco responsável por guardar os dados dos aplicativos do dia 6:
                    if app == '1' or app == 'CHROME' or app == '2' or app == 'FACEBOOK' or app == '3' or app == 'INSTAGRAM' or app == '4' or app == 'WHATSAPP' or app == '5' or app == 'OUTROS':

                        cond0 = ('S')
                        while not cond0 == ('N'):

                            # Bloco responsável por checar se o usuário não digitou um caracter errado:
                            try:
                                if app == ('CHROME') or app == ('1'):
                                    usodedados = float(input(('quantos bytes usados:')))
                                    dadoschome6 += usodedados
                                    appsusadosdias6 +=1
                                if app == ('FACEBOOK') or app == ('2'):
                                    usodedados = float(input(('quantos bytes usados:')))
                                    dadosfacebook6 += usodedados
                                    appsusadosdias6 += 1
                                if app == ('INSTAGRAM') or app == ('3'):
                                    usodedados = float(input(('quantos bytes usados:')))
                                    dadosinstagram6 += usodedados
                                    appsusadosdias6 += 1
                                if app == ('WHATSAPP') or app == ('4'):
                                    usodedados = float(input(('quantos bytes usados:')))
                                    dadoswhatsapp6 += usodedados
                                    appsusadosdias6 += 1
                                if app == ('OUTROS') or app == ('5'):
                                    usodedados = float(input(('quantos bytes usados:')))
                                    dadosoutros6 += usodedados
                                    appsusadosdias6 += 1
                                cond0 = input('deseja adicionar mais algum aplicativo?[s/n]').upper() # Repetir o loop, caso o usuário digite S
                                if cond0 == ('S'):
                                    app = input('''qual o aplicativo?
1.Chrome
2.Facebook
3.Instagram
4.Whatsapp
5.Outros
-> ''').upper()
                            except:
                                print('você digitou um caracter invalido. Digite novamente:')
                                continue
                    else:
                        print('você digitou um caracter invalido. Digie novamente.')
                        continue
                else:
                    print('Você não pode retornar os dias.')
                    continue
                NaoRetorno6 += 6

            #Bloco para separar os dias da semana. Dia 7:
            if dia == 7:

                #Estrurtura para o usuario não retornar o dia 7:
                if NaoRetorno7 != 7:
                    app = input('''qual o aplicativo?
1.Chrome
2.Facebook
3.Instagram
4.Whatsapp
5.Outros
-> ''').upper()
                    # Bloco responsável por guardar os dados dos aplicativos do dia 7:
                    if app == '1' or app == 'CHROME' or app == '2' or app == 'FACEBOOK' or app == '3' or app == 'INSTAGRAM' or app == '4' or app == 'WHATSAPP' or app == '5' or app == 'OUTROS':

                        cond0 = ('S')
                        while not cond0 == ('N'):

                            # Bloco responsável por checar se o usuário não digitou um caracter errado:
                            try:
                                if app == ('CHROME') or app == ('1'):
                                    usodedados = float(input(('quantos bytes usados:')))
                                    dadoschome7 += usodedados
                                    appsusadosdias7 +=1
                                if app == ('FACEBOOK') or app == ('2'):
                                    usodedados = float(input(('quantos bytes usados:')))
                                    dadosfacebook7 += usodedados
                                    appsusadosdias7 += 1
                                if app == ('INSTAGRAM') or app == ('3'):
                                    usodedados = float(input(('quantos bytes usados:')))
                                    dadosinstagram7 += usodedados
                                    appsusadosdias7 += 1
                                if app == ('WHATSAPP') or app == ('4'):
                                    usodedados = float(input(('quantos bytes usados:')))
                                    dadoswhatsapp7 += usodedados
                                    appsusadosdias7 += 1
                                if app == ('OUTROS') or app == ('5'):
                                    usodedados = float(input(('quantos bytes usados:')))
                                    dadosoutros7 += usodedados
                                    appsusadosdias7 += 1
                                cond0 = input('deseja aidcionar mais algum aplicativo?[s/n]').upper() # Repetir o loop, caso o usuário digite S
                                if cond0 == ('S'):
                                    app = input('''qual o aplicativo?
1.Chrome
2.Facebook
3.Instagram
4.Whatsapp
5.Outros
-> ''').upper()
                            except:
                                print('você digitou um caracter invalido. Digite novamente:')
                                continue
                    else:
                        print('você digitou um caracter invalido. Digie novamente.')
                        continue
                else:
                    print('Você não pode retornar os dias.')
                    continue
                NaoRetorno7 += 7
            contadora_dias += 1
        else:
            print('Você digitou um dia invalido. Digite novamente:')
            continue
        if contadora_dias < 7:
            cond1 = input('deseja adicionar mais um dia?[s/n]').upper()
            if cond1 == ('N'):
                break
    except:
        print('Você digitou um caracter invalido. digite novamente:')
        continue

#tratamento dos dados:

#Bloco que calcula o total de dados usados por cada aplicativo ao longo da semana:

totalchrome = (dadoschome1+dadoschome2+dadoschome3+dadoschome4+dadoschome5+dadoschome6+dadoschome7)

totalfacebook = (dadosfacebook1+dadosfacebook2+dadosfacebook3+dadosfacebook4+dadosfacebook5+dadosfacebook6+dadosfacebook7)

totalinstagram = (dadosinstagram1+dadosinstagram2+dadosinstagram3+dadosinstagram4+dadosinstagram5+dadosinstagram6+dadosfacebook7)

totalwhatsapp = (dadoswhatsapp1+dadoswhatsapp2+dadoswhatsapp3+dadoswhatsapp4+dadoswhatsapp5+dadoswhatsapp6+dadoswhatsapp7)

totaloutros = (dadosoutros1 + dadosoutros2 + dadosoutros3 + dadosoutros4 + dadosoutros5 + dadosoutros6 + dadosoutros7)

#Bloco que calcula o total de dados usados por todos os aplicativos por dia:

totaldia1 = (dadoschome1+dadosfacebook1+dadosinstagram1+dadoswhatsapp1+dadosoutros1)

totaldia2 = dadoschome2+dadosfacebook2+dadosinstagram2+dadoswhatsapp2+dadosoutros2

totaldia3 = (dadoschome3+dadosfacebook3+dadosinstagram3+dadoswhatsapp3+dadosoutros3)

totaldia4 = (dadoschome4+dadosfacebook4+dadosinstagram4+dadoswhatsapp4+dadosoutros4)

totaldia5 = (dadoschome5+dadosfacebook5+dadosinstagram5+dadoswhatsapp5+dadosoutros5)

totaldia6 = (dadoschome6+dadosfacebook6+dadosinstagram6+dadoswhatsapp6+dadosoutros6)

totaldia7 = (dadoschome7+dadosfacebook7+dadosinstagram7+dadoswhatsapp7+dadosoutros7)

#Variável que calcula o total de dados utilizados por todos os aplicativos:

totalsemana = (totaldia1 + totaldia2 + totaldia3 + totaldia4 + totaldia5 + totaldia6 + totaldia7)


SomaDia1 = (dadoschome1 + dadosfacebook1 + dadosinstagram1 + dadoswhatsapp1)
SomaDia2 = (dadoschome2 + dadosfacebook2 + dadosinstagram2 + dadoswhatsapp2)
SomaDia3 = (dadoschome3 + dadosfacebook3 + dadosinstagram3 + dadoswhatsapp3)
SomaDia4 = (dadoschome4 + dadosfacebook4 + dadosinstagram4 + dadoswhatsapp4)
SomaDia5 = (dadoschome5 + dadosfacebook5 + dadosinstagram5 + dadoswhatsapp5)
SomaDia6 = (dadoschome6 + dadosfacebook6 + dadosinstagram6 + dadoswhatsapp6)
SomaDia7 = (dadoschome7 + dadosfacebook7 + dadosinstagram7 + dadoswhatsapp7)

#calcula a média total com os dados de todos os aplicativos:
MediaTotal = (totalchrome + totalfacebook + totalinstagram + totalwhatsapp + totaloutros) / (contadora_dias - 1)

#calcula a média dos dias de uso de cada aplicativos:

media_semana_chome = (totalchrome / (contadora_dias - 1))
media_semana_facebook = (totalfacebook / (contadora_dias - 1))
media_semana_instagram = (totalinstagram / (contadora_dias - 1))
media_semana_whatsapp = (totalwhatsapp / (contadora_dias - 1))
media_semana_outros = (totaloutros / (contadora_dias - 1))
#saída de dados

if contadora_dias > 7:
    print('Você chegou ao final da semana')

#Loop para ver os dados separadamente:

while not cond3 == ('N'):
    VerDados = input('''Quais dados gostaria de ver:
1.total de dados utilizados por cada aplicativo por dia.
2.total de dados utilizados por cada aplicativo na semana.
3.total de dados totais utilizados em cada dia.
4.total de dados totais utilizados na semana.
5.Média diária de consumo total de dados.
6.Média diária de consumo de dados de cada aplicativo.
-> ''')
    if VerDados == ('1'):
        print('''total de dados utilizados por cada aplicativo por dia:

DIA1   CHROME: {:.2f}   FACEBOOK: {:.2f}  INSTAGRAM:  {:.2f}  WHATSAPP: {:.2f}  OUTROS: {:.2f}

DIA2   CHROME: {:.2f}  FACEBOOK: {:.2f}   INSTAGRAM: {:.2f}   WHATSAPP: {:.2f}  OUTROS: {:.2f}

DIA3   CHROME: {:.2f}  FACEBOOK: {:.2f}   INSTAGRAM: {:.2f}   WHATSAPP: {:.2f}  OUTROS: {:.2f}

DIA4   CHROME: {:.2f}  FACEBOOK: {:.2f}   INSTAGRAM: {:.2f}   WHATSAPP: {:.2f}  OUTROS: {:.2f}

DIA5   CHROME: {:.2f}  FACEBOOK: {:.2f}   INSTAGRAM: {:.2f}   WHATSAPP: {:.2f}  OUTROS: {:.2f}

DIA6   CHROME: {:.2f}  FACEBOOK: {:.2f}   INSTAGRAM: {:.2f}   WHATSAPP: {:.2f}  OUTROS: {:.2f}

DIA7   CHROME: {:.2f}  FACEBOOK: {:.2f}   INSTAGRAM: {:.2f}   WHATSAPP: {:.2f}  OUTROS: {:.2f}'''.format(dadoschome1, dadosfacebook1, dadosinstagram1, dadoswhatsapp1, dadosoutros1, dadoschome2, dadosfacebook2, dadosinstagram2, dadoswhatsapp2, dadosoutros2, dadoschome3, dadosfacebook3 ,dadosinstagram3, dadoswhatsapp3, dadosoutros3, dadoschome4, dadosfacebook4, dadosinstagram4, dadoswhatsapp4, dadosoutros4, dadoschome5, dadosfacebook5, dadosinstagram5, dadoswhatsapp5, dadosoutros5, dadoschome6, dadosfacebook6, dadosinstagram6, dadoswhatsapp6, dadosoutros6, dadoschome7, dadosfacebook7, dadosinstagram7, dadoswhatsapp7, dadosoutros7 ))
    if VerDados == ('2'):
        print('''total de dados utilizados por cada aplicativo na semana:

CHROME: {:.2f}   FACEBOOK: {:.2f}  INSTAGRAM:  {:.2f}  WHATSAPP: {:.2f} OUTROS: {:.2f}
'''.format(totalchrome, totalfacebook, totalinstagram, totalwhatsapp, totaloutros))
    if VerDados == ('3'):
        print('''total de dados totais utilizados em cada dia:

DIA1: {:.2f}

DIA2: {:.2f}

DIA3: {:.2f}

DIA4: {:.2f}

DIA5: {:.2f}

DIA6  {:.2f}

DIA7: {:.2f}'''.format(totaldia1, totaldia2, totaldia3, totaldia4, totaldia5, totaldia6, totaldia7))

    if VerDados == ('4'):
        print('total de dados totais utilizados na semana: {:.2f} bytes'.format(totalsemana))
    if VerDados == ('5'):
        print('Média diária de consumo total de dados: {:.2f}'.format(MediaTotal))
    if VerDados == ('6'):
        print('''Média diária de consumo de dados de cada aplicativo:

CHROME: {:.2f}

FACEBOOK: {:.2f}

INSTAGRAM: {:.2f}

WHATSAPP: {:.2f}

OUTROS: {:.2f}'''.format(media_semana_chome, media_semana_facebook, media_semana_instagram, media_semana_whatsapp, media_semana_outros))
    cond3 = input('Deseja ver outro dado?[S/N] ').upper() # Repetir o loop, caso o usuário digite S


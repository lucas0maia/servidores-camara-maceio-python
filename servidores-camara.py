import requests
from bs4 import BeautifulSoup
import pandas

urldapagina1 = "http://camarademaceio.al.gov.br/transparencia/folha-pagamento/" #AQUI ACESSA A PAGINA
urldapagina2 = 1
urldapagina3 = "?nome=Seu+Nome&cpf=seucepf" #altere inserindo seu nome e seu cpf sem pontuação e sem espaços

print('Feita análise da página:')   
planilhadosservidores = [] #Lista de dicionários contendo... ("servidor":"nome","Matricula":"numerodematricula","")
while urldapagina2 < 5: #A última página é a 5027 - colocar 5028 para dados completos

    pagina = requests.get(urldapagina1 + str(urldapagina2) + urldapagina3) #CAPTURA A PAGINA
    pagina = BeautifulSoup(pagina.content, 'html.parser') #transforma a pagina em algo legível
       
    tabeladoservidor = pagina.find_all("td") #tabeladoservidor é uma lista com tudo na página dentro de 'td'
    nome = tabeladoservidor[3].text #O .text retira todos os espaços e tags deixando só o necessário
    matricula = tabeladoservidor[1].text
    cargo = tabeladoservidor[5].text
    remuneracao = float((tabeladoservidor[9].text.strip('R$ ')).replace('.','').replace(',','.')) #Retirei o simbolo de R$ e adequei a pontuação para um float
    abono = float((tabeladoservidor[11].text.strip('R$ ')).replace('.','').replace(',','.'))
    eventuais = float((tabeladoservidor[13].text.strip('R$ ')).replace('.','').replace(',','.'))
    descontos = float((tabeladoservidor[15].text.strip('R$ ')).replace('.','').replace(',','.'))
    salario = float((tabeladoservidor[17].text.strip('R$ ')).replace('.','').replace(',','.'))
    mesreferencia = (tabeladoservidor[7]).text.split('/')[0]
    anodereferencia = (tabeladoservidor[7]).text.split('/')[1]
    dicionariodoservidor = {"Servidor":nome, "Matrícula":matricula, "Cargo":cargo, "Remuneração":remuneracao, "Abono":abono, "Eventuais":eventuais, "Descontos":descontos, "Salario":salario,"MesRef":mesreferencia, "AnoRef":anodereferencia}
    planilhadosservidores.append(dicionariodoservidor)
    print(urldapagina2, end=" ") #Informa a página que está sendo analisada
    urldapagina2 += 1
dadosservidores = pandas.DataFrame(planilhadosservidores)
dadosservidores = dadosservidores[['Servidor', 'Matrícula', 'Cargo','Remuneração','Abono','Eventuais','Descontos','Salario','MesRef','AnoRef']] #Apenas organizando as colunas, que por padrão são postas em ordem alfabética
dadosservidores.sort_values(by="Salario",ascending=False)
dadosservidores.to_csv("listagemdosservidores.csv", encoding="utf-8")

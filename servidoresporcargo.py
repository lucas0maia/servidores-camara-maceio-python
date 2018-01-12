#Trata alguns dados do csv construído para gerar informações relevantes 

import pandas

mes = "Novembro"
ano = 2017
listagemservidores = pandas.read_csv("listagemdosservidores.csv")
listagemservidores = listagemservidores[listagemservidores.MesRef == mes]
listagemservidores = listagemservidores[listagemservidores.AnoRef == ano]
#listagemservidores = listagemservidores[listagemservidores.Cargo == 'VEREADOR'] ###DESMARQUE CASO QUEIRA SELECIONAR APENAS UM CARGO

servidoresporcargo = listagemservidores.Cargo.value_counts()
mediasalarial = listagemservidores.groupby('Cargo')['Salario'].mean()
print(f"O total de servidores na folha de pagamento em {mes} de {ano} é de {servidoresporcargo.sum()} pessoas")
print(f"O total de cargos nesse mesmo mês é de {servidoresporcargo.count()}")
custodafolha = listagemservidores.Salario.get_values().sum()
custodafolha = ("%.2f" % custodafolha)
print(f"O custo da folha de pagamento foi de R${custodafolha}")
print("\nCARGO ------------------------------------------------ NÚMERO DE SERVIDORES")
print(servidoresporcargo)
print("\n CARGO ------------------------------------------------ MEDIA SALARIAL") #NA PRÓXIMA VERSÃO COLOCAR AS INFORMAÇÕES NA MESMA LINHA
print(mediasalarial)

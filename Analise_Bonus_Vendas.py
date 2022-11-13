import pandas as pd
from twilio.rest import Client
# Your Account SID from twilio.com/console
account_sid = "AC60c29ad6fccfd4aada546ce76d0f0b16"
# Your Auth Token from twilio.com/console
auth_token = "0cb6343261c68132ca3a2dfb2e5e02c5"
client = Client(account_sid, auth_token)






lista_meses = ['janeiro','fevereiro','março','abril','maio','junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx') # O"f" e para editar o texto de maneira dinamica
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000,'Vendedor'].values[0]  #O .loc retorna o resultado em tabela, colocamos o .values[0] no final para transformar isso em valor
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000,'Vendas'].values[0]

        message = client.messages.create(
            to="+5511941865651",
            from_="+16075363282",
            body=f' No mes de {mes} o vendedor(a) {vendedor} atingiu vendas com um valor de {vendas} Parabens!')

        print(message.sid)









# INSTRUCOES PARA CONSTRUCAO DO PROJETO
# IMPORTAR OS ARQUIVOS E ABRIR DENTRO DO PYCHARM
# VERIFICAR SE EXISTEM VENDES MAIORES QUE 55.00 E ENVIAR UM SMS, COM NOME, VENDAS E MES

#RECURSOS NECESSARIOS
#PIP INSTALL PANDAS
#PIP INSTALL OPENPYXL
#PIP INSTALL TWILIO

# ACABEI INSTALANDO O WHEEL

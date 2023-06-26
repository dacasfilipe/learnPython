from datetime import datetime

print(datetime.now())
print(datetime.now().day)
print(datetime.now().month)
print(datetime.now().year)
print(datetime.now().hour)

#criar uma data
lancamento_app = datetime(2023,5,28)
print(lancamento_app)
#quero receber uma data
data_lancamento = datetime.strptime(input('Quando devemos lançar o aplicativo?'),'%d/%m/%Y')
print(type(data_lancamento))

#calcular o intervalo entre uma data e outra
data_atual = datetime.now()
prazo = data_lancamento - data_atual
print(prazo.days)

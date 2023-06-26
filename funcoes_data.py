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
data_lancamento = input('Quando devemos lançar o aplicativo?')
print(data_lancamento)

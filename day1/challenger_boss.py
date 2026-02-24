from functools import reduce

transacoes = [150.0, -50.0, 300.0, -20.0, 45.0, -100.0]

depositos = filter(lambda n: n > 0 ,transacoes)

total_deposito = reduce(lambda x,y: x+y,depositos)
print(f"Deposito total: {total_deposito}")
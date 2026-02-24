idade = input("Digite sua idade")
try:
    int_idade = int(idade)
    print(f"Idade: {int_idade}")
except ValueError as e:
    print(f"Erro ao converter número: {e}")
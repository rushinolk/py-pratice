import json

produtos = ["Pistola 9mm", "Erva Mista", "Escopeta", "Faca de Combate", "Lança-Foguetes"]
valores = [250, 80, 600, 45, 10000]

loja_completa = {item: preco for item, preco in zip(produtos,valores)}

vitrine_barato = {item: preco for item, preco in loja_completa.items() if preco < 300}

print(loja_completa)

print(vitrine_barato)

try:
    with open("day5\\backup_loja.json","w",encoding="utf-8") as file:
        json.dump(loja_completa,file,indent=4,ensure_ascii=False)
    print("Backup realizado com sucesso")
except FileNotFoundError as e:
    print(f"Falha ao realizar Backup: {e}")

import json
import re


try:
    with open("day5\\recompensa.json","r",encoding="utf-8") as file:
        source_json = json.load(file)
except FileNotFoundError as e:
    print(f"Arquivo não encontrado: {e}")

try:
    with open("day5\\relatorio_sujo.txt","r",encoding="utf-8") as file:
        source_txt = file.read()
except FileNotFoundError as e:
    print(f"Arquivo não encontrado: {e}")

#print(source_txt)
#print(source_json)
#texto_clean = source_txt.strip().split(".")
#print(texto_clean)

aventureiros = re.findall(r"Aventureiro:\s(\w+)",source_txt)
aventureiros_set = set(aventureiros)

recompensa_com_imposto = {monster: price*0.8 for monster, price in source_json.items()}

def calcular_pagamento(monstros_abatidos,source):
    monstros_validos = list(filter(lambda m: m in source,monstros_abatidos))
    valores = [source[m] for m in monstros_validos]
    pagamento_total = sum(valores)

    return monstros_validos, pagamento_total


meus_abates = ["Slime", "Pedra", "Dragao", "Troll", "Erro_de_Rede", "Orc", "Lixo_do_Sistema"]

abates_limpos, gold = calcular_pagamento(meus_abates,recompensa_com_imposto)

print(f"Aventureiros do dia: {aventureiros_set}")
print(f"Monstros unicos abatidos: {abates_limpos}")
print(f"Pagamento total recebido (descontado impostos da guilda): {gold}")
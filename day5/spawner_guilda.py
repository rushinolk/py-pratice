import json

# 1. Dicionário para virar JSON
catalogo_recompensas = {
    "Slime": 10,
    "Orc": 50,
    "Dragao": 500,
    "Troll": 150,
    "Lobo": 25,
    "Goblin": 15
}

try:
    with open ("day5\\recompensa.json","w",encoding="utf-8") as file:
        json.dump(catalogo_recompensas,file,indent=4,ensure_ascii=False)
    print("Arquivo JSON salvo com sucesso")
except FileNotFoundError as e:
    print(f"Pasta não encontrada para salvar arquivo: {e}")



# 2. Texto corrompido para virar TXT
log_corrompido = """
[SISTEMA INICIADO].
Erro de leitura de pacotes... 0x88A.
[LOG] Aventureiro: Arthur abateu Slime.
[WARN] Aventureiro: Leon abateu Orc.
Rede instável... reconectando.
[LOG] Aventureiro: Arthur abateu Dragao.
[ERROR] Aventureiro: Claire abateu Troll.
Lixo de rede: x889912.
[LOG] Aventureiro: Leon abateu Lobo.
[LOG] Aventureiro: Arthur abateu Goblin.
[SISTEMA OFFLINE]
"""
try:
    with open("day5\\relatorio_sujo.txt","w",encoding="utf-8") as file:
        file.writelines(log_corrompido)
        print("Arquivo de texto salvo com sucesso")
except FileNotFoundError as e:
    print(f"Pasta não encontrada para salvar arquivo: {e}")

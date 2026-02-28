import json

banco_rh = {
    "9910": "Nivel Azul",
    "8820": "Nivel Vermelho",
    "7730": "Nivel Azul",
    "6640": "Nivel Vermelho",
    "5550": "Nivel Verde",
    "4460": "Nivel Vermelho"
}

try:
    with open("day6\\banco_rh.json","w",encoding="utf-8") as file:
        json.dump(banco_rh,file,indent=4,ensure_ascii=False)
    print("Arquivo JSON criado com sucesso")
except FileNotFoundError as e:
    print(f"Pasta do arquivo não encontrado: {e}")


log_radio = """
[ESTATICA]... Socorro! Setor Oeste comprometido.
Oficial abatido. Distintivo: 8820. Requer evacuação!
[RUIDO]... Criaturas no saguão...
Múltiplas baixas. Distintivo: 7730 sem sinal.
[ESTATICA]... Porta principal trancada... Distintivo: 6640 não responde.
Aviso de falha no sistema elétrico.
[RUIDO]... Fuga pela garagem falhou... Distintivo: 9910. Infecção confirmada.
"""

try:
    with open("day6\\transmissoes.txt","w",encoding="utf-8") as file:
        file.writelines(log_radio)
    print("Arquivo TXT criado com sucesso")
except FileNotFoundError as e:
    print(f"Pasta do arquivo não encontrado: {e}")
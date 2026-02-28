import json
import re


path_json = "day6\\banco_rh.json"
path_txt = "day6\\transmissoes.txt"
path_protocolo = "day6\\protocolo_vermelho.json"


try:
    with open(path_json,"r",encoding="utf-8") as file:
        source_json = json.load(file)
    print("JSON lido com sucesso")
except FileNotFoundError as e:
    print(f"Arquivo não encontrado: {e}")


try:
    with open(path_txt,"r",encoding="utf-8") as file:
        source_txt = file.read()
        print("TXT lido com sucesso")
except FileNotFoundError as e:
    print(f"Arquivo não encontrado: {e}")

distintivos = re.findall(r"\d+",source_txt)

print(distintivos)

alvos_quarentena = {distintivo: nivel for distintivo, nivel in source_json.items() if distintivo in distintivos and nivel == "Nivel Vermelho"}

print(alvos_quarentena)


try:
    with open(path_protocolo,"w",encoding="utf-8") as file:
        json.dump(alvos_quarentena,file,indent= 4)
    print("Relatorio salvo com sucesso")
except FileNotFoundError as e:
    print(f"Erro ao encontrar pasta para salvar: {e}")
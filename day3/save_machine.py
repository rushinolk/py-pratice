inventario = "Itens: Pistola, Erva verde, chave de espadas"

path = "E:\\main_folder\\Tech\\Projetos\\pypratice\\day3"
source_name = "\\save_game.txt"


with open(f"{path}{source_name}", "w",encoding="utf-8") as file:
    file.write(inventario)
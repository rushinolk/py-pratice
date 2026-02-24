name = input("Digite o nome do arquivo: ")
path = "E:\\main_folder\\Tech\\Projetos\\pypratice\\day3"
full_path = f"{path}\\{name}.txt"

try:
    with open(full_path,'r',encoding="utf-8") as file:
        rows = file.readlines()
        first_row = rows[0]
        clear_first = first_row.strip()
        split_first = clear_first.split(",")
        full_first = "".join(split_first)
        if any(f.isdigit() for f in full_first):
            print(f"Senha validada com sucesso {full_first}")
        else:
            print("Acesso Negado: A senha não possui números")

except FileNotFoundError as e:
    print(f"Arquivo não encontrado \nErro: {e}")



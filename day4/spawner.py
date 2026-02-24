import random

def gerar_missao_diaria():
    print("Iniciando a seleção das missões do dia")

    missoes = [
        "Ler por 30 minutos",
        "Limpar o quintal", 
        "Estudar Python",
        "Escrever roteiro",
        "Correr 5km"
    ]

    missoes_sorteadas = random.sample(missoes,3)
    xps = [random.randint(30,150) for m in missoes_sorteadas]
    

    missoes_reward = zip(missoes_sorteadas,xps)

    missoes_final = [ (f"Missão: {missao} | XP: {xp}\n") for missao,xp in missoes_reward ]

    path = "E:\\main_folder\\Tech\\Projetos\\pypratice\\day4\\"
    source = f"{path}sync_data.txt"

    try:
        with open(source,"w",encoding="utf-8") as file:
            file.writelines(missoes_final)
        print("Arquivo sync criado com sucesso")
    except Exception as e:
        print(f"Erro ao criar arquivo: {e}")

if __name__ == "__main__":
    gerar_missao_diaria()
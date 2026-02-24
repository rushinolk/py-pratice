from functools import reduce

def processar_missoes_do_dia():
    print("Iniciando a Engine do sistema...")
    path = "E:\\main_folder\\Tech\\Projetos\\pypratice\\day4\\sync_data.txt"

    try:
        with open(path,"r",encoding="utf-8") as file:
            rows = file.readlines()
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado")
        return
    
    missao = []
    xp = []


    for row in rows:
        row = row.strip().split("|")
        quest = row[0].replace("Missão: ","")
        missao.append(quest)
        drop = int(row[1].replace("XP: ",""))
        xp.append(drop)

    bonus_xp = list(map(lambda n: n*1.2,xp))
    xp_total = reduce(lambda x,y: x+y,bonus_xp)


    print("\n--- RELATÓRIO DO DIA ---")
    print(f"Missões concluidas: {missao}\nXP total: {round(xp_total,2)}")
    if any("Python" in c for c in missao):
        print("Missão epica do dia")
    
if __name__ == "__main__":

    processar_missoes_do_dia()

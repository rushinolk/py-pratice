

def derreter_item(itens, taxa_ferreiro=10,):
    unique_itens = set(itens)
    custo_total = len(unique_itens) * taxa_ferreiro

    return unique_itens,custo_total


if __name__ == "__main__":
    inventario_do_jogador = ["Faca", "Faca", "Pistola", "Erva", "Erva", "Lixo", "Sucata", "Lixo"]

    inventario_clean = filter(lambda n: n != "Lixo",inventario_do_jogador)

    itens,price = derreter_item(inventario_clean)
    print(f"Itens forjados: {itens} | Custo total: {price} moedas")
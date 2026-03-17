import asyncio
import time


async def consultar_db(nome:str, segundos:int):
    print("[DG] Iniciando consulta no db")
    await asyncio.sleep(segundos)
    return f"Usuario: {nome} conectado"



if __name__ == "__main__":
    sincro = asyncio.run(consultar_db("Arthur", 3))
    print(sincro)
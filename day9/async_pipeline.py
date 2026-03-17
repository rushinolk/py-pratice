import asyncio
import time
import random
from functools import reduce

async def extrair_dados(arquivo_id:int):
    await asyncio.sleep(random.uniform(1,3))
    return random.randint(10,100)

async def pipeline_extract():
    start = time.perf_counter()

    print("Iniciando extração de dados...")

    resultados = await asyncio.gather(
        extrair_dados(1),
        extrair_dados(2),
        extrair_dados(3),
        extrair_dados(4),
        extrair_dados(5),
        return_exceptions=True
    )

    async with asyncio.TaskGroup as tg:
        task1 = tg.create_task(extrair_dados(1))
        task2 = tg.create_task(extrair_dados(2))
        task3 = tg.create_task(extrair_dados(3))
        task4 = tg.create_task(extrair_dados(4))
        task5 = tg.create_task(extrair_dados(5))
    resultados_task = [task1.result(),task2.result(),task3.result(),task4.result(),task5.result()]

    soma_total = reduce(lambda x,y: x+y,resultados)
    media = soma_total / len(resultados)

    end = time.perf_counter()

    print(f"Soma total dos dados extraidos: {soma_total}")
    print(f"Media dos dados extraidos: {media}")
    print(f"Tempo total da extração: {end - start:.2f}s")

if __name__ == "__main__":

    asyncio.run(pipeline_extract())

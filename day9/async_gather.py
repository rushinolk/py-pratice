import asyncio
import time


async def download_sensor(sensor_id:int, tempo:int):
    await asyncio.sleep(tempo)
    return {
        "sensor":sensor_id,
        "status":"online"
    }


async def iniciar_download():
    start = time.perf_counter()

    print("Conferindo sensores")

    resultados = await asyncio.gather(
        download_sensor(1,3),
        download_sensor(2,1),
        download_sensor(3,2)
    )

    end = time.perf_counter()

    print(f"Downlaod dos sensores concluido! Status {resultados}")

    print(f"Tempo de resposta do download {end - start:.2f}s")


if __name__ == "__main__":
    asyncio.run(iniciar_download())

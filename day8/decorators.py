import functools


raw_data = [
    {"id": 50, "valor": 100.0},    # Deve ser barrado pelo decorador (< 100)
    {"id": 101, "valor": 250.0},   # OK
    {"id": 101, "valor": 250.0},   # Duplicado (Deve ser removido na função)
    {"id": 102, "valor": None},    # Valor None (Deve ser removido na função)
    {"id": 103, "valor": 500.0},   # OK
]

def data_validator(min_id_value=100):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):

            resultado = func(*args,**kwargs)
            resultado_limpo = [item for item in resultado if item.get("id") is not None and item.get("id")>=min_id_value]

            return resultado_limpo
        return wrapper
    return decorator     

@data_validator()
def clean_pipeline(raw_data):
    data_tuple = [tuple(d.items()) for d in raw_data if d.get("valor") is not  None]
    data_set = [dict (d) for d in set(data_tuple)]
    return data_set

final_data = clean_pipeline(raw_data)
print(f"Dados finais: {final_data}")

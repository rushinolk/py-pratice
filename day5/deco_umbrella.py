import re


log_corrompido = """
Iniciando teste...
Setor G: Falha no isolamento. 
ID de contenção recuperado: 884920. 
Dano estrutural: 75%.
Tentativas de bloqueio manual: 3 falhas.
Código mestre de override: 9920114.
"""


dados = re.findall(r"\d+",log_corrompido)
dados_int = [int(dado) for dado in dados]

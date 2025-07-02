# 14/process.py
import time
import sys

print("Iniciando o processamento de dados...")
# Simula um processamento
time.sleep(2)
print("Dados processados com sucesso!")

# Exemplo de dependência (pandas não é estritamente necessário para este print,
# mas se a regra pedir uma dependência de exemplo, podemos simulá-la aqui).
try:
    import pandas as pd
    print("Biblioteca pandas disponível e importada.")
except ImportError:
    print("Pandas não está disponível, continuando sem ele.")

print("Processamento concluído.")
sys.exit(0) # Indica saída bem-sucedida
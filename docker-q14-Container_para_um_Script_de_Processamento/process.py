# 14/process.py
import time
import sys

print("Inicializando o processamento de dados...")
# Simula um processamento
time.sleep(2)
print("Dados processado!")


try:
    import pandas as pd
    print("Biblioteca pandas disponível e importada.")
except ImportError:
    print("Pandas não está disponível, continuando sem ele.")

print("Processamento concluído.")
sys.exit(0) # Indica saída bem-sucedida
import pandas as pd
from pathlib import Path

def carregar_dados_(caminho_arquivo: str) -> pd.DataFrame:
    df_carteira_cliente_ing = pd.read_csv(caminho_arquivo)
    # Salvar na bronze
    return df_carteira_cliente_ing
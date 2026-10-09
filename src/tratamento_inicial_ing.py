import pandas as pd
import numpy as np

def traduzir_colunas_df(dataframe_bruto: pd.DataFrame) -> pd.DataFrame:
    df_carteira_cliente_traduzido = dataframe_bruto.copy()
    df_carteira_cliente_traduzido = df_carteira_cliente_traduzido.rename(columns={
        'customerID': "id_cliente", 
        'gender': "genero", 
        'SeniorCitizen': "idoso", 
        'Partner': "possui_parceiro", 
        'Dependents': "possui_dependentes",
        'tenure': " tempo_de_contrato", 
        'PhoneService': "servico_telefonico", 
        'MultipleLines': "multiplas_linhas", 
        'InternetService': "servico_de_internet",
        'OnlineSecurity': "seguraca_online", 
        'OnlineBackup': "backup_online", 
        'DeviceProtection': "protecao_de_dispositivos", 
        'TechSupport': "suporte_tecnico",
        'StreamingTV': "streaming_de_tv", 
        'StreamingMovies': "streaming_de_filmes", 
        'Contract': "tipo_de_contrato", 
        'PaperlessBilling': "faturamento_digital",
        'PaymentMethod': "metodo_pagamento", 
        'MonthlyCharges': "cobranca_mensal", 
        'TotalCharges': "cobranca_total", 
        'Churn': "cancelou_contrato",
        'CustomerFeedback': "feedback_cliente", 
        'MonthlyIncome': "renda_mensal"
    }) 

    return df_carteira_cliente_traduzido
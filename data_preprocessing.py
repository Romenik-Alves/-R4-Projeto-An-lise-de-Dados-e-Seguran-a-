import pandas as pd

def load_data(filepath):
    data = pd.read_csv(filepath)
    data['data'] = pd.to_datetime(data['data'])  # Convertendo a coluna de data
    return data

def preprocess_data(data):
    # Remover linhas com dados faltantes
    data.dropna(inplace=True)
    return data
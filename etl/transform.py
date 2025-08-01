
'''
Autor: Thiago Vilarinho Lemes
Data: 2024-01-15
Descrição: Funções utilitárias para realizar transformações em DataFrames.
'''
import pandas as pd

def transformar_dados(df, colunas_remover=None, renomear_colunas=None, drop_na=False):
    '''
    Função para transformar um DataFrame do Pandas.
    Args:
        df (pd.DataFrame): DataFrame a ser transformado.
        colunas_remover (list, opcional): Lista de colunas a serem removidas do DataFrame.
        renomear_colunas (dict, opcional): Dicionário para renomear colunas no formato {'coluna_antiga': 'coluna_nova'}.
        drop_na (bool, opcional): Se True, remove linhas com valores NaN.

    Returns:
        pd.DataFrame: DataFrame transformado.
    '''
    if colunas_remover:
        df = df.drop(columns=colunas_remover, errors='ignore')
    if renomear_colunas:
        df = df.rename(columns=renomear_colunas)
    if drop_na:
        df = df.dropna()
    return df

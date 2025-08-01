'''
Autor: Thiago Vilarinho Lemes
Data: 2024-01-15
Descrição: Funções utilitárias para carregar tipos de arquivos suportados.
'''
import pandas as pd
import streamlit as st


def loading_type_files(nome, arquivo):
    """
    Função para carregar os tipos de arquivos suportados.
    Retorna um dicionário com as extensões e seus respectivos tipos.

    Args:
        nome (str): Nome do arquivo.
        arquivo (file-like object): Objeto de arquivo carregado pelo Streamlit.
    """
    if nome.endswith('.csv'):
        df = pd.read_csv(arquivo)
    elif nome.endswith('.xlsx'):
        df = pd.read_excel(arquivo)
    elif nome.endswith('.json'):
        df = pd.read_json(arquivo)
    elif nome.endswith('.parquet'):
        df = pd.read_parquet(arquivo)
    
    return df
    

def return_type_files(nome):
    """
    Retorna um dicionário com os tipos de arquivos suportados.

    Args:
        nome (str): Nome do arquivo.
    """

    if nome.endswith('.csv'):
        return '.csv'
    elif nome.endswith('.xlsx'):
        return '.xlsx'
    elif nome.endswith('.json'):
        return '.json'
    elif nome.endswith('.parquet'):
        return '.parquet'
    
    
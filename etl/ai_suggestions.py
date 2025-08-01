'''
Autor: Thiago Vilarinho Lemes
Data: 2024-01-15
Descrição: Funções utilitárias para sugerir transformações em DataFrames.
'''
import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

def sugerir_transformacao_local(df, temperatura=0.7, max_tokens=3000):
    '''    
    Sugere transformações de limpeza e padronização para um DataFrame usando um modelo IA local.
    Args:
        df: DataFrame do pandas a ser analisado
        temperatura: temperatura para a geração de texto (padrão: 0.7)
        max_tokens: número máximo de tokens a serem gerados (padrão: 3000)

    Returns:
        Uma string com as sugestões de transformação
    '''

    colunas = list(df.columns)
    tipos = df.dtypes.astype(str).to_dict()

    prompt = f"""
    Você é um assistente de engenharia de dados.
    As colunas do dataframe são: {colunas}
    Os tipos de dados são: {tipos}

    Sugira transformações de limpeza e padronização para este dataset.
    Retorne apenas uma lista com instruções simples e outra lista com os comandos correspondentes.
    """

    payload = {
        "model": "local-model",  # você pode deixar assim ou colocar um nome como 'mistral' apenas para identificar
        "prompt": prompt,
        "max_tokens": max_tokens,
        "temperature": temperatura
    }

    try:
        response = requests.post(
            "http://localhost:1234/v1/completions",
            headers={"Content-Type": "application/json"},
            data=json.dumps(payload)
        )

        if response.status_code == 200:
            resultado = response.json()
            return resultado['choices'][0]['text'].strip()
        else:
            return f"Erro: {response.status_code} - {response.text}"
    except Exception as e:
        return f"Erro de conexão: {e}"




def sugerir_transformacao_hf(df):
    '''    
    Sugere transformações de limpeza e padronização para um DataFrame usando um modelo da Hugging Face.
    Args:
        df: DataFrame do pandas a ser analisado
    Returns:
        Uma string com as sugestões de transformação
    '''
    colunas = list(df.columns)
    tipos = df.dtypes.astype(str).to_dict()
    prompt = f"""
    Você é um assistente de engenharia de dados.
    As colunas do dataframe são: {colunas}
    Os tipos de dados são: {tipos}

    Sugira transformações de limpeza e padronização para este dataset.
    Retorne apenas uma lista com instruções simples.
    """

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 1000,
            "temperature": 0.7
        },
    }

    headers = {
        "Authorization": f"Bearer {HUGGINGFACE_API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(
        "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct",
        headers=headers,
        data=json.dumps(payload)
    )

    if response.status_code == 200:
        return response.json()[0]['generated_text'].split("###")[-1].strip()
    else:
        return f"Erro ao consultar o modelo: {response.text}"

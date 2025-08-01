'''
Autor: Thiago Vilarinho Lemes
Data: 2024-01-15
Descrição: Função para exibir o histórico de uploads.
'''
import streamlit as st
import pandas as pd

def hist(conn):
    '''
    Função para exibir o histórico de uploads.
    Esta função consulta o banco de dados e exibe o histórico de uploads.
    em uma tabela no Streamlit.
    Args:
        conn: conexão com o banco de dados.
    '''
    st.write("### 📜 Histórico de uploads")
    df_hist = pd.read_sql_query("SELECT * FROM historico ORDER BY id DESC", conn)
    st.dataframe(df_hist)
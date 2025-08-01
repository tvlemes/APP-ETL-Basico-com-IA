
'''
Autor: Thiago Vilarinho Lemes
Data: 2024-01-15
Descrição: Funções utilitárias para executar comandos Python personalizados e tratar valores nulos em DataFrames.
'''
import pandas as pd
import streamlit as st

# Execução de comandos Python personalizados import matplotlib.pyplot as plt\nst.pyplot(df.hist())
###################################################################################################
def exec_command(df):
    '''
    Função para executar comandos Python personalizados com o DataFrame.
    Esta função permite ao usuário digitar comandos Python que serão executados
    com o DataFrame `df` e o módulo `streamlit` disponível.
    Args:
        df: DataFrame do Pandas que será usado nos comandos.
    '''
    st.write("### 🧠 Execução de comandos Python com o DataFrame")

    codigo_usuario = st.text_area("Digite comandos Python usando o DataFrame `df`", height=200, placeholder="Ex: df.describe()\nimport matplotlib.pyplot as plt\nst.pyplot(df.hist())")

    if st.button("Executar código"):
        try:
            # Cria um ambiente local seguro com acesso ao df e st
            local_env = {"df": df, "st": st, "pd": pd}

            exec(codigo_usuario, {}, local_env)

        except Exception as e:
            st.error(f"Erro ao executar o código: {e}")
###################################################################################################


# Tratamento de valores nulos
###################################################################################################
def tratamento_nulos(df):
    '''
    Função para tratar valores nulos no DataFrame.
    Esta função permite ao usuário escolher como tratar os valores nulos no DataFrame,
    incluindo opções para remover colunas, renomear colunas e aplicar diferentes estratégias
    de preenchimento para valores nulos.
    Args:
        df: DataFrame do Pandas que será tratado.
    Returns:
        list: Lista contendo o DataFrame tratado, colunas removidas, colunas renomeadas e flag de remoção de NA.
    '''

    colunas = list(df.columns)
    col_remover = st.multiselect("Colunas para remover", colunas)
    col_renomear = {}
    st.write("Renomear colunas (opcional)")
    for col in colunas:
        novo_nome = st.text_input(f"{col} →", value=col)
        if novo_nome != col:
            col_renomear[col] = novo_nome
    remover_na = st.checkbox("Remover linhas com valores nulos")

    # Tratamento de valores nulos
    st.write("### 🧹 Tratamento de valores nulos")
    # if df.isnull().sum().sum() > 0:

    st.write("Valores nulos encontrados nas colunas:")
    st.dataframe(df.isnull().sum()[df.isnull().sum() > 0])

    acoes_nulos = ["Remover linhas com nulos", "Preencher com string", "Preencher com média", "Preencher com mediana", "Preencher com moda"]
    escolha_nulos = st.selectbox("Escolha o tratamento para valores nulos:", acoes_nulos)
    colunas_nulas = df.columns[df.isnull().any()].tolist()
    colunas_selecionadas = st.multiselect("Selecione as colunas com nulos para aplicar o tratamento:", colunas_nulas, default=colunas_nulas)

    if escolha_nulos == "Preencher com string":
        valor_str = st.text_input("Digite o valor que será usado para preencher os nulos:")
    
        try:
            if escolha_nulos == "Remover linhas com nulos":
                df = df.dropna(subset=colunas_selecionadas)
            elif escolha_nulos == "Preencher com string":
                df[colunas_selecionadas] = df[colunas_selecionadas].fillna(valor_str)
            elif escolha_nulos == "Preencher com média":
                for col in colunas_selecionadas:
                    if pd.api.types.is_numeric_dtype(df[col]):
                        df[col] = df[col].fillna(df[col].mean())
            elif escolha_nulos == "Preencher com mediana":
                for col in colunas_selecionadas:
                    if pd.api.types.is_numeric_dtype(df[col]):
                        df[col] = df[col].fillna(df[col].median())
            elif escolha_nulos == "Preencher com moda":
                for col in colunas_selecionadas:
                    moda = df[col].mode()
                    if not moda.empty:
                        df[col] = df[col].fillna(moda[0])
            
            # st.success("Tratamento aplicado com sucesso!")
            st.dataframe(df.head())
            
        except Exception as e:
            st.error(f"Erro ao aplicar tratamento: {e}")
    # else:
    #     st.success("✅ Nenhum valor nulo encontrado no DataFrame.")

    return [df, col_remover, col_renomear, remover_na]
###################################################################################################
'''
Autor: Thiago Vilarinho Lemes
Data: 2024-01-15
Descrição: Aplicação Streamlit para upload de arquivos, ETL e histórico em SQLite.
'''
import streamlit as st
import pandas as pd
import os
import sqlite3
from datetime import datetime
from etl.transform import transformar_dados
from utils.type_files import loading_type_files, return_type_files
from utils.save_files import save_files_parquet
from utils.manipulation_functions import tratamento_nulos
from utils.historico import hist
from etl.ai_suggestions import sugerir_transformacao_local
from dotenv import load_dotenv
import os


# Configurações iniciais
load_dotenv()
dt_raw = os.getenv('DT_RAW') 


# Criar pastas e DB
###################################################################################################
os.makedirs(dt_raw, exist_ok=True)
os.makedirs("db", exist_ok=True)
conn = sqlite3.connect("db/historico.sqlite")
conn.execute('''
    CREATE TABLE IF NOT EXISTS historico (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_arquivo TEXT,
        data_upload TEXT,
        colunas_removidas TEXT,
        colunas_renomeadas TEXT,
        linhas_antes INTEGER,
        linhas_depois INTEGER
    )
''')

conn.commit()
###################################################################################################


st.title("📥 APP ETL Básico com IA + Histórico (SQLite)")
st.sidebar.title("⚙️ Configurações da IA")

temperatura = st.sidebar.slider("Temperatura", min_value=0.0, max_value=1.0, value=0.7, step=0.05)
max_tokens = st.sidebar.slider("Max tokens", min_value=50, max_value=5000, value=500, step=50)

# Upload
arquivo = st.file_uploader("Faça upload de um arquivo (.csv, .xlsx, .json, .parquet)", type=["csv", "xlsx", "json", "parquet"])


# Lógica de ETL e salvamento do arquivo em disco
# Leitura do arquivo e criação do DataFrame
# Sugestões de transformação com IA
###################################################################################################
if arquivo:

    nome = arquivo.name
    st.write(f"### Pré-visualização de: `{nome}`")

    # Verifica o tipo de arquivo e carrega o DataFrame
    try:
        df = loading_type_files(nome, arquivo)
        st.dataframe(df.head())
        if st.checkbox("💡 Sugerir transformações com IA"):
            sugestoes = sugerir_transformacao_local(df, temperatura=temperatura, max_tokens=max_tokens)
            st.code(sugestoes, language="markdown")
    except Exception as e:
        st.error(f"Erro ao carregar o arquivo: {e}")
###################################################################################################


# Transformação dos dados
###################################################################################################
    resultado = tratamento_nulos(df)
    if resultado:
        df, col_remover, col_renomear, remover_na = resultado
    else:
        st.stop()
###################################################################################################


# Aplicar ETL e salvar o arquivo
###################################################################################################
    if st.button("Aplicar ETL e salvar"):

        # Salvar em disco
        try:
            linhas_antes = df.shape[0]
            df_transformado = transformar_dados(df, colunas_remover=col_remover, renomear_colunas=col_renomear, drop_na=remover_na)
            linhas_depois = df_transformado.shape[0]
            nome_completo = arquivo.name
            nome_sem_extensao, extensao = os.path.splitext(nome_completo)
            caminho = f"{dt_raw}/{nome_sem_extensao}.parquet"  # Forçar salvar como Parquet
            save_files_parquet(caminho, df_transformado)
            
            # Se quiser salvar em outros formatos, descomente as linhas abaixo
            # loading_type_files(nome_completo, arquivo)  # Carregar o tipo de arquivo
            # tipo_arquivo = return_type_files(nome)
            # save_files_disc(tipo_arquivo, caminho, df_transformado)

            # Salvar as alterações no SQLite
            conn.execute('''
                INSERT INTO historico (nome_arquivo, data_upload, colunas_removidas, colunas_renomeadas, linhas_antes, linhas_depois)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (
                    nome,
                    datetime.now().isoformat(),
                    ','.join(col_remover),
                    str(col_renomear),
                    linhas_antes,
                    linhas_depois
                ))
            conn.commit()

            st.success(f"Arquivo transformado e salvo em: `{caminho}`")
            st.info("Histórico atualizado.")
        except Exception as e:
                st.error("Tipo de arquivo não suportado para salvar.")
###################################################################################################


# Mostrar histórico
###################################################################################################
hist(conn)


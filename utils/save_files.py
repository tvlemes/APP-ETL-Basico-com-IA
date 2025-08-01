'''
Autor: Thiago Vilarinho Lemes
Data: 2024-01-15
Descrição: Funções utilitárias para salvar arquivos em diferentes formatos.
'''
def save_files_disc(tipo_arquivo, caminho, df_transformado):
    '''
    Salva o DataFrame em disco no formato especificado.
    Args:
        tipo_arquivo (str): Tipo de arquivo (csv, xlsx, json, parquet).
        caminho (str): Caminho completo para salvar o arquivo.
        df_transformado (DataFrame): DataFrame a ser salvo.
    '''

    if tipo_arquivo == '.csv':
        df_transformado.to_csv(caminho, index=False)
    elif tipo_arquivo == '.xlsx':   
        df_transformado.to_excel(caminho, index=False)
    elif tipo_arquivo == '.json':
        df_transformado.to_json(caminho, orient='records', lines=True, force_ascii=False)
    elif tipo_arquivo == '.parquet':
        df_transformado.to_parquet(caminho)
    

def save_files_parquet(caminho, df_transformado):
    '''
    Salva o DataFrame em disco no formato Parquet.

    Args:
        caminho (str): Caminho completo para salvar o arquivo Parquet.
        df_transformado (DataFrame): DataFrame a ser salvo.
    '''
    df_transformado.to_parquet(caminho)
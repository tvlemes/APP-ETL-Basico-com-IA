# 🧠 APP ETL Básico com IA

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/tvlemes/APP-ETL-Basico-com-IA/blob/main/LICENSE)
[![Status](https://img.shields.io/badge/status-Em%20Desenvolvimento-yellow.svg)]()

---

## 📄 Descrição

Este projeto apresenta um **aplicativo de ETL com inteligência artificial**, construído com **Streamlit**. Ele permite que usuários façam upload de arquivos tabulares em diversos formatos, recebam **sugestões automáticas de transformação via IA** e salvem os resultados prontos para ingestão em um data warehouse ou banco relacional.

Com ele, usuários podem:

* Fazer upload de arquivos tabulares nos formatos .csv, .parquet, .xlsx, .xls e .xml;

* Aplicar automaticamente transformações sugeridas por IA;

* Realizar tratamentos como preenchimento de valores nulos, renomeações, conversões de tipo e mais;

* Salvar os resultados no formato Parquet, prontos para ingestão em bancos relacionais ou data warehouses.

⚠️ Pré-requisitos:

É necessário ter o **LM Studio instalado** e possuir ao menos um modelo de IA para **geração de texto** já baixado (como Mistral, Gemma ou Roberta), pois o sistema utiliza esses modelos para sugerir **transformações automatizadas** com base na estrutura do dataset carregado.

---

## 🚀 Funcionalidades

- ✅ Upload de arquivos `.csv`, `.parquet`, `.xlsx`, `.xls`, `.xml`
- 🧠 Sugestões inteligentes de transformação com modelos LLMs (via LM Studio ou Hugging Face)
- 🧼 Preenchimento de valores ausentes (auto ou manual)
- 🐍 Execução de comandos Python customizados no DataFrame
- 🗃️ Histórico persistente de uploads e transformações
- 📁 Armazenamento do resultado em formato **Parquet**

---

## 🗃️ Estrutura do Projeto

```bash
📦 app-etl-ia/
├── data_lake/
│   └── raw/                           # Arquivos Parquet transformados
│
├── etl/
│   ├── ai_suggestions.py             # IA para sugestões automáticas
│   └── transform.py                  # Funções clássicas de transformação
│
├── utils/
│   ├── historico.py                  # Histórico de execuções
│   ├── manipulation_functions.py     # Execução dinâmica de código
│   ├── save_files.py                 # Salva DataFrame em disco
│   └── type_files.py                 # Carregamento de arquivos suportados
│
├── app.py                            # Aplicação Streamlit principal
├── requirements.txt                  # Dependências do projeto
└── README.md                         # Este arquivo
```

---

## 🧪 Instalação Local

```bash
git clone https://github.com/tvlemes/APP-ETL-Basico-com-IA
cd APP-ETL-Basico-com-IA
python -m venv venv
source venv/bin/activate  # ou .\venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

---

## 📄 Licença

Este projeto está licenciado sob a licença [MIT](https://github.com/tvlemes/APP-ETL-Basico-com-IA/blob/main/LICENSE).
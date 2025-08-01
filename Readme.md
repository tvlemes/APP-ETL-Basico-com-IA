# 🧠 APP ETL Básico com IA

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/tvlemes/APP-ETL-Basico-com-IA/blob/main/LICENSE)
[![Status](https://img.shields.io/badge/status-Em%20Desenvolvimento-yellow.svg)]()

---

## 📄 Descrição

Este projeto apresenta um **aplicativo de ETL com inteligência artificial**, construído com **Streamlit**. Ele permite que usuários façam upload de arquivos tabulares em diversos formatos, recebam **sugestões automáticas de transformação via IA** e salvem os resultados prontos para ingestão em um data warehouse ou banco relacional.

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
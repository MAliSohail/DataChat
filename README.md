# DataChat 💬

An AI-powered data assistant built with Python and Streamlit that lets you 
upload any CSV or Excel report and ask questions about it in plain English.

## How it works

1. Upload a CSV or Excel file (e.g. a KPI report or product dataset)
2. The app loads your data and passes it as context to an LLM (GPT-4o-mini)
3. Ask questions in natural language and get answers based strictly on your data

This follows the core principle of a RAG (Retrieval-Augmented Generation) 
pipeline — grounding LLM responses in a specific knowledge base rather than 
general training data.

## Tech Stack

- Python
- Streamlit
- OpenAI API (GPT-4o-mini)
- Pandas

## Use Cases

- Querying business reports without writing formulas
- Summarizing data quality issues
- Extracting KPI insights from raw datasets

## Setup

1. Clone the repo
2. Install dependencies: `pip install streamlit pandas openpyxl openai`
3. Add your OpenAI API key to `.streamlit/secrets.toml`:
   `OPENAI_API_KEY = "your-key-here"`
4. Run: `python -m streamlit run app.py`
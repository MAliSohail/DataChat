import streamlit as st
import pandas as pd
from openai import OpenAI

# Configure OpenAI
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="DataChat", page_icon="💬")
st.title("💬 DataChat")
st.caption("Upload a report or dataset and ask questions about it in plain English.")

# File upload
uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file:
    # Read file
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.success(f"Loaded {len(df)} rows and {len(df.columns)} columns.")
    st.dataframe(df.head(10))

    # Convert dataframe to text for context
    data_as_text = df.to_string(index=False)

    # Chat interface
    st.divider()
    st.subheader("Ask a question about your data")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("e.g. Which region has the highest budget?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Build RAG-style prompt
        system_prompt = f"""You are a data analyst assistant.
You answer questions strictly based on the dataset provided below.
If the answer is not in the data, say so clearly.

DATASET:
{data_as_text}
"""
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ]
        )
        answer = response.choices[0].message.content

        st.session_state.messages.append({"role": "assistant", "content": answer})
        with st.chat_message("assistant"):
            st.markdown(answer)
else:
    st.info("Please upload a CSV or Excel file to get started.")
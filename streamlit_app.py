# %%
# import streamlit as st
# from langchain.llms.openai import OpenAI
# from langchain.agents import load_tools, initialize_agent
# Import libraries
import streamlit as st
import pandas as pd
import json
from pandas import json_normalize
import os 

# Specify the file name and its relative path
current_dir = os.getcwd() + "\\gitRepos" + "\\"
file_name = "gitJSON.txt"
file_path = os.path.join(current_dir, file_name)
# Check if the file exists
if os.path.isfile(file_path):
    # File exists, perform operations on the file
    with open(file_path, "r") as file:
        text = file.read()
        data = json.loads(text)

else:
    # File does not exist
    print("File not found.")
# Use pandas.DataFrame.from_dict() to Convert JSON to DataFrame
df = pd.DataFrame.from_dict(data)

# %%
# Page setup
st.set_page_config(page_title="Github Semantic Search Engine", page_icon="🐍", layout="wide")
st.title("Github Semantic Search Engine")

# Use a text_input to get the keywords to filter the dataframe
text_search = st.text_input("What kind of github repo do you need?", value="")
if text_search:
    from sentence_transformers import SentenceTransformer, util
    import torch as t
    import os

    model = SentenceTransformer('sentence-transformers/paraphrase-mpnet-base-v2')

    # Get the current working directory
    current_dir = os.getcwd() + "\\gitRepos" + "\\descriptions" + "\\"
    searchQuery = text_search
    sentences = []
    sentences.append(searchQuery)
    similarity = []
    for x in range(100):
        # Specify the file name and its relative path
        file_name = f"{x}"
        file_path = os.path.join(current_dir, file_name)
        # Check if the file exists
        if os.path.isfile(file_path):
            # File exists, perform operations on the file
            with open(file_path, "r") as file:
                text = file.read()
                sentences.append(text)
        else:
            # File does not exist
            print("File not found.")
    embeddings = model.encode(sentences)
    for x in range(100):
        similarity.append(util.pytorch_cos_sim(embeddings[0], embeddings[x+1]))
    print(similarity)
    print(t.argmax(t.tensor(similarity)))
    # Filter the dataframe using masks
    m1 = df["full_name"].str.contains(text_search)
    m2 = df["name"].str.contains(text_search)
    df_search = df.iloc[t.topk(t.tensor(similarity), k=2)[1].tolist()]
    print(df_search)
    # Show the results, if you have a text_search
    N_cards_per_row = 3
    for n_row, row in df_search.reset_index().iterrows():
        i = n_row%N_cards_per_row
        if i==0:
            st.write("---")
            cols = st.columns(N_cards_per_row, gap="large")
        # draw the card
        with cols[n_row%N_cards_per_row]:
            st.caption(f"{row['name'].strip()} - {row['html_url'].strip()} - {row['description'].strip()} ")
            st.markdown(f"**{row['name'].strip()}**")
            st.markdown(f"*{row['full_name'].strip()}*")
            st.markdown(f"**{row['id']}**")
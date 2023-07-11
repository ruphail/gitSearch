#%%
from sentence_transformers import SentenceTransformer, util
sentences = ["This is an example sentence", "Each sentence is converted"]

model = SentenceTransformer('sentence-transformers/paraphrase-mpnet-base-v2')
embeddings = model.encode(sentences)
print(embeddings)
util.pytorch_cos_sim(embeddings[0], embeddings[1])
# %%
import os

# Get the current working directory
current_dir = os.getcwd() + "\\gitRepos" + "\\descriptions" + "\\"
searchQuery = "Javascript Application"
sentences = []
sentences.append(searchQuery)
similarity = []
print(sentences)
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
# %%
import torch as t
print(t.argmax(t.tensor(similarity)))
# %%

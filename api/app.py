from flask import Flask,jsonify
import pinecone
import os
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer

app = Flask(__name__)

@app.route('/')
def pineconesearch():
    bashcommand="gcloud functions list"
    all_functions = os.popen(bashcommand).read()
    all_functions=all_functions.split("\n\n")

    model= SentenceTransformer("flax-sentence-embeddings/all_datasets_v3_mpnet-base")
    all_embeddings = model.encode(all_functions)
    all_embeddings.shape

    tokenizer = AutoTokenizer.from_pretrained('transfo-xl-wt103')
    all_functions_list_tokens = [tokenizer.tokenize(function.lower()) for function in all_functions]

    pinecone.init(api_key='853364c2-0cf3-4c6b-bb7e-8508807c99f9',enviroment='us-west1-gcp')

    list=[2,3,4]
    list_function_name=[]
    for i in list:
        list_function_name.append(all_functions_list_tokens[i][2])
    
    return jsonify(list_function_name)

if __name__ == "__main__":
    app.run(debug=True)
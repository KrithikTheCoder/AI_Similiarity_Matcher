import os
from flask import Flask, request, jsonify
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# Load or create FAISS vector store
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

FAISS_INDEX_PATH = "faiss_index"

if os.path.exists(FAISS_INDEX_PATH):
    print("Loading existing FAISS index...")
    vector_store = FAISS.load_local(FAISS_INDEX_PATH, embeddings, allow_dangerous_deserialization=True)

else:
    print("Creating new FAISS index...")
    urls = ["https://brainlox.com/courses/category/technical"]
    loader = UnstructuredURLLoader(urls=urls)
    documents = loader.load()

    vector_store = FAISS.from_documents(documents, embeddings)
    vector_store.save_local(FAISS_INDEX_PATH)

# Step 3: Create a Flask RESTful API
app = Flask(__name__)


@app.route('/query', methods=['POST'])
def query_vector_store():
    data = request.get_json()
    user_query = data.get('query', '')

    print(f"Received query: {user_query}")

    if not user_query:
        return jsonify({"error": "No query provided"}), 400

    # Retrieve documents similar to the query
    results = vector_store.similarity_search(user_query, k=2)

    # Format the results
    response = [{"content": res.page_content, "metadata": res.metadata} for res in results]

    print("Sending response:",response[0]['content'])
    return jsonify(response)


if __name__ == '__main__':
    print("Starting Flask API on port 5001...")
    app.run(host='0.0.0.0', port=5001)

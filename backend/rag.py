import chromadb
from sentence_transformers import SentenceTransformer

from backend.config import *

model = SentenceTransformer(MODEL_NAME)

client = chromadb.PersistentClient(
    path=VECTOR_DB_PATH
)

collection = client.get_collection(
    COLLECTION_NAME
)


def retrieve_context(question):

    embedding = model.encode(question).tolist()

    results = collection.query(
        query_embeddings=[embedding],
        n_results=TOP_K_RESULTS
    )

    contexts = results["documents"][0]

    return "\n\n".join(contexts)
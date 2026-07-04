import chromadb
from sentence_transformers import SentenceTransformer

print("=" * 60)
print("AI Evaluation Platform - Retrieval Test")
print("=" * 60)

print("\nLoading embedding model...")

model = SentenceTransformer("all-MiniLM-L6-v2")

print("Model Loaded!")

print("\nConnecting to ChromaDB...")

client = chromadb.PersistentClient(path="vector_db")

collection = client.get_collection("knowledge_base")

print("Connected!")

print(f"Knowledge Base Size : {collection.count()} chunks")

print("\nType 'exit' to quit.")

while True:

    query = input("\nEnter Question : ")

    if query.lower() == "exit":
        break

    embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[embedding],
        n_results=3
    )

    print("\nTop Results")
    print("=" * 60)

    for i in range(len(results["documents"][0])):

        print(f"\nResult {i+1}")

        print("-" * 50)

        print("Question :")
        print(results["metadatas"][0][i]["question"])

        print("\nAnswer :")
        print(results["metadatas"][0][i]["answer"])

        print("\nDataset :")
        print(results["metadatas"][0][i]["dataset"])

        print("\nRetrieved Context :")
        print(results["documents"][0][i][:500])

        print("-" * 50)
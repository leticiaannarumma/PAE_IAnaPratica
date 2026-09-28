import chromadb

chroma_client = chromadb.Client()

collection = chroma_client.create_collection(name="filmes_collection")

collection.add(
    documents=[
        "É um documento com os filmes que ganharam o premio do Oscars nos ultimos 10 anos",
        "É outro documento com os atores e atrizes que ganharam o Oscar de melhor atuação nos ultimos 10 anos",
        "É outro documento com os diretores que ganharam o Oscar de melhor direção nos ultimos 10 anos"
    ],
    metadatas=[
        {"source": "filmes1"},
        {"source": "filmes2"},
        {"source": "filmes3"}
    ],
    ids=[
        "id1",
        "id2",
        "id3"
    ]
)
results = collection.query(
    query_texts=[
        "Eu gostaria de saber sobre os vencedores do Oscar de filmes, atores e diretores"
    ],
    n_results=3
)

print(results)
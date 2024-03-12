from elasticsearch import Elasticsearch

# Conecte-se ao seu cluster Elasticsearch
es = Elasticsearch(["http://localhost:9200"])

# Defina o índice que deseja buscar
indice = "pdf_documents"

# Defina a query de busca
query = {
    "query": {
        "match": {
            "content": "econômico"
        }
    }
}

# Realize a busca
resultado = es.search(index=indice, body=query)

if resultado is None or 'hits' not in resultado or resultado['hits']['total']['value'] == 0:
    print("null")
else:
    for hit in resultado['hits']['hits']:
        print(hit['_source']['titulo'])
        print(hit['_id'])

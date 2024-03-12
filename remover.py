from elasticsearch import Elasticsearch

# Conectando-se ao Elasticsearch
es = Elasticsearch(["http://localhost:9200"])


# ID do documento que você deseja remover
documento_id = "kd08MI4BkWZAHwFsXEIX"  # Substitua pelo ID do documento que você deseja remover

# Removendo o documento pelo ID
es.delete(index="pdf_documents", id=documento_id)  # Substitua "seu_indice" pelo nome do seu índice
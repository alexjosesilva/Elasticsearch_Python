import PyPDF2
from elasticsearch import Elasticsearch

def extract_text_from_pdf(pdf_path):
    """
    Extrai o texto de um arquivo PDF e retorna como uma string.
    """
    text = ''
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text() + " "
    return text


def index_pdf_content(pdf_path, index_name='pdf_documents'):
    """
    Indexa o conteúdo de um arquivo PDF no Elasticsearch.
    """
    # Conectar ao Elasticsearch com autenticação básica
    # es = Elasticsearch(["http://localhost:9200"], http_auth=("elastic", "123456"))
    es = Elasticsearch(["http://localhost:9200"])

    # Extrair texto do PDF
    pdf_text = extract_text_from_pdf(pdf_path)

    # Indexar o texto extraído no Elasticsearch
    document = {
        "titulo": "Entendendo Algoritmos: Fundamentos e Exemplos",
        "content": pdf_text,
        "filename": pdf_path.split('/')[-1]  # Nome do arquivo
    }
    response = es.index(index=index_name, body=document)
    print("Documento indexado com sucesso:", response['_id'])

# Caminho para o arquivo PDF que você deseja indexar
pdf_path = "pdf/algoritmo.pdf"

# Indexar o PDF no Elasticsearch
index_pdf_content(pdf_path)

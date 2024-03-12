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

def clean_text(text):
    # Remove quebras de linha e espaços extras
    cleaned_text = ' '.join(text.split())
    return cleaned_text

def index_pdf_content(pdf_path, index_name='pdf_documents'):
    """
    Indexa o conteúdo de um arquivo PDF no Elasticsearch.
    """
    # Conectar ao Elasticsearch com autenticação básica
    # es = Elasticsearch(["http://localhost:9200"], http_auth=("elastic", "123456"))
    es = Elasticsearch(["http://localhost:9200"])

    # Extrair texto do PDF
    pdf_text = extract_text_from_pdf(pdf_path)

    # Supondo que pdf_text seja o texto extraído do PDF
    cleaned_pdf_text = clean_text(pdf_text)

    print(cleaned_pdf_text)

    # Indexar o texto extraído no Elasticsearch
    document = {
        "titulo": "Capitalismo: Benefícios e Limitações",
        "content": cleaned_pdf_text,
        "filename": pdf_path.split('/')[-1]  # Nome do arquivo
    }
    response = es.index(index=index_name, body=document)
    print("Documento indexado com sucesso:", response['_id'])

# Caminho para o arquivo PDF que você deseja indexar
pdf_path = "pdf/arquivos/arquivo3.pdf"

# Indexar o PDF no Elasticsearch
index_pdf_content(pdf_path)

import streamlit as st
from azure.storage.blob import BlobServiceClient
import os
import pymssql
import uuid
from dotenv import load_dotenv

load_dotenv()
BlobConnectionString = os.getenv('BLOB_CONNECTION_STRING')
BlobContainerName = os.getenv('BLOB_CONTAINER_NAME')
BlobAccountName = os.getenv('BLOB_ACCOUNT_NAME')

SQL_SERVER = os.getenv('SQL_SERVER')
SQL_DATABASE = os.getenv('SQL_DATABASE')
SQL_USER = os.getenv('SQL_USER')
SQL_PASSWORD = os.getenv('SQL_PASSWORD')

st.title('Cadastro de Produtos')

product_name = st.text_input('Nome do produto')
product_price = st.number_input('Preço do produto', min_value=0.0, format='%.2f')
product_description = st.text_area('Descrição do produto')
product_image = st.file_uploader('Imagem do produto', type=['jpg', 'png, jpeg'])

def upload_blob(file):
    blob_service_client = BlobServiceClient.from_connection_string(BlobConnectionString)
    container_client = blob_service_client.get_container_client(BlobContainerName)
    blob_name = str(uuid.uuid4()) + file.name
    blob_client = container_client.get_blob_client(blob_name)
    blob_client.upload_blob(file.read(), overwrite= True)
    image_url = f"https://{BlobAccountName}.blob.core.windows.net/{BlobContainerName}/{blob_name}"
    return image_url

def insert_product(product_name, product_price, product_description, product_image):

    try:
        image_url = upload_blob(product_image)
        conn = pymssql.connect(server=SQL_SERVER, user=SQL_USER, password=SQL_PASSWORD, database=SQL_DATABASE)
        cursor = conn.cursor()
        insert_sql = (f"INSERT INTO dbo.Produtos (nome, preco, descricao, image_url) VALUES ('{product_name}', {product_price}, '{product_description}', '{image_url}')")
        print(insert_sql)
        cursor.execute(insert_sql)
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        st.error(f'Erro ao inserir produto: {e}')
        return False

def list_products():
    try:
        conn = pymssql.connect(server=SQL_SERVER, user=SQL_USER, password=SQL_PASSWORD, database=SQL_DATABASE)
        cursor = conn.cursor(as_dict=True)
        cursor.execute("SELECT * FROM Produtos")
        rows = cursor.fetchall()
        conn.close()
        return rows
    except Exception as e:
        st.error(f"Erro ao listar produtos: {e}")
        return[]
    
def list_products_screen():
    products = list_products()
    if products:
        cards_for_rows = 3
        cols = st.columns(cards_for_rows)
        for i, product in enumerate(products):
            col = cols[i % cards_for_rows]
            with col:
                st.markdown(f"### {product['nome']}")
                st.write(f"**Descrição:** {product['descricao']}")
                st.write(f"**Preço:** {product['preco']:2f}")
                if product["image_url"]:
                    html_img = f'<img src="{product["image_url"]}" width="200" height="200" alt="imagem do produto">'
                    st.markdown(html_img, unsafe_allow_html=True)
                st.markdown("---")
            if(i + 1) % cards_for_rows == 0 and (i + 1) < len(products):
                cols = st.columns(cards_for_rows)
    else:
        st.info("Nenhum produto encontrado")

if st.button('Salvar produto'): 
    insert_product(product_name, product_price, product_description, product_image)
    return_message = 'Produto salvo com sucesso'
    list_products_screen()

st.header('Produto cadastrados')

if st.button('Listar produtos'):
    list_products_screen()
    return_message = 'Produtos listados com sucesso'
# 🛒 Sistema de Cadastro de Produtos - Azure & Streamlit

Este projeto é uma aplicação web completa para gerenciamento de inventário, desenvolvida para integrar serviços de nuvem da **Microsoft Azure** com uma interface moderna em **Python**.

A aplicação permite cadastrar produtos com nome, preço, descrição e imagem, armazenando os dados estruturados no **Azure SQL Database** e os arquivos de mídia no **Azure Blob Storage**.

---

## 🚀 Tecnologias Utilizadas

* **Linguagem:** Python 3.14
* **Interface Web:** [Streamlit](https://streamlit.io/)
* **Banco de Dados:** Azure SQL Database (utilizando a biblioteca `pymssql`)
* **Armazenamento de Arquivos:** Azure Blob Storage (utilizando `azure-storage-blob`)
* **Gestão de Ambiente:** `python-dotenv` para segurança de credenciais.

---

## 🛠️ Funcionalidades

- [x] **Cadastro de Produtos:** Formulário intuitivo para entrada de dados.
- [x] **Upload de Imagens:** Integração automática com o Azure Blob Storage para hospedagem de fotos.
- [x] **Listagem Dinâmica:** Visualização dos produtos cadastrados em formato de cards.
- [x] **Segurança de Dados:** Uso de variáveis de ambiente para proteção de chaves de acesso.

---

## 📂 Estrutura do Projeto



```text
├── .env                # Credenciais reais (não enviado ao GitHub)
├── .env.example        # Modelo de configuração para novos usuários
├── .gitignore          # Proteção de arquivos sensíveis
├── main.py             # Código principal da aplicação
├── requirements.txt    # Lista de dependências do projeto
└── README.md           # Documentação do projeto 
```
## 🔧 Como Executar o Projeto

Para rodar este projeto localmente, siga os passos abaixo:

1. **Clone o Repositório:**
   ```bash
   git clone https://github.com/nathanshigaki/azure-streamlit-sqlserver.git
   ```
2. **Configurar Ambiente Virtual (Venv):**
   ```bash
   python -m venv .venv
   # Ativar no Windows:
   .venv\Scripts\activate
   # Ativar no Linux/Mac:
   source .venv/bin/activate
   ```
3. **Instalar Dependências:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Configurar Credenciais (Variáveis de Ambiente):**
*  Renomeie o ficheiro .env.example para .env.
*  Abra o ficheiro .env e insira as suas chaves da Azure (SQL Server e Storage Account).
5. **Rodar a Aplicação:**
   ```bash
   streamlit run main.py
   ```

# Sistema de Gestão de Estoque e Vendas

Este é um sistema de gestão de estoque e vendas desenvolvido em Django com Django REST Framework. O projeto tem como objetivo fornecer uma API para gerenciar diferentes aspectos de um sistema de vendas, incluindo produtos, fornecedores, clientes e transações de venda.

## Funcionalidades

- **Gerenciamento de Lotes**: Criação, leitura, atualização e deleção de lotes de produtos.
- **Gerenciamento de Produtos**: Cadastro e controle de produtos em estoque.
- **Gerenciamento de Fornecedores**: Registro e manutenção de informações sobre fornecedores.
- **Gerenciamento de Clientes**: Cadastro e gerenciamento de clientes.
- **Itens de Venda**: Controle de itens em vendas, permitindo adicionar produtos a transações.
- **Movimentação de Estoque**: Registro de movimentações de estoque, como entradas e saídas de produtos.
- **Vendas**: Registro de vendas realizadas, incluindo detalhes de transações.
- **Categorias de Produtos**: Classificação de produtos em categorias.
- **Promoções**: Cadastro e controle de promoções em produtos.
- **Histórico de Preços**: Acompanhamento do histórico de preços de produtos.
- **Configurações de PDV**: Gerenciamento das configurações do ponto de venda.
- **Log de Auditoria**: Registro de ações realizadas no sistema para auditoria.

## Tecnologias Utilizadas

- **Django**: Framework web utilizado para o desenvolvimento do backend.
- **Django REST Framework**: Biblioteca para construir APIs RESTful de forma rápida e fácil.
- **SQLite**: Banco de dados utilizado para armazenamento de dados.

## Instalação

### Pré-requisitos

- Python 3.x
- pip
- Django
- Django REST Framework

### Passos para instalação

1. Clone o repositório:
   
   git clone (https://github.com/ocaioffernan/DJANGO-API.git)
   cd DJANGO-API
   
**##Crie um ambiente virtual e ative-o:**

python -m venv venv
source venv/bin/activate  # Para Linux/Mac
venv\Scripts\activate  # Para Windows

**##Instale as dependências:**

pip install -r requirements.txt

**##Realize as migrações do banco de dados:**

python manage.py migrate

**##Inicie o servidor:**

python manage.py runserver
Acesse a API em http://127.0.0.1:8000/.

**##Uso**

A API fornece endpoints para realizar operações CRUD (Create, Read, Update, Delete) em cada modelo.

**##Contribuição**

Contribuições são bem-vindas! Sinta-se à vontade para abrir um issue ou enviar um pull request.

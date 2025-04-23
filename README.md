📦 API de Consulta de Produtos - FarmaFácil
Esta aplicação em Flask disponibiliza uma API REST para consultar produtos da base de dados farmafacil, retornando a descrição e o grupo de produtos válidos, com autenticação por chave de API.

🚀 Tecnologias utilizadas
Python 3

Flask

psycopg2 (PostgreSQL)

🔧 Como usar
📁 Clone o repositório
bash
Copiar
Editar
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
📦 Instale as dependências
bash
Copiar
Editar
pip install flask psycopg2
⚙️ Configure a aplicação
No código, a conexão com o banco e a chave de acesso estão definidas diretamente:

python
Copiar
Editar
API_KEY = "************"
🔐 Recomenda-se mover essas informações sensíveis para variáveis de ambiente ou arquivos .env em produção.

▶️ Executando o servidor
bash
Copiar
Editar
python app.py
O servidor ficará disponível em:

arduino
Copiar
Editar
http://localhost:5000
📌 Endpoints
GET /produtos
Consulta produtos pertencentes aos grupos definidos.

Parâmetros obrigatórios:
key: chave de API para autenticação

Exemplo de requisição:
vbnet
Copiar
Editar
GET /produtos?key=d8A3b6JvQ1xP9zT7EwLm2YFkUo4RNsHG
Exemplo de resposta:
json
Copiar
Editar
[
  {
    "descricao": "dipirona 500mg",
    "grupo": 30
  },
  {
    "descricao": "paracetamol 750mg",
    "grupo": 31
  }
]
Respostas de erro:
403 Unauthorized – quando a chave de API é inválida.

500 Internal Server Error – erro de conexão ou consulta no banco de dados.
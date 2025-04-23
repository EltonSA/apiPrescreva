# 🧪 API de Consulta de Produtos - FarmaFácil

Esta é uma API simples desenvolvida com Flask que permite consultar produtos do banco de dados **FarmaFácil**, retornando sua descrição e código de grupo, com autenticação via **chave de API**.

---

## 📌 Funcionalidades

- 🔐 Autenticação via chave de API
- 📦 Consulta de produtos com base em grupos válidos
- 🧾 Retorno em JSON com descrição e grupo do produto

---

## 🚀 Tecnologias Utilizadas

- Python 3.x
- Flask
- psycopg2 (PostgreSQL)

---

## ⚙️ Como Usar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

## 2. Instale as dependências
```bash
pip install flask psycopg2
```
## 3. Execute o servidor
```bash
python app.py
```
## O servidor estará disponível em:
```bash
http://meudominio:5000
```

## 🔐 Autenticação
```bash
/produtos?key=SUA_CHAVE_AQUI
```
## Chave atual definida no código:
```bash
d8A3b6JvQ1xP9zT7E**********
```

## 📨 Endpoint
### GET /produtos
- Retorna a lista de produtos pertencentes a grupos válidos.

Parâmetro | Tipo    | Obrigatório   | Descrição
key       | string  | ✅ Sim       |  have de autenticação

### Exemplo de requisição:
```bash
GET http://meudominio:5000/produtos?key=d8A3b6JvQ1xP9z*********
```

### Exemplo de reposta
```bash
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
```

## Possíveis Erros:

Código | Significado
403 | Acesso não autorizado
500 | Erro ao conectar ou consultar o banco de dados
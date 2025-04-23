from flask import Flask, jsonify, request
import psycopg2
import os

app = Flask(__name__)

# Chave da API
API_KEY = "d8A3b6JvQ1xP9zT7EwLm2YFkUo4RNsHG"

# Grupos válidos definidos
GRUPOS_VALIDOS = [
    30, 31, 92, 27, 8, 88, 33, 116,
    21, 19, 20, 16, 12, 23, 126, 29,
    28, 26, 25, 32
]

# Conexão com o banco de dados
def conectar_banco():
    try:
        conexao = psycopg2.connect(
            host="apparenza.dyndns.org",
            port="5432",
            database="farmafacil",
            user="suporte",
            password="80207024"
        )
        return conexao
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

@app.route('/produtos', methods=['GET'])
def consultar_produtos():
    # Validação da chave de API
    key = request.args.get("key")
    if key != API_KEY:
        return jsonify({"erro": "Acesso não autorizado"}), 403

    conexao = conectar_banco()
    if conexao:
        cursor = conexao.cursor()
        try:
            consulta = """
                SELECT descricaoproduto, codigogrupo
                FROM data.produto
                WHERE codigogrupo::int = ANY(%s)
            """
            cursor.execute(consulta, (GRUPOS_VALIDOS,))
            resultados = cursor.fetchall()

            produtos = [
                {
                    "descricao": row[0].strip().lower() if row[0] else "",
                    "grupo": int(row[1]) if row[1] is not None else None
                }
                for row in resultados
            ]

            conexao.close()
            return jsonify(produtos)

        except Exception as e:
            conexao.close()
            return jsonify({"erro": str(e)}), 500
    else:
        return jsonify({"erro": "Falha ao conectar ao banco de dados"}), 500

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)

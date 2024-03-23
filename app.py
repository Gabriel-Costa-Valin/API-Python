# Para criar uma API se é preciso ter em mente 4 coisas
# 1. Objetivo - Criar uma api que disponibiliza a consulta, criação, edição e exclusão de livros.
# 2. URL Base - localhost
# 3. Endpoints {
#   localhost/livros (GET)
#   localhost/livros (POST)
#   localhost/livros/id (GET com ID)
#   localhost/livros/id (PUT)
#   localhost/livros/id (DELETE)
#}
# 4. Quais recursos disponibilizar - Livros

from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'Harry Potter e a Pedra Filosofal',
        'autor': 'J.K Rowling'
    },
    {
        'id': 2,
        'titulo': 'O Senhor dos Anéis - A Sociedade do Anel',
        'autor': 'J.R.R Tolkien'
    },
    {
        'id': 3,
        'titulo': 'James Clear',
        'autor': 'Hábitos Atômicos'
    }
]

#Criar uma API que nos permite consultar (Todos), consultar por (ID), editar e excluir

#Consultar (todos)
@app.route('/livros',methods=['GET'])
def obterLivros():
    return jsonify(livros)


#Consultar por ID
@app.route('/livros/<int:id>',methods=['GET'])
def obterLivroID(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)


#Editar
@app.route('/livros/<int:id>', methods=['PUT'])
def editarLivroID(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])

#Criar
@app.route('/livros',methods=['POST'])
def incluirLivro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)


#Excluir
@app.route('/livros/<int:id>',methods=['DELETE'])
def excluirLivro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    
    return jsonify(livros)

app.run(port=5000,host='localhost',debug=True)
from flask import Flask, render_template, request, redirect, url_for
from modelos import Livro, Estante # Assumindo que suas classes estão em outro arquivo

app = Flask(__name__)

# --- Ponto crítico da orientação a objetos ---
# É criada UMA ÚNICA instância da Estante.
# Este objeto 'minha_estante' vai persistir enquanto o app estiver rodando.
# É ele que vai carregar os livros do arquivo e manter a lista em memória.
minha_estante = Estante()
# ---------------------------------------------

@app.route('/')
def pagina_inicial():
    """
    Rota principal. Exibe a estante de livros.
    """
    # Acessa o método do objeto para pegar a lista de livros de forma segura
    livros_na_estante = minha_estante.get_livros()

    # Renderiza o HTML, passando a lista de livros para o template
    return render_template('estante.html', livros=livros_na_estante)

@app.route('/adicionar', methods=['POST'])
def adicionar_livro():
    """
    Rota que recebe os dados do formulário para adicionar um novo livro.
    """
    # 1. Pega os dados enviados pelo formulário
    titulo = request.form['titulo']
    autor = request.form['autor']

    # 2. Cria um NOVO OBJETO Livro com esses dados
    novo_livro = Livro(titulo=titulo, autor=autor)

    # 3. Usa o MÉTODO do objeto Estante para adicionar o novo livro
    minha_estante.adicionar_livro(novo_livro)

    # 4. Redireciona o usuário de volta para a página inicial
    return redirect(url_for('pagina_inicial'))

# Roda o servidor de desenvolvimento
if __name__ == '__main__':
    # Para rodar em produção, defina debug=False
    app.run(debug=True)
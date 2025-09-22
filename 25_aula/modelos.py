import json
import os

class Livro:
    """
    Representa um único livro com título e autor.
    Esta classe é o "molde" para cada livro a ser cadastrado.
    """
    def __init__(self, titulo: str, autor: str):
        # Atributos de cada objeto Livro
        self.titulo = titulo
        self.autor = autor

class Estante:
    """
    Gerencia uma coleção de objetos Livro.
    É responsável por adicionar, carregar e salvar os livros.
    """
    def __init__(self, arquivo_json='estante.json'):
        self._arquivo = arquivo_json
        self._livros = []
        # Chame o método de carregamento logo no início
        self._carregar_livros()

    # O decorator @property já lida com o acesso seguro, mas vamos criar um método
    # para retornar uma cópia da lista e evitar modificações externas.
    def get_livros(self):
        """Retorna uma cópia da lista de livros para evitar modificações diretas."""
        return list(self._livros)

    def adicionar_livro(self, livro: Livro):
        """Adiciona um novo livro à estante e salva a lista no arquivo."""
        # Use um tipo explícito para a verificação, garantindo que apenas objetos Livro sejam adicionados.
        if not isinstance(livro, Livro):
            raise TypeError("O objeto a ser adicionado deve ser uma instância da classe Livro.")

        self._livros.append(livro)
        self._salvar_livros()

    def _salvar_livros(self):
        """Salva a lista atual de livros no arquivo JSON. Este é um método interno."""
        lista_para_salvar = [vars(livro) for livro in self._livros]
        try:
            with open(self._arquivo, 'w', encoding='utf-8') as f:
                json.dump(lista_para_salvar, f, ensure_ascii=False, indent=4)
        except IOError as e:
            print(f"Erro ao salvar o arquivo: {e}")

    def _carregar_livros(self):
        """
        Carrega os livros do arquivo JSON ao iniciar.
        Este é um método interno, não deve ser chamado fora da classe.
        """
        if not os.path.exists(self._arquivo):
            return

        try:
            with open(self._arquivo, 'r', encoding='utf-8') as f:
                dados_json = json.load(f)
                # Use uma list comprehension com validação para garantir a integridade dos dados.
                self._livros = [Livro(dado['titulo'], dado['autor']) for dado in dados_json
                                if 'titulo' in dado and 'autor' in dado]
        except (json.JSONDecodeError, IOError) as e:
            print(f"Erro ao carregar ou decodificar o arquivo: {e}")
            self._livros = [] # Garante que a lista não fique em um estado inválido
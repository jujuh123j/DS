from transacao import Transacao
"""
movimentacao1 = Transacao("Salário de 07/2025", 2000.0,"Receita")
movimentacao2 = Transacao("Conta de luz 07/2025", 200.0,"Despesa")


print(movimentacao1)
print(movimentacao2) """

#Pedir para o usuario cadastrar a transação 
""" descricao = input("Forneça uma descrição da nova transação:")
valor = float(input("Informe o valor da transação"))
tipo = input("Tipo da transação:")

movimentacao3 = Transacao(descricao,valor,tipo)

print(movimentacao3) """


""" 
Classe para gerenciar as transações do usuario, permitindo adicionar ou
excluir transações. 
"""

class ControleFinanceiro:
    def __init__(self,nome_arquivo='transacoes.csv'):
        self._transacoes = []
    def adicionaTransacao(self, transacao: Transacao):
        if isinstance(transacao, Transacao):
            self._transacoes.append(transacao)
            print("Transação adicionada vom sucesso")

        else:
            print("Erro! Apenas objetos do tipo Transacao podem ser adicionados")

    def listarTransacoes(self):
        if not self._transacoes:
            print("Nenhuma transação cadastrada!")
            return
    
        for transacao in self._transacoes:
            print(transacao)


class ControleFinanceiro: 

""" Gerencia uma coleção de transações financeiras, com capacidade de salvar e carregar de um arquivo CSV. 
"""
 def __init__(self, nome_arquivo='transacoes.csv'): """ Construtor da classe ControleFinanceiro. """ self._transacoes = [] self._nome_arquivo = nome_arquivo # O encapsulamento é aplicado aqui. A lista de transações e o nome do arquivo
# são "protegidos" dentro do objeto.
self.carregar_transacoes() # <-- NOVO: Carrega os dados ao iniciar
def adicionar_transacao(self, transacao: Transacao):
"""
Adiciona uma nova transação à lista e salva no arquivo.
"""
if isinstance(transacao, Transacao):
self._transacoes.append(transacao)
self.salvar_transacoes() # <-- NOVO: Salva a lista após adicionar
print("Transação adicionada e salva com sucesso!")
else:
print("Erro: Apenas objetos do tipo Transacao podem ser adicionados.")
def listar_transacoes(self):
"""
Exibe todas as transações registradas.
"""
if not self._transacoes:
print("\nNenhuma transação registrada.")
return
print("\n--- Extrato Financeiro ---")
for transacao in self._transacoes:
print(transacao)
print("--------------------------")
def calcular_saldo(self) -> float:
"""
Calcula e retorna o saldo total (receitas - despesas).
"""
saldo = 0.0
for transacao in self._transacoes:
if transacao.tipo.lower() == 'receita':
saldo += transacao.valor
else:
saldo -= transacao.valor
return saldo
def salvar_transacoes(self):
"""
Salva a lista de transações em um arquivo CSV.
"""
try:
with open(self._nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
# O cabeçalho do nosso CSV
cabecalho = ['descricao', 'valor', 'tipo']
escritor = csv.DictWriter(arquivo_csv, fieldnames=cabecalho)
escritor.writeheader() # Escreve o cabeçalho no arquivo
for transacao in self._transacoes:
# Usamos vars() para converter os atributos do objeto em um dicionário
escritor.writerow(vars(transacao))
except IOError as e:
print(f"Erro ao salvar o arquivo: {e}")
def carregar_transacoes(self):
"""
Carrega as transações de um arquivo CSV para a lista.
"""
# Verifica se o arquivo existe antes de tentar abri-lo
if not os.path.exists(self._nome_arquivo):
print("Arquivo de transações não encontrado. Começando um novo.")
return # Sai da função se o arquivo não existe
try:
with open(self._nome_arquivo, 'r', newline='', encoding='utf-8') as arquivo_csv:
leitor = csv.DictReader(arquivo_csv)
self._transacoes = [] # Limpa a lista atual antes de carregar
for linha in leitor:
# Recria o objeto Transacao a partir dos dados do CSV
# Precisamos converter o valor de volta para float
transacao = Transacao(
descricao=linha['descricao'],
valor=float(linha['valor']),
tipo=linha['tipo']
)
self._transacoes.append(transacao)
print("Transações carregadas com sucesso!")
except FileNotFoundError:
# Esta exceção é um seguro extra, embora o os.path.exists já verifique
print("Arquivo de transações não encontrado. Começando um novo.")
except Exception as e:
print(f"Erro ao carregar o arquivo: {e}")
# Se o arquivo estiver corrompido, começamos do zero para evitar erros
self._transacoes = []





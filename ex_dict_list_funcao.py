# Exercicio para alunos de administracao e economia
# Evento Gastronomico realizado na faculdade para arrecadar fundos para uma entidade filantrópica
#Lista dos organizadores do evento
lst_organizadores = ['bento','mariana','saulo']
# Fornecedores do evento
dict_fornecedor = {
    0: {'nome': 'Pastel Frito', 'vendas': 3000},
    1: {'nome': 'Massa da Mama', 'vendas': 5000},
    2: {'nome': 'Pizza do Tio', 'vendas': 10000},
    3: {'nome': 'Rodizio Mineiro', 'vendas': 3900},
}
# Clientes que consumiram no evento
list_cliente = ['rafael','douglas','amanda','jorge','jeffri','carol','cristian',
 'leonardo','maria','luana','vanessa','jose','maria','bento','mariana','saulo',
 'glauco','ze','maria']
# Despesas do evento
locacao = 0.10 # 10% das vendas
limpeza = 700
seguranca = 800
outras_despesas = 500

# 1 - Calcular o total de vendas usando o for loop no dict
total_vendas = 0
for fornecedor in dict_fornecedor.values():
    total_vendas += fornecedor['vendas']

print("Total de vendas:", total_vendas)
       
# 2 - Criar um dicionario com o nome e valor
dict_professores = {
    'Gustavo': 1000,
    'Glauceny': 1000,
    'Zenaide': 1000,
    'Professor 4': 1000,
    'Professor 5': 1000
}

# 3 - Criar uma lista com os nomes dos professores  
lst_professores = list(dict_professores.keys())
print("Lista de professores:", lst_professores)

# 4 - Adicionar essa lista dos professores na lista de clientes
list_cliente.extend(lst_professores)

lst_professores += list_cliente

# 5 - Calcular quantas pessoas estiveram e a media de gasto por pessoa
quantidade_pessoas = len(set(list_cliente))
media_gasto_por_pessoa = total_vendas / quantidade_pessoas
print("Quantidade de pessoas:", quantidade_pessoas)
print("Média de gasto por pessoa:", media_gasto_por_pessoa)

# 6 - Encontrar quem foi o 10 consumidor e retire da lista
decimo_consumidor = list_cliente[9]

list_cliente.pop(9)
print("10º consumidor removido:", decimo_consumidor)

# 7 - Encontre o nome "bola" inserido incorretamente na lista e retire da lista
list_cliente.append("bola")
if "bola" in list_cliente:
    list_cliente.remove("bola")
print("Nome 'bola' removido da lista.")

# 8 - Verificar se todos os organizadores estao na lista
for nome in list_cliente:
    if nome in list_cliente:
        print(f"{nome} esta na lista")
    else:
        print(f"{nome} não está na lista")

# 9 - Tira-los da lista
for organizador in lst_organizadores:
    if organizador in list_cliente:
        list_cliente.remove(organizador)
print("Organizadores removidos da lista.")

# 10 - fazer uma funçao que calcule o lucro liquido do evento
def calcular_lucro_liquido(vendas, despesas):
    total_despesas = vendas * locacao + limpeza + seguranca + outras_despesas + sum(dict_professores.values())
    lucro_liquido = vendas - total_despesas
    return lucro_liquido
# entrada dos parametros sao as vendas e as despesas
# criar um pacote e gravar o modulo com essa funcao
# importe o pacote com a funcao
# chame a funcao
# execute o programa











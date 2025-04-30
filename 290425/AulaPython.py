# somatemp = 0
# lista_celsius = [10, 20, 40, 50]

# for i in lista_celsius:
#     somatemp += i 

# print(f"A soma das temperaturas é: {somatemp}")
# mediaf = somatemp / len(lista_celsius)
# print(f"Média dos Valores: {mediaf}")


# Ex. 3
# univ = []
# for k in range(5):
#     univ.append(str(input("Digite 5 universidades: ")))
# print(univ)


# Crie um algoritmo que permita ao usuário adicionar 10 itens e seus respectivos valores a duas listas (lista_produtos e lista_preco).
# Utilize uma estrutura de repetição while para solicitar as informações dos itens e seus valores. Em seguida, utilize uma estrutura de repetição for ou while para calcular o valor total da compra e o valor médio dos itens.

# lista_produtos = []
# lista_preco = []
# total = 0
# i = 0

# while i != 10:
#     lista_produtos.append(str(input("Digite o nome do produto: ")))
#     lista_preco.append(float(input("Digite o valor do produto: ")))
#     i += 1

# for k in lista_preco:
#     total += k

# media = total / len(lista_preco)
# print(f"O valor total é de R${total:.2f}")
# print(f"A média dos valores é: {media:.3f}")

#Declaramos 4 variaveis: duas listas(preço e produto), uma variavel para calculo do preço total e a variavel i para contagem do while.

#Declaramos o laço while que enquanto i for difente de 10, ele continua o loop. Utilizando o metodo append, é adicionado um input com o nome do produto a lista e em seguida é adiconado com o append o input do valor na lista do preço. O while é finalizado adicionando +1 a contagem do i.

#Declaramos o for sendo k o indice atual da lista de preços no qual o for esta rodando. Dentro do for é calculado uma soma dos total mais o valor do k, ou seja, o preço da lista de preços.

#A variavel media é o total dividido pelo tamanho da lista de preço.

#Para finalizar utilizamos o print para imprimir no console, com format string o valor total e a média dos valores. Formatando as variaveis para mostrar apenas duas casas decimais após a virgula.


# Crie um algoritmo para filtrar nomes curtos e longos.
# Inicialmente, solicite 10 nomes ao usuário e armazene-os em uma lista. Posteriormente, crie um filtro que permita separar os nomes com até 5 caracteres (inclusive) e os com mais de 5 caracteres, armazenando-os em duas listas: lista_nomes_curtos e lista_nomes_longos.
# Utilize uma estrutura de repetição for ou while: uma para solicitar os nomes ao usuário e outra para realizar o filtro.

# nomes = []
# lista_nomes_curtos = []
# lista_nomes_longos = []

# for i in range(10):
#     nomes.append(str(input("Digite o nome: ")))

# for nome in nomes:
#     if len(nome) > 5:
#         lista_nomes_longos.append(nome)
#     else:
#         lista_nomes_curtos.append(nome)

# print(f"Lista de nomes curtos: {lista_nomes_curtos}")
# print(f"Lista de nomes longos: {lista_nomes_longos}")

#Declaramos três variaveis como listas, sendo elas: nomes (irá coletar todos os nomes sem filtro), lista_nomes_curtos (que servirá para coletar apenas nomes com 5 ou menos letras), lista_nomes_longos (que servirá para coletar apenas nomes com mais de 5 letras).

#Declaramos um for como i para a quantidade de 10 nomes. Dentro deste laço serão solicitados 10 nomes que juntos do metodo append, já irá criar uma lista automaticamente.

#Declaramos outro for como nome dentro da quantidade de itens na variavel (nomes). Dentro do laço, aplicamos a condição de que se a quantidade de letras for maior do que 5, ele irá armazenar o nome dentro da lista de nomes longos, caso contrario ele irá armazenar dentro da lista de nomes curtos.

#Para finalizar, utilizamos o print para exibir no console ambas as listas já filtradas; sendo elas a Lista de nomes curtos (<5) e Lista de nomes longos (>5).

tarefas = []
prioridades = []
prioridades_tarefas = []
prioridade_alta =[]
prioridade_media =[]
prioridade_baixa =[]

for i in range(10):
    tarefas.append(str(input("Digite uma tarefa: ")))
    prioridades.append(str(input("Digite a prioridade da tarefa: ")))

for index, prioridade in enumerate(prioridades):
    if(prioridade == 'Alta'):
        prioridade_alta.append(f'{tarefas[index]} - {prioridades[index]}')
    elif(prioridade == 'Media'):
        prioridade_media.append(f'{tarefas[index]} - {prioridades[index]}')
    else:
        prioridade_baixa.append(f'{tarefas[index]} - {prioridades[index]}')

prioridades_tarefas = prioridade_alta + prioridade_media + prioridade_baixa
print(prioridades_tarefas)
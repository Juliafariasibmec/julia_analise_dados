"""
Lista de exercícios de revisão de Python
Disciplina: Programação para Análise de Dados
Nome do aluno: Julia Lima Farias 
Matrícula: 202301452538
Email: 202301452538@alunos.ibmec.edu.br

Orientações:
- Resolva cada exercício separadamente.
- Execute o arquivo após cada solução para conferir o resultado. (shift + enter)
- Use apenas os comandos básicos estudados em aula.
- Não use IA para resolver os exercícios, pois o objetivo é relembrar e praticar os conceitos aprendidos.
- Duvidas, mande um e-mail para o professor: laerte.takeuti@professores.ibmec.edu.br
- Se quiser mais exercícios, consulte o site: https://www.w3schools.com/python/default.asp
- Se quiser aulas em vídeo, consulte o canal: https://www.youtube.com/watch?v=S9uPNppGsGo&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6
"""
# ============================================================================
# 1. VARIÁVEIS — EXERCÍCIOS 1 A 10
# ============================================================================

# Exercício 1 — Dados pessoais
# Crie quatro variáveis para armazenar seu nome, sua idade, sua altura e se você
# é estudante. Mostre o valor e o tipo de cada variável usando print() e type().
nome = "Julia"
idade = 20
altura = 1.59
eh_estudante = True
# Exercício 2 — Saudação
# Peça ao usuário seu nome e sua cidade. Depois, mostre a mensagem:
# "Olá, <nome>! Você mora em <cidade>."
name = input("Digite o seu nome")
cidade = input("Digite a sua cidade")
print (f"O nome é {nome}  e a cidade é {cidade}")

# Exercício 3 — Soma de dois números
# Leia dois números inteiros usando input(), converta-os com int() e mostre
# a soma dos valores.
n1 = input("Digite um número inteiro")
n2 = input("Digite um número inteiro")
n1 = int(n1)
n2 = int(n2)
total = n1 + n2
print(total)

# Exercício 4 — Operações básicas
# Leia dois números e mostre o resultado da soma, subtração, multiplicação
# e divisão entre eles.
n1 = 10
n2 = 20
resultado_soma = n1 + n2
resultado_subtracao = n1 - n2
resultado_multiplicacao = n1 * n2
resultado_divisao = n1 / n2
print()

# Exercício 5 — Média de três notas
# Leia três notas do tipo float, calcule a média aritmética e mostre o resultado
# com duas casas decimais.
nota1 = 10.0
nota2 = 9.0
nota3 = 8.0
media = (nota1 + nota2 + nota3) / 3

import statistics as st
st. mean(nota1, nota2, nota3)


# Exercício 6 — Idade no futuro
# Peça a idade atual do usuário e informe quantos anos ele terá daqui a 10 anos.
n1 = input("Digite um número inteiro")
n2 = 10 
n1 = int(n1)
n2 = int(n2)
total = n1 + n2
print(total)


# Exercício 7 — Conversão de temperatura
# Leia uma temperatura em graus Celsius e converta para Fahrenheit.
# Fórmula: fahrenheit = (celsius * 9 / 5) + 32
celsius = 
fahrenheit = 

# Exercício 8 — Área de um retângulo
# Leia a largura e a altura de um retângulo. Calcule e mostre sua área.
# Fórmula: area = largura * altura


# Exercício 9 — Manipulação de texto
# Peça uma frase ao usuário e mostre:
# a) a frase em letras maiúsculas;
# b) a frase em letras minúsculas;
# c) a quantidade de caracteres da frase.


# Exercício 10 — Preço com desconto
# Leia o nome de um produto, seu preço e um percentual de desconto.
# Calcule e mostre o nome do produto, o valor do desconto e o preço final.


# ============================================================================
# 2. ESTRUTURA CONDICIONAL — EXERCÍCIOS 11 A 20
# ============================================================================

# Exercício 11 — Positivo, negativo ou zero
# Leia um número e informe se ele é positivo, negativo ou igual a zero.
numero = 10
if numero > 0:
    print ("o numero é positivo")
elif numero < 0: 
    print ("o numero é negativo")
else:
    print ("o numero é zero")




# Exercício 12 — Par ou ímpar
# Leia um número inteiro e informe se ele é par ou ímpar.
# Dica: use o operador de resto da divisão (%).
numero = 11
resto = numero % 2 # o % significa o resto da divisisão por 2
if resto == 0: """ continuar essa questão"""
    

# Exercício 13 — Aprovação
# Leia a média de um aluno. Mostre "Aprovado" se a média for maior ou igual
# a 7 e "Reprovado" caso contrário.


# Exercício 14 — Aprovação com recuperação
# Leia a média de um aluno e mostre:
# - "Aprovado", se a média for maior ou igual a 7;
# - "Recuperação", se a média estiver entre 5 e 6.9;
# - "Reprovado", se a média for menor que 5.


# Exercício 15 — Maior entre dois números
# Leia dois números e mostre qual é o maior. Se forem iguais, informe isso.


# Exercício 16 — Faixa etária
# Leia a idade de uma pessoa e classifique-a como:
# - "Criança": até 11 anos;
# - "Adolescente": de 12 a 17 anos;
# - "Adulto": de 18 a 59 anos;
# - "Idoso": 60 anos ou mais.


# Exercício 17 — Desconto na compra
# Leia o valor de uma compra. Se o valor for maior que R$ 100,00, aplique
# desconto de 10%. Caso contrário, mantenha o valor original. Mostre o total.


# Exercício 18 — Acesso ao sistema
# Leia o nome de usuário e a senha. Mostre "Acesso permitido" somente quando
# o usuário for "admin" e a senha for "1234". Caso contrário, mostre
# "Acesso negado".


# Exercício 19 — Número dentro do intervalo
# Leia um número e informe se ele está entre 10 e 50, incluindo os limites.
# Use os operadores and, >= e <=.


# Exercício 20 — Calculadora simples
# Leia dois números e uma operação (+, -, * ou /). Use if/elif/else para
# realizar a operação escolhida e mostrar o resultado. Não permita divisão
# por zero.


# ============================================================================
# 3. LISTAS — EXERCÍCIOS 21 A 30
# ============================================================================

# Exercício 21 — Criando uma lista
# Crie uma lista com as frutas "maçã", "banana", "laranja" e "uva".
# Mostre a lista completa.
frutas = ["maçã", "banana", "morango"]

# Exercício 22 — Acessando elementos
# Usando a lista abaixo, mostre o primeiro e o último elemento.
# cores = ["azul", "verde", "amarelo", "vermelho"]

cores = [ "azul", "verde", "amarelo", "vermelho"]
cores =[0] 
cores =[-1]

# Exercício 23 — Adicionando elementos
# Crie uma lista com três nomes. Peça outro nome ao usuário, adicione-o ao
# final da lista com append() e mostre a lista atualizada.


# Exercício 24 — Removendo elementos
# Dada a lista abaixo, remova "banana" com remove() e mostre o resultado.
# frutas = ["maçã", "banana", "laranja", "uva"]


# Exercício 25 — Alterando um elemento
# Dada a lista abaixo, substitua "laranja" por "abacaxi" usando seu índice.
# frutas = ["maçã", "banana", "laranja", "uva"]


# Exercício 26 — Tamanho e presença
# Dada a lista abaixo, mostre a quantidade de elementos e verifique se
# o número 30 pertence à lista.
# numeros = [10, 20, 30, 40, 50]


# Exercício 27 — Soma, maior e menor
# Dada a lista abaixo, mostre a soma, o maior valor e o menor valor usando
# sum(), max() e min().
# valores = [12, 5, 28, 9, 17]


# Exercício 28 — Ordenação
# Coloque a lista abaixo em ordem alfabética usando sort() e mostre o resultado.
# cidades = ["Curitiba", "Salvador", "Recife", "Goiânia", "Manaus"]


# Exercício 29 — Concatenação
# Una as duas listas abaixo em uma terceira lista e mostre o resultado.
# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6]


# Exercício 30 — Fatiamento
# Dada a lista abaixo, use fatiamento para mostrar:
# a) os três primeiros números;
# b) os três últimos números;
# c) os números do índice 2 ao índice 5.
# numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# ============================================================================
# 4. ESTRUTURAS DE REPETIÇÃO — EXERCÍCIOS 31 A 40 for loop
# ============================================================================

# Exercício 31 — Números de 1 a 10
# Use um laço for e range() para mostrar os números de 1 a 10.
for n in range(0,10):
    print(n)


# Exercício 32 — Números pares
# Use um laço for para mostrar apenas os números pares de 2 a 20.


# Exercício 33 — Percorrendo nomes
# Use um laço for para mostrar cada nome da lista abaixo em uma linha.
# nomes = ["Ana", "Bruno", "Carla", "Diego"]
nomes = ["Ana", "Bruno", "Carla", "Diego"]
for nome in nomes:
    print(nome)

# Exercício 34 — Quadrados
# Use um laço for para criar uma nova lista contendo o quadrado de cada número.
# numeros = [1, 2, 3, 4, 5]


# Exercício 35 — Soma com for
# Use um laço for e uma variável acumuladora para somar os valores abaixo.
# Não use a função sum().
# valores = [10, 20, 30, 40, 50]


# Exercício 36 — Contando aprovados
# Percorra a lista e conte quantas notas são maiores ou iguais a 7.
# notas = [8.0, 5.5, 7.0, 9.2, 4.0, 6.8]


# Exercício 37 — Contagem com while
# Use um laço while para mostrar os números de 1 a 10.


# Exercício 38 — Contagem regressiva
# Use um laço while para fazer uma contagem regressiva de 10 até 1.
# Ao terminar, mostre a mensagem "Fim!".


# Exercício 39 — Senha correta
# Peça uma senha ao usuário repetidamente usando while. O programa deve parar
# somente quando a senha digitada for "python123".


# Exercício 40 — Somando até zero
# Peça números inteiros ao usuário e some os valores digitados. Use while para
# continuar a leitura até que o usuário digite 0. Ao final, mostre a soma.


# ============================================================================
# 5. DICIONÁRIOS — EXERCÍCIOS 41 A 50
# ============================================================================

# Exercício 41 — Criando um dicionário
# Crie um dicionário chamado aluno com as chaves "nome", "idade" e "curso".
# Preencha com valores fictícios e mostre o dicionário completo.
aluno = {"nome": "laerte", 
        "idade":47,
        "curso": "programação para análise de dados"
        }

# Exercício 42 — Acessando valores
# Dado o dicionário abaixo, mostre separadamente o nome e o preço do produto.
# produto = {"nome": "Teclado", "preco": 150.0, "estoque": 8}
produto = {"nome": "Teclado", "preco": 150.0, "estoque": 8}


# Exercício 43 — Adicionando uma chave
# Adicione a chave "marca" ao dicionário abaixo e mostre o resultado.
# produto = {"nome": "Mouse", "preco": 80.0}


# Exercício 44 — Atualizando um valor
# Altere o estoque do produto abaixo para 15 unidades e mostre o dicionário.
# produto = {"nome": "Monitor", "preco": 900.0, "estoque": 5}


# Exercício 45 — Removendo uma chave
# Remova a chave "cor" do dicionário abaixo usando pop() e mostre o resultado.
# carro = {"marca": "Ford", "modelo": "Ka", "ano": 2020, "cor": "prata"}


# Exercício 46 — Verificando uma chave
# Verifique se a chave "telefone" existe no dicionário abaixo. Mostre uma
# mensagem informando o resultado.
# contato = {"nome": "Marina", "email": "marina@email.com"}


# Exercício 47 — Chaves e valores
# Use keys() para mostrar todas as chaves e values() para mostrar todos os
# valores do dicionário abaixo.
# capitais = {"Brasil": "Brasília", "Argentina": "Buenos Aires", "Chile": "Santiago"}


# Exercício 48 — Percorrendo um dicionário
# Use um laço for e items() para mostrar o nome de cada produto e seu preço.
# produtos = {"caderno": 25.0, "caneta": 4.5, "mochila": 120.0}


# Exercício 49 — Soma dos valores
# Calcule a soma de todas as quantidades do dicionário abaixo e mostre o total.
# estoque = {"notebook": 5, "mouse": 20, "teclado": 12, "monitor": 4}


# Exercício 50 — Frequência de palavras
# Percorra a lista abaixo e crie um dicionário que conte quantas vezes cada
# palavra aparece. Ao final, mostre o dicionário de frequências.
# palavras = ["python", "dados", "python", "lista", "dados", "python"]

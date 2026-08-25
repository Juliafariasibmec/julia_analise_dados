"""
Exercício desempenho alunos
Disciplina: Programação para Análise de Dados
Nome do aluno: Julia Lima Farias 
Matrícula: 202301452538
Email: 202301452538@alunos.ibmec.edu.br
""" 
#CSV É UM ARQUIVO TEXTO NORMAL SEPARADO POR , OU ;

#1. EXPLORAÇÃO INICIAL

import pandas as pd
df = pd.read_csv("alunos_desempenho.csv") #importo o dataframe para dentro do python
df.shape #sabemos que tem 150 linhas e 12 colunas

#1. O que representa cada linha do DataFrame?
df.head()
#2. O que representa cada coluna?
df.columns
#3. Qual é a unidade de análise desta base? Os registros dos alunos
"são as informações dos alunos"
#4. Quantas linhas existem? colo zero para pedir a primeira info
df.shape[0]
"150"
#5. Quantas colunas existem? coloco 1 para pedir a segunda informação
df.shape[1]
"12"
#6. O número de linhas representa exatamente o número de estudantes? Explique.
"Sim, pois cada aluno tem seu id único"
#7. Liste todas as variáveis da base.
df.info()
#8. Classifique as variáveis como identificadoras, categóricas ou quantitativas
"id e aluno são identificadoras"
"curso, participou_monitoria, trabalha_atualmente e período são categóricas"
"nota_final, faltas, horas_estudo_semana, participacao_aula, horas_trabalho_semana e horas_sono_noite são quantitativas"
#Começamos a explorar nossa base de dados. Esses comandos a AI faz, mas precisamos saber o que ela está fazendo por trás.

#2. ESTRUTURA E ORGANIZAÇÃO

#9. Quais variáveis são numéricas? para saber, seleciono as que estão com dtype object ou string
df.info()
#10. Quais variáveis aparecem como object?
"nenhuma"
#11. Por que aluno, curso e período não são variáveis numéricas?
"Por serem categóricos e não funcionarem como unidade de conta"
#12. A presença de dados faltantes pode alterar o tipo de uma coluna? Explique.
df.isna().sum()
"Aqui estamos pedindo os resultados nulos e depois somamos todos. Podemos ver 4 alunos não responderam o curso e o período tb"
"Não altera o tipo de uma coluna"
#13. Qual a vantagem de selecionar apenas as variáveis necessárias para uma determinada análise?
df.columns #Peço todas as colunas da lista, gravo em formato de lista e depois filtro (como deixei manualmente na linha abaixo)
col = ['aluno', 'curso', 'periodo', 'nota_final', 'faltas']
df_filtrado = df[col]

#3. QUALIDADE DOS DADOS

#14. Quais colunas possuem valores faltantes?
df.isna().sum()
#15. Quantos valores faltantes existem em cada coluna?
df.isna().sum()
#16. Qual variável possui maior quantidade de dados faltantes?
df.isna().sum().sort_values(ascending = false)
df.isna().sum().idxmax()
#17. Uma coluna com aproximadamente 3% de dados ausentes deveria ser automaticamente eliminada? Explique.
"Não, pois perderíamos outras informações que podem ser relevantes para a análise"
#18. Quantos alunos estão sem nota final?
df.isna().sum()
"6 alunos"
#19. Podemos utilizar esses estudantes para calcular a média das notas? Explique.
"Não, dessa maneira, a nota final dos alunos será alterada"
#20. Seria correto substituir todas as notas faltantes por zero? Justifique.
"Se eu coloco zero, abaixo a média. Se coloco a média, mantenho a nota. Estaríamos inferindo a nota final dos alunos. Dessa maneira, depende da situação"

#4. REGISTROS DUPLICADOS

#21. Existem linhas completamente duplicadas?
df.duplicated().sum()
#22. Por que duplicidades podem prejudicar uma análise?
"Por que você acrescenta uma informação já existente na análise"
#23. Por que seria um problema encontrar dois alunos diferentes com o mesmo id_aluno?
"Por que a função da coluna estaria inutilizada"

#5. ANÁLISE DESCRITIVA BÁSICA

#24. Qual é a média da nota final?
df["nota_final"].mean()
#25. Qual é a mediana da nota final?
df["nota_final"].median()
#26. Qual é o número médio de faltas?
df["faltas"].mean()
#27. Qual é o máximo de faltas registrado?
df["faltas"].max()
#28. Qual é a maior quantidade de horas de estudo semanal?
df.columns
df["horas_estudo_semana"].max()
#29. Algum valor parece estranho ou muito distante dos demais? Cite exemplos.
df["horas_estudo_semana"].describe()
#30. A média e a mediana da nota são semelhantes? O que essa comparação pode indicar?
"sim, são semelhantes e indicam que não existem muitos outliers"
#31. Compare a média, a mediana e o máximo da variável faltas. O que você observa?
df["faltas"].describe()
df["faltas"].median()

#6. IDENTIFICAÇÃO DE OUTLIERS

#32. Existem estudantes com quantidade de faltas muito superior aos demais?
df.boxplot(column="faltas")
#33. Existem valores muito elevados de horas de estudo?
df["horas_estudo_semana"].max()
#34. Existem jornadas de trabalho extremamente altas?
df["horas_trabalho_semana"].max()
#35. Esses valores necessariamente são erros? Explique.
"Não,pois indica as horas trabalhadas por cada aluno"
#36. Quantos possíveis outliers foram encontrados para faltas pelo método do intervalo interquartil?
df["faltas"].describe()
#37. Qual é o maior número de faltas?
df["faltas"].max() #45
#38. Um valor identificado como outlier deve ser automaticamente removido? Justifique.

# 7. LIMPEZA DOS DADOS

# 39. Por que é uma boa prática preservar o DataFrame original antes de realizar alterações?
# 40. Por que eliminar apenas registros sem nota_final pode ser mais adequado do que eliminar todas as linhas que possuam algum valor ausente?
# 41. Que informações poderiam ser perdidas ao remover toda linha que contenha algum dado faltante?
# 42. Por que a mediana pode ser preferível à média quando existem outliers?
# 43. Todo dado faltante deve ser preenchido? Explique.
# 44. Em que situações seria melhor manter um valor como ausente?

# 8. VARIÁVEIS CATEGÓRICAS
# 45. Existem valores faltantes nas variáveis categóricas?
# 46. Por que categorias como Administração, administracao, ADM e Administração com espaço ao final poderiam prejudicar a análise?

# 9. FILTROS

# 47. Quantos estudantes possuem nota inferior a 7?
filtro = df["nota_final"]<7
df[filtro] #87alunos com nota abaixo de sete
df_menor_7 = df[filtro][col]

# 48. Quantos estudantes possuem mais de 10 faltas?
filtro = df["faltas"]>10
col = ["aluno", "nota_final", "faltas"]
df[filtro][col]

# 49. Quantos estudantes possuem nota inferior a 7 e mais de 10 faltas?
filtro = (df["nota_final"]<7) & (df["faltas"]>10)
df_pior = df[filtro][col]

# 50. Todos os estudantes com nota baixa possuem muitas faltas?
df_menor_7.shape[0]
df_pior.shape[0] 
"Não, pois tem alunos com nota menor que 7 e com falta"

# 10. ORDENAÇÃO DOS DADOS

# 51. Quem são os cinco estudantes com maiores notas?
col=["alunos", "nota_final"]
df[col].sort_values(by= ["nota_final", "aluno"],ascending=False).head(5)
# 52. Os estudantes com menores notas possuem necessariamente muitas faltas
col=["alunos", "nota_final"]
df[col].sort_values(by= ["nota_final", "aluno"],ascending=False).head(10)

#11. ANÁLISE POR GRUPOS

# 53. Existe diferença relevante entre as médias dos cursos?
df.columns
df["curso"]
df.groupby("curso")["nota_final"].mean()
# 54. Qual período apresenta maior média?
df.groupby("periodo")["nota_final"].mean()
# 55. Estudantes que participaram da monitoria apresentam média maior?
df.groupby("participou_monitoria")["nota_final"].mean()
# 56. Podemos afirmar que a monitoria causou o aumento das notas? Explique.
"Não, por que causalidade não foi comprovada. Pode haver variáveis impactantes que não foram consideradas"
# 57. Existe diferença entre alunos que trabalham e alunos que não trabalham?
df.groupby("trabalha_atualmente")["nota_final"].mean()
# 58. Essa diferença, caso exista, é suficiente para estabelecer causalidade?
"Não"
# 59. Por que analisar somente a média pode ser insuficiente?
"pois os outliers podem afetar o resultado"

# 12. RELAÇÃO ENTRE FALTAS E NOTAS

# 60. A correlação entre faltas e nota final é positiva, negativa ou próxima de zero?
col=["nota_final", "faltas"]
df[col].corr()
# 61. O sinal da correlação está de acordo com a hipótese inicial?
"Sim"
# 62. Quanto mais próximo de -1 estiver o valor da correlação, o que isso significa?
"significa que é mais inversamente correlacionado"

# 13. HORAS DE ESTUDO E NOTA

# 63. Existe associação entre horas de estudo e nota?
col=["horas_estudo_semana","nota_final"]
df[col].corr()
# 64. A associação encontrada é positiva ou negativa?
'positiva. quanto mais estudo, maior nota'
# 65. Horas de estudo parecem ter relação com desempenho? Explique com base nos dados.
"Sim"

# 14. MATRIZ DE CORRELAÇÃO

# 66. Qual variável apresenta maior correlação positiva com nota_final?
df.corr(numeric_only=True).sort_values(["nota_final"])
# 67. Qual variável apresenta maior correlação negativa com nota_final?

# 68. Alguma correlação surpreendeu você? Explique.

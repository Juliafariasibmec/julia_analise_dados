"""
Docstring for ex_aluno_desempenho_merge
Lista de exercícios de revisão de Python
Disciplina: Programação para Análise de Dados
Nome do aluno: Julia Lima Farias 
Matrícula: 202301452538
Email: 202301452538@alunos.ibmec.edu.br
"""

import pandas as pd
df_localidade = pd.read_excel("alunos_localidade_carro_merge.xlsx")
df_alunos = pd.read_csv("alunos_desempenho.csv")
pd.merge(df_alunos, df_localidade, on= "id_aluno")

# 1. Quais variáveis existem na base de desempenho e quais existem na base complementar?
df_localidade.info()
df_alunos.info()
pd.merge(df_alunos, df_localidade, on= "id_aluno")
# 2. Qual variável deve ser utilizada como chave para realizar o merge?
pd.merge(df_alunos, df_localidade, on= "id_aluno", how= "left")
# 3. Por que id_aluno é uma chave mais segura do que o nome do estudante?
'O nome pode ser igual e confundir o restante dos dados. é mais seguro ter um id único, como matricula, cpf ou cefp infos numéricas'
# 4. Antes do merge, quantos registros existem em cada base?
df_localidade.shape
df_alunos.shape
"quando rodo cada um aparece: (150,7) e (150,12)"
# 5. Realize o merge utilizando id_aluno. Quantos estudantes existem na base resultante?
df = pd.merge(df_alunos, df_localidade, on= "id_aluno", how= "left")

# 6. Todos os estudantes foram associados corretamente? Como você verificou isso?
pd.merge(df_alunos, df_localidade, on= "id_aluno", how= "outer", indicator= True)

# 7. Existe algum estudante presente apenas em uma das bases? Se houver, como você identificaria esses casos?
'não há'

# 8. Qual tipo de merge é mais adequado para preservar todos os estudantes da base principal? Justifique.
"left"

import pandas as pd
df_localidades = pd.read_excel("alunos_localidade_carro_merge.xlsx")
df_alunos = pd.read_csv("alunos_desempenho.csv")
df_localidades.info()
df_alunos.info()
# Merge entre df_alunos e df_localidades (que tem cep)
df = pd.merge(df_alunos, df_localidades, on="id_aluno", how="left")
# Consulta da api viacep para consultar o endereco (atraves do cep)
import requests
ceps = df["cep"].unique()
dados_ceps = []
for cep in ceps:
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    dados = response.json()
    dados_ceps.append(dados)
    print(cep)
df_endereco = pd.DataFrame(dados_ceps)
# Consulta de latitude e longitude apartir dos enderecos
import requests
import pandas as pd
import time
enderecos = df_endereco["logradouro"].unique()
lista_enderecos = []
for endereco in enderecos:
    url = "https://https://brasilapi.com.br/"
    params = {
        "q": endereco,
        "format": "json",
        "limit": 1,
        "countrycodes": "br"
    }
    headers = {
        "User-Agent": "meu_projeto_geocoding/1.0"
    }
    response = requests.get(url, params=params, headers=headers)
    dados = response.json()
    if dados:
        latitude = float(dados[0]["lat"])
        longitude = float(dados[0]["lon"])
        lista_enderecos.append({
            "logradouro": endereco,
            "latitude": latitude,
            "longitude": longitude
        })
    time.sleep(1)
    print(endereco)
df_coordenadas = pd.DataFrame(lista_enderecos)
# Latitude e longitude do Ibmec
import requests
endereco_ibmec = "SIG Quadra 4, Brasília, DF, Brasil"
url = "https://nominatim.openstreetmap.org/search"
params = {
    "q": endereco_ibmec,
    "format": "json",
    "limit": 1,
    "countrycodes": "br"
}
headers = {"User-Agent": "meu_projeto_geocoding/1.0"}
response = requests.get(url, params=params, headers=headers)
dados_ibmec = response.json()
lat_ibmec = float(dados_ibmec[0]["lat"])
lon_ibmec = float(dados_ibmec[0]["lon"])
print(lat_ibmec, lon_ibmec)
# Calcula a distacia entre dois pontos (latitude e longitude)
from math import radians, sin, cos, sqrt, atan2
def calcular_distancia(lat1, lon1, lat2, lon2):
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    distancia = 6371 * c
    return distancia



import requests
endereco_ibmec= "SIG Quadra 4, Brasília, DF, Brasil"
url= "https://nominatim.openstreetmap.org/ui/search.html"
params = {
    "q" = endereco_ibmec,
    "format"= "json",
    "limit": 1,
    "countrycodes": "br"
}
headers = {"User.Agent"; "meu_projeto_geocoding/1.0"}
response = requests.get(url, params=params, headers=headers)
dados_ibmec = response.json()
lat_ibmec = float(dados_ibmec[0]["lat"])
lon_ibmec = float(dados[0]["lon"])
print(lat_ibmec, lon_ibmec)
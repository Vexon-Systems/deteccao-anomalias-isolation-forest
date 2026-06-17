import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest

# Carregamento

df = pd.read_csv("acessos_sistema.csv")

# Exploração

print(df.head())
print(df.info())
print(df.describe())

# Pré-processamento

scaler = StandardScaler()
X = scaler.fit_transform(df)

# Modelo

modelo = IsolationForest(
    contamination=0.10,
    random_state=42
)

df["anomalia"] = modelo.fit_predict(X)

# Mostrar anomalias

print(df[df["anomalia"]==-1])

# Gráfico 1

normal = df[df["anomalia"]==1]
anomalo = df[df["anomalia"]==-1]

plt.figure(figsize=(8,5))

plt.scatter(
    normal["duracao_sessao_min"],
    normal["quantidade_paginas_acessadas"],
    label="Normal"
)

plt.scatter(
    anomalo["duracao_sessao_min"],
    anomalo["quantidade_paginas_acessadas"],
    label="Anomalia"
)

plt.xlabel("Duração da Sessão")
plt.ylabel("Quantidade de Páginas")
plt.title("Detecção de Anomalias")

plt.legend()

plt.savefig("dispersao_anomalias.png")

plt.show()

# Gráfico 2

plt.figure(figsize=(10,5))

df.drop(columns=["anomalia"]).boxplot()

plt.title("Distribuição das Variáveis")

plt.savefig("boxplot_variaveis.png")

plt.show()

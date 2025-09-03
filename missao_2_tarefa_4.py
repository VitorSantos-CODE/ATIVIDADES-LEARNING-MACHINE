"Você é um analista de segurança. Sua missão é identificar transações fraudulentas (anomalias) em um conjunto de dados. Uma transação anômala geralmente está muito distante das outras."
"Use o mesmo KMeans para agrupar as transações. A transação que ficar isolada em seu próprio cluster é provavelmente a anomalia."

from sklearn.cluster import KMeans

# Dados: [valor_transacao, hora_do_dia (0-23)]
transacoes = np.array([
    [15.50, 14], [30.00, 10], [12.75, 11],
    [50.20, 19], [25.00, 9],
    [2500.00, 3] # Uma transação muito alta e de madrugada -> suspeita
])

# TODO: Crie um modelo KMeans para encontrar 2 grupos.
# A ideia é que as transações normais fiquem em um grupo e a anômala fique sozinha no outro.
modelo_anomalia = KMeans(n_clusters=2, random_state=42, n_init=10)


# TODO: Treine e preveja os clusters para os dados de transações.
clusters_transacoes = modelo_anomalia.fit_predict(transacoes)


print(f"Clusters para as transações: {clusters_transacoes}")
print("A transação anômala é aquela que está em um cluster isolado!")
print("Complete o código acima!")
print("-" * 50, "\n")

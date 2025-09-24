# K-Nearest Neighbors (KNN)
# Exercício: Aprovado ou Reprovado?
# Sua Tarefa: Crie um modelo KNN que classifica se um aluno foi aprovado (1) ou reprovado (0) com base em duas notas.

import numpy as np
from sklearn.neighbors import KNeighborsClassifier

# EXERCÍCIO - APROVADO OU REPROVADO?
print("\n--- 2.2: Exercício - Aprovado/Reprovado ---")
# X: [nota_prova_1, nota_prova_2]
notas_alunos = np.array([[8, 7], [5, 4], [9, 8], [4, 2], [7, 9], [3, 5]])
# y: 0=Reprovado, 1=Aprovado
situacao = np.array([1, 0, 1, 0, 1, 0])

# TODO: Crie uma instância do modelo KNeighborsClassifier com 3 vizinhos.
modelo_alunos = KNeighborsClassifier(n_neighbors=3)

# TODO: Treine o modelo com os dados dos alunos.
modelo_alunos.fit(notas_alunos, situacao)

# TODO: Preveja a situação de um aluno com notas 6 e 7.
aluno_novo = np.array([[6, 7]])
previsao_aluno = modelo_alunos.predict(aluno_novo)

resultado_aluno = "Aprovado" if previsao_aluno[0] == 1 else "Reprovado"
print(f"Um aluno com notas [6, 7] foi classificado como: {resultado_aluno}")

# MISSÃO 04 - VALOR 0,25

# REGRESSÃO LINEAR
# Exercício: Prever Pontuação em Jogo
# Sua Tarefa: Crie um modelo que prevê a pontuação final de um jogador com base no número de horas que ele jogou.

import numpy as np
from sklearn.linear_model import LinearRegression

# EXERCÍCIO - PREVER PONTUAÇÃO EM JOGO
print("\n--- 1.2: Exercício - Prever Pontuação ---")
# X: Horas jogadas
horas_jogadas = np.array([1, 3, 5, 8, 10]).reshape(-1, 1)
# y: Pontuação final (em milhares)
pontuacao_final = np.array([10, 25, 60, 90, 110])

# TODO: Crie uma instância do modelo LinearRegression.
modelo_pontuacao = LinearRegression()

# TODO: Treine o modelo com os dados de horas jogadas e pontuação.
modelo_pontuacao.fit(horas_jogadas, pontuacao_final)

# TODO: Preveja a pontuação para um jogador que jogou por 7 horas.
horas_novas = np.array([[7]])
pontuacao_prevista = modelo_pontuacao.predict(horas_novas)

print(f"Para 7 horas jogadas, a pontuação prevista é de {pontuacao_prevista[0]:.0f} mil pontos.")

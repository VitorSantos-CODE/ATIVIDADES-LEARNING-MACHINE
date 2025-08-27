# Criar um classificador de Previsão de Tempo de Entrega de Pizza - rode sem erros no VSCODE ###
# ------------------------------------------------------------------------------
#criar um modelo que prevê o tempo de entrega (em minutos) com base na distância (em km) e no número de pizzas no pedido.
# ------------------------------------------------------------------------------
import numpy as np
from sklearn.linear_model import LinearRegression

print("\n--- 1.2 Exercício para Alunos (Supervisionado) ---")

# Dados de Treino: [distancia_km, numero_de_pizzas]
dados_entregas = np.array([
    [5, 2],   # 5 km, 2 pizzas
    [2, 1],   # 2 km, 1 pizza
    [10, 4],  # 10 km, 4 pizzas
    [7, 3],   # 7 km, 3 pizzas
    [1, 1]    # 1 km, 1 pizza
])

# Rótulos: Tempo de entrega em minutos
tempos_entrega = np.array([30, 15, 55, 40, 10])

# TODO: Crie uma instância do modelo LinearRegression.
modelo_entrega = LinearRegression() 

# TODO: Treine o modelo usando os dados de entregas e os tempos.
modelo_entrega.fit(dados_entregas, tempos_entrega)

# TODO: Faça a previsão para um novo pedido: 8 km de distância e 2 pizzas.
pedido_novo = np.array([[8, 2]])
tempo_previsto = modelo_entrega.predict(pedido_novo)

print(f"Tempo de entrega previsto para o novo pedido: {tempo_previsto[0]:.2f} minutos")


# --- SOLUÇÃO COMENTADA DO EXERCÍCIO ---
# modelo_entrega = LinearRegression()
# modelo_entrega.fit(dados_entregas, tempos_entrega)
# pedido_novo = np.array([[8, 2]])
# tempo_previsto = modelo_entrega.predict(pedido_novo)
# print(f"SOLUÇÃO: Tempo de entrega previsto para o novo pedido: {tempo_previsto[0]:.2f} minutos")

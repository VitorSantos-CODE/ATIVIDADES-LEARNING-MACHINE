# Exercício para Alunos: Classificar Veículo
# Sua Tarefa: Crie um modelo KNN para classificar um veículo como 'Carro', 'Moto' ou 'Caminhão' com base no seu peso (em kg) e número de rodas.

from sklearn.neighbors import KNeighborsClassifier
import numpy as np

# PARTE 2.3: EXERCÍCIO - CLASSIFICAR VEÍCULO
print("\n--- 2.3: Exercício - Classificar Veículo ---")
# X: [peso_kg, numero_rodas]
dados_veiculos = np.array([[150, 2], [1500, 4], [8000, 6], [180, 2], [2000, 4], [10000, 8]])
# y: 0=Moto, 1=Carro, 2=Caminhão
tipo_veiculo = np.array([0, 1, 2, 0, 1, 2])

# TODO: Crie e treine um modelo KNN com 3 vizinhos para estes dados.
modelo_veiculo = KNeighborsClassifier(n_neighbors=3)
modelo_veiculo.fit(dados_veiculos, tipo_veiculo)

# TODO: Preveja o tipo de um veículo com 1800 kg e 4 rodas.
veiculo_novo = np.array([[1800, 4]])
previsao_veiculo = modelo_veiculo.predict(veiculo_novo)

mapa_veiculos = {0: 'Moto', 1: 'Carro', 2: 'Caminhão'}
resultado_veiculo = mapa_veiculos[previsao_veiculo[0]]
print(f"Um veículo de [1800 kg, 4 rodas] foi classificado como: {resultado_veiculo}")

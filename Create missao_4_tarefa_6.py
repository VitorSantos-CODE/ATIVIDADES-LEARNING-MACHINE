import numpy as np
from sklearn.tree import DecisionTreeClassifier

print("\n--- 3.3: Exercício - Diagnóstico Médico ---")

# X: [febre (0=Não, 1=Sim), tosse (0=Leve, 1=Forte)]
sintomas = np.array([[1, 1], [0, 0], [1, 0], [0, 1], [1, 1], [0, 0]])
# y: 0=Resfriado, 1=Gripe
diagnostico = np.array([1, 0, 0, 0, 1, 0])

# Crie e treine um modelo de árvore de decisão.
modelo_saude = DecisionTreeClassifier()
modelo_saude.fit(sintomas, diagnostico)

# Preveja o diagnóstico para um paciente com febre (1) e tosse leve (0).
novo_paciente = np.array([[1, 0]])
previsao_saude = modelo_saude.predict(novo_paciente)

mapa_diagnostico = {0: 'Resfriado', 1: 'Gripe'}
resultado_saude = mapa_diagnostico[previsao_saude[0]]
print(f"Diagnóstico para [Febre=Sim, Tosse=Leve]: {resultado_saude}")

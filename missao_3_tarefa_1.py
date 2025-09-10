### **Exercício 1: O Corredor Simples**

### **Cenário:** O exercício mais básico possível. Um agente está em um corredor de 7 posições (0 a 6) e quer chegar ao final. Ele só pode se mover para frente.

### **Sua Missão:** Implementar a lógica de movimento e a recompensa final.

import numpy as np
import time

print("\n--- Exercício 1: O Corredor Simples ---")
posicao_agente = 0
objetivo = 6
recompensa_total = 0

for passo in range(10):
    print(f"Passo {passo + 1}: Posição atual = {posicao_agente}")
    posicao_agente += 1
    if posicao_agente == objetivo+1:
      recompensa_total += 10
      break;
    else:
      recompensa_total -= 1
    
    # Neste cenário simples, a única ação possível é 'avançar'.
    # TODO 1: Atualize a 'posicao_agente' para que ele avance 1 passo.
    
    
    # TODO 2: Verifique se o agente alcançou o 'objetivo'.
    # Se sim, adicione 10 pontos à 'recompensa_total' e use 'break' para parar.
    
    
    # Se não chegou, ele perde 1 ponto de 'recompensa_total' pelo esforço.
    
    
    time.sleep(0.5)

print(f"Simulação finalizada! Recompensa total: {recompensa_total}")

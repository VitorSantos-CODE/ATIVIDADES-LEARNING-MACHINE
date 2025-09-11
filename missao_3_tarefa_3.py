# Exercício 3: O Caminho Perigoso
# Cenário: O mesmo corredor do exercício 2, mas agora existe um buraco na posição 2. Se o agente cair no buraco, ele perde 50 pontos e o episódio acaba.
# Sua Missão: Adicionar a lógica do buraco, que é uma condição de término negativa.

# Exercício 3: O Caminho Perigoso
import numpy as np

print("\n--- Exercício 3: O Caminho Perigoso ---")
posicao_agente = 5
objetivo = 9
buraco = 2
recompensa_total = 0

for passo in range(15):
    acao = np.random.choice(['esquerda', 'direita'])
    print(f"Passo {passo + 1}: Posição={posicao_agente}, Ação='{acao}'")
    
    if acao == 'direita': posicao_agente += 1
    else: posicao_agente -= 1
    posicao_agente = np.clip(posicao_agente, 0, 9) # np.clip faz o mesmo que max/min

    # TODO 1: Crie uma estrutura if/elif/else para as recompensas.
    # - Se a posição for igual ao 'objetivo': recompensa +20, fim.
    # - Se a posição for igual ao 'buraco': recompensa -50, fim.
    # - Senão: recompensa -1.
    
    if posicao_agente == objetivo:
     recompensa_total += 20
     break;
    elif posicao_agente == buraco:
     recompensa_total -= 50
     break;
    else:
      recompensa_total -= 1

    time.sleep(0.5)

print(f"Simulação finalizada! Posição final: {posicao_agente}, Recompensa: {recompensa_total}")

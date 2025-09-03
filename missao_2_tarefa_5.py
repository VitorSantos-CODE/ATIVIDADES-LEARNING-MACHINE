# EXERCICIO FINAL DA MISSÃO 2 - APRENDIZADO POR REFORÇO

# Imagine que você está ensinando um Doguinho a buscar um petisco. Você não escreve um manual de instruções para ele. Em vez disso, o processo é interativo:

# 1 - O cachorro (o Agente) está em um ambiente (a sala). Ele decide fazer uma Ação (andar para frente).
# 2 - Você dá um Feedback (a Recompensa). Se ele chegou mais perto do petisco, você diz "Bom garoto!" (recompensa positiva).
# 3 - Se ele foi para longe, você não diz nada (recompensa neutra ou negativa, como o custo de energia).
# 4 - O cachorro recebe esse feedback e atualiza o seu "entendimento" sobre qual ação é boa naquela situação.
# 5 - Ele repete esse ciclo de Ação -> Recompensa várias vezes. Depois de muitas tentativas e erros, o cachorro aprende a sequência de ações ideal para conseguir o petisco da forma mais rápida possível.

# O Aprendizado por Reforço é exatamente isso: um método de Machine Learning onde um agente aprende a tomar decisões em um ambiente para maximizar uma recompensa total ao longo do tempo.

# Exercício: Agente Comilão
# Cenário: Nosso agente está em uma linha com 5 posições (0, 1, 2, 3, 4).
# O Agente: Um programa que só pode se mover para a 'direita'.
# O Ambiente: O caminho de 5 posições.
# O Objetivo: Chegar na Comida, que está na posição 4.

# Regras de Recompensa:
# +20 pontos: Se o agente chegar na Comida.
# -1 ponto: Para cada passo que o agente der (representa o custo de energia).

# Sua Missão: Você vai preencher a lógica do ambiente. O agente sempre tentará se mover para a 'direita'. Você precisa atualizar a posição dele, verificar se ele alcançou a comida e calcular a recompensa a cada passo.

# ==============================================================================
# EXERCÍCIO 5 - APRENDIZADO POR REFORÇO: O PERSONAGEM COMILÃO
# Objetivo: Entender o loop básico de interação do RL (Ação -> Recompensa).
# ==============================================================================

import time
# --- CONFIGURAÇÃO DO AMBIENTE ---
POSICAO_INICIAL = 0
POSICAO_COMIDA = 4
recompensa_total = 0

# O agente começa na posição inicial.
posicao_agente = POSICAO_INICIAL

print("--- Iniciando a Simulação do PERSONAGEM COMILÃOo ---")
print(f"O agente começa na posição {posicao_agente} e quer chegar na comida na posição {POSICAO_COMIDA}.")
print("-" * 30)

# O agente tem no máximo 10 passos para tentar chegar à comida.
for passo in range(10):
    print(f"Passo {passo + 1}:")
    
# O agente sempre toma a mesma AÇÃO: mover para a 'direita'.
    acao_agente = 'direita'
    print(f"   -> Ação do Agente: '{acao_agente}'")
    
# ======================================================================
# CONSTRUA A LÓGICA DO AMBIENTE
# ======================================================================
    
# 1. ATUALIZE A POSIÇÃO DO AGENTE
    #    Como a ação é sempre 'direita', simplesmente incrementamos a posição.
    posicao_agente = posicao_agente + 1
        
# 2. CALCULE A RECOMPENSA DO PASSO
#    Verificamos primeiro a condição de vitória.
    if posicao_agente == POSICAO_COMIDA:
        # Se chegou, recebe a recompensa positiva.
        recompensa_do_passo = 20
    else:
        # Se ainda não chegou, recebe a penalidade de movimento.
        recompensa_do_passo = -1

# 3. ATUALIZE A RECOMPENSA TOTAL
#    Acumulamos a recompensa do passo na variável total.
    recompensa_total = recompensa_total + recompensa_do_passo
        
# Exibe o resultado do passo
    print(f"   <- Resposta do Ambiente: Nova Posição={posicao_agente}, Recompensa={recompensa_do_passo}")
        
# 4. VERIFIQUE SE O JOGO TERMINOU
#    Se a condição de vitória foi atingida, paramos a simulação.
    if posicao_agente == POSICAO_COMIDA:
        print("\nO personagem encontrou a comida!")
        break
    
# Pausa para visualização
time.sleep(1)

print("-" * 30)
print(f"Simulação Finalizada! Recompensa total acumulada: {recompensa_total}")
missao_2_tarefa_3.py

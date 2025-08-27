## TAREFA 1 :  Treine o modelo abaixo colocando mais 4 conjuntos de dados e rode sem erros no VSCODE - Faça teste após o treinamento ###

import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Função de pré-processamento
def limpar_texto(texto):
    texto = texto.lower()  # Converte para minúsculas
    texto = re.sub(r'[^\w\s]', '', texto)  # Remove pontuação
    texto = re.sub(r'\d+', '', texto)  # Remove números
    texto = texto.strip()  # Remove espaços extras
    return texto

# 1. Conjunto de dados (mensagens + rótulos)
mensagens = [
    "Quero fazer um pedido",
    "Preciso falar com o suporte",
    "Quais promoções vocês têm hoje?",
    "Qual o horário de funcionamento?",
    "Meu produto veio com defeito",
    "Posso pagar com cartão de crédito?",
    "Quanto custa a pizza?",
    "Quais as promoções da semana?",
    "Quais sabores vocês tem?",
    "Quero cancelar meu pedido."
]
rotulos = ["pedido", "suporte", "promoção", "informação", "suporte", "pagamento", "valores", "promoção", "informação", "suporte"]

# 2. Pré-processamento das mensagens
mensagens_limpas = [limpar_texto(m) for m in mensagens]

# 3. Vetorização
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(mensagens_limpas)

# 4. Treinamento do modelo
modelo = MultinomialNB()
modelo.fit(X, rotulos)

# 5. Interação com o usuário
while True:
    nova_mensagem = input("\nDigite uma mensagem (ou 'sair' para encerrar): ")
    if nova_mensagem.lower() == "sair":
        break
    nova_mensagem_limpa = limpar_texto(nova_mensagem)
    X_novo = vectorizer.transform([nova_mensagem_limpa])
    predicao = modelo.predict(X_novo)
    print(f"Intenção prevista: {predicao[0]}")

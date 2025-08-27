### TAREFA 2 :  Criar um classificador de mensagens para um bot de atendimento acadêmico - rode sem erros no VSCODE ###

# Criar um classificador de mensagens para um bot de atendimento acadêmico.
# Instruções:
# 1. Crie uma lista de frases (ex: dúvidas sobre matrícula, notas, eventos, biblioteca)
# 2. Crie a lista de rótulos correspondentes
# 3. Vetorize as frases com CountVectorizer
# 4. Treine um modelo Naive Bayes ou outro de sua escolha
# 5. Teste com uma nova frase e imprima o resultado

# início código
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

def limpar_texto(texto):
    texto = texto.lower()  # Converte para minúsculas
    texto = re.sub(r'[^\w\s]', '', texto)  # Remove pontuação
    texto = re.sub(r'\d+', '', texto)  # Remove números
    texto = texto.strip()  # Remove espaços extras
    return texto


# 1. Dataset
frases = [
    "Como faço para me matricular?",
    "Quando saem as notas do semestre?",
    "Onde vejo o calendário acadêmico?",
    "Qual o horário de funcionamento da biblioteca?",
    "Preciso de ajuda com a minha senha do portal do aluno.",
    "Como posso solicitar um atestado de matrícula?",
    "Qual a programação dos próximos eventos da faculdade?",
    "Não recebi meu boleto",
    "Posso trancar minha matrícula? Como funciona?",
    "Como entro em contato com a coordenação do meu curso?"
]
rotulos = ["matricula", "notas", "calendario", "financeiro", "suporte", "matricula", "calendario", "financeiro", "suporte", "suporte"]
  


# 2. Vetorização
mensagens_limpas = [limpar_texto(m) for m in frases]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(mensagens_limpas)

# 3. Modelo
modelo = MultinomialNB()
modelo.fit(X, rotulos)

# 4. Previsão
while True:
    nova_mensagem = input("\nDigite uma mensagem (ou 'sair' para encerrar): ")
    if nova_mensagem.lower() == "sair":
        break
    nova_mensagem_limpa = limpar_texto(nova_mensagem)
    X_novo = vectorizer.transform([nova_mensagem_limpa])
    predicao = modelo.predict(X_novo)
    print(f"Intenção prevista: {predicao[0]}")

# TAREFA 5 : Agrupar frases de um chatbot de turismo - rode sem erros no VSCODE
# 1. Crie uma lista de frases sobre passagens, hospedagem, passeios, restaurantes
# 2. Vetorize as frases
# 3. Use KMeans com número de clusters à sua escolha
# 4. Imprima a qual cluster cada frase pertence

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans

# 1. Dataset
frases = ["Quais são os melhores voos para Embu Guaçu?",
"Poderia me indicar hotéis ou pousadas em São Paulo?",
"Onde posso encontrar pacotes de passeios para Disney?",
"Que restaurantes vocês recomendam para experimentar a culinária local?",
"Há alguma promoção em passagens aéreas para a próxima temporada?",
"Como faço para reservar um tour guiado pelo centro histórico?",
"Quais são as opções de hospedagem mais econômicas?",
"Podem me sugerir restaurantes com vista para o mar?",
"Preciso de informações sobre horários de ônibus ou trem para Bahia.",
"Quais são os passeios imperdíveis para quem viaja com crianças?"
]

# 2. Vetorização
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(frases)

# 3. Modelo
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
kmeans.fit(X)

# 4. Saída
print("\nAgrupamento de mensagens:")
for i, msg in enumerate(frases):
    print(f"'{msg}' => Cluster {kmeans.labels_[i]}")

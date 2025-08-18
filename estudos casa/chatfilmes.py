import requests
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

api_key ='8d90b1cc294cc2c83d72439b80645cde'
analyzer= SentimentIntensityAnalyzer()

def suggest_movies():
    phrase  = input("Como voce está se sentindo hoje ? : ")
    emotion= analyzer.polarity_scores(phrase)['compound']

    print(emotion)
    
    if emotion <= -0.5:
        genre=18  # Drama
    elif emotion <0:
        genre=35  # Comedy
    elif emotion <0.5:
        genre=10749  # Romance
    else:
        genre=27  # horror
    url= f'https://api.themoviedb.org/3/discover/movie?api_key={api_key}&with_genres={genre}&sort_by=popularity.desc'
    response = requests.get(url).json()
    if response['results']:
        titles=[result['title'] for result in response['results'][:3]]
        print("recomendações de filmes: ")
        for title in titles:
            print(f"- {title}")
    else:
            print("Desculpe, não encontrei recomendações de filmes no momento.")


suggest_movies()

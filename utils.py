import requests 
from textblob import TextBlob

def get_news_articles(query):
    """
    Fetches news articles using NewsAPI.
    Returns a list of dictionaries containing title, summary, and URL.
    """
    API_KEY = "f804905478b34ede96743c3f80d11df3"  # Replace with your API key
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={API_KEY}"

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        articles = []

        for item in data.get("articles", [])[:10]:  # Get the first 10 articles
            articles.append({
                "title": item["title"],
                "summary": item["description"] or "No summary available",
                "url": item["url"]
            })

        return articles

    except requests.exceptions.RequestException as e:
        print("Error fetching news:", e)
        return []

def analyze_sentiment(text):
    """
    Performs sentiment analysis on the given text.
    Returns 'Positive', 'Negative', or 'Neutral'.
    """
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity  # Polarity score (-1 to 1)

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

import requests 
from textblob import TextBlob
from collections import Counter

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

def compare_sentiments(articles):
    """
    Performs comparative sentiment analysis and generates insights.
    """
    sentiment_counts = {"Positive": 0, "Negative": 0, "Neutral": 0}
    sentiment_groups = {"Positive": [], "Negative": [], "Neutral": []}

    for article in articles:
        sentiment = analyze_sentiment(article["summary"])
        sentiment_counts[sentiment] += 1
        sentiment_groups[sentiment].append(article)

    # Identify dominant sentiment
    dominant_sentiment = max(sentiment_counts, key=sentiment_counts.get)

    # Extract topics from positive and negative news
    positive_topics = Counter()
    negative_topics = Counter()
    # Extract common words/themes from positive and negative news
    positive_words = Counter()
    negative_words = Counter()

    for article in sentiment_groups["Positive"]:
        positive_topics.update(article["title"].split())

    for article in sentiment_groups["Negative"]:
        negative_topics.update(article["title"].split())

    # Identify most common topics in each sentiment group
    top_positive_topics = [word for word, count in positive_words.most_common(5)]
    top_negative_topics = [word for word, count in negative_words.most_common(5)]

    # Find common and unique topics
    common_topics = list(set(positive_topics.keys()) & set(negative_topics.keys()))
    unique_positive_topics = list(set(positive_topics.keys()) - set(negative_topics.keys()))
    unique_negative_topics = list(set(negative_topics.keys()) - set(positive_topics.keys()))

    # Generate insights based on sentiment distribution and trends
    insights = []

    if sentiment_counts["Positive"] > sentiment_counts["Negative"]:
        insights.append("The company's news coverage is mostly positive, reflecting strong market confidence.")
        if top_positive_topics:
            insights.append(f"Key positive themes in recent news include: {', '.join(top_positive_topics)}.")
    elif sentiment_counts["Negative"] > sentiment_counts["Positive"]:
        insights.append("The company is facing more negative news coverage, indicating potential challenges or controversies.")
        if top_negative_topics:
            insights.append(f"Key negative themes in recent news include: {', '.join(top_negative_topics)}.")
    else:
        insights.append("The company's news coverage is balanced, with equal amounts of positive and negative sentiment.")

    # Comparative Analysis: Identify Contrasting News Trends
    if sentiment_groups["Positive"] and sentiment_groups["Negative"]:
        first_positive_title = sentiment_groups["Positive"][0]["title"]
        first_negative_title = sentiment_groups["Negative"][0]["title"]

        insights.append(f"Example contrast: '{first_positive_title}' focuses on company success, whereas '{first_negative_title}' highlights a challenge.")

    # Debugging: Print all insights to verify correctness
    print("\n🔍 DEBUG: Generated Insights")
    for i, insight in enumerate(insights, 1):
        print(f"{i}. {insight}")

    return {
        "Sentiment Distribution": sentiment_counts,
        "Dominant Sentiment": dominant_sentiment,
        "Insights": insights
    }
    


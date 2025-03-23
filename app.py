from utils import get_news_articles, analyze_sentiment

if __name__ == "__main__":
    company_name = input("Enter company name: ")
    news = get_news_articles(company_name)

    for i, article in enumerate(news, 1):
        sentiment = analyze_sentiment(article['summary'])
        print(f"{i}. {article['title']}")
        print(f"   Sentiment: {sentiment}")
        print(f"   {article['summary']}")
        print(f"   {article['url']}\n")
 

from utils import get_news_articles, analyze_sentiment, compare_sentiments

if __name__ == "__main__":
    company_name = input("Enter company name: ")
    news = get_news_articles(company_name)

    if not news:
        print("No news articles found.")
    else:
        print("\nNews Articles with Sentiment Analysis:\n")
        for i, article in enumerate(news, 1):
            sentiment = analyze_sentiment(article["summary"])
            print(f"{i}. {article['title']}")
            print(f"   Sentiment: {sentiment}")
            print(f"   {article['summary']}")
            print(f"   {article['url']}\n")

        # Perform comparative sentiment analysis
        sentiment_summary = compare_sentiments(news)

        print("\nComparative Sentiment Analysis Report:")
        print(f"Sentiment Distribution: {sentiment_summary['Sentiment Distribution']}")
        print(f"Dominant Sentiment: {sentiment_summary['Dominant Sentiment']}")
        
        print("\nKey Insights:")
        final_sentiment = ""
        
        for insight in sentiment_summary["Insights"]:
            print(f"- {insight}")  # Print all insights properly
            final_sentiment += insight + " "  # Ensure all insights are combined
 

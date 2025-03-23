import streamlit as st
from utils import get_news_articles, analyze_sentiment, compare_sentiments, generate_tts

# Step 1: Set up the Streamlit app
st.title("News Summarization and Sentiment Analysis")
st.write("Enter a company name to get the latest news and sentiment analysis.")

# Step 2: Get user input
company_name = st.text_input("Enter a company name:")

if company_name:
    # Fetch News Articles
    st.subheader(f"News Articles about {company_name}:")
    news = get_news_articles(company_name)
    
    if news:
        for i, article in enumerate(news, 1):
            sentiment = analyze_sentiment(article["summary"])
            st.write(f"{i}. **{article['title']}**")
            st.write(f"   Sentiment: {sentiment}")
            st.write(f"   {article['summary']}")
            st.write(f"   [Read Full Article]({article['url']})")
            st.markdown("---")
        
        # Perform Comparative Sentiment Analysis
        sentiment_summary = compare_sentiments(news, company_name)

        # Display Sentiment Distribution and Insights
        st.subheader(f"Comparative Sentiment Analysis for {company_name}")
        st.write(f"Sentiment Distribution: {sentiment_summary['Sentiment Distribution']}")
        st.write(f"Dominant Sentiment: {sentiment_summary['Dominant Sentiment']}")
        
        st.write("### Key Insights:")
        for insight in sentiment_summary["Insights"]:
            st.write(f"- {insight}")
        
        # Button to Generate TTS
        if st.button("Play audio for Insights"):
            final_sentiment = " ".join(sentiment_summary["Insights"])
            generate_tts(final_sentiment, "final_sentiment.mp3")
            st.audio("final_sentiment.mp3")  # Display the generated audio file for playback
            st.success("Hindi audio generated successfully!")
    else:
        st.error("No news articles found.")


import streamlit as st
import requests

# Set the title of the app
st.title("News Summarization APP 📰")

# Input for company name
company_name = st.text_input("Enter a company name", "")

if st.button("Analyze Sentiment"):
    if company_name:
        # Call the backend API to fetch news
        api_url = f"https://news-summarizer.onrender.com/compare-news?company={company_name}"
        
        try:
            response = requests.get(api_url)
            if response.status_code == 200:
                data = response.json()
              
                # Display sentiment distribution
                st.subheader("Sentiment Distribution")
                st.json(data["Sentiment Distribution"])

                # Show insights
                st.subheader("Key Insights")
                for insight in data["Insights"]:
                    st.write(f"- {insight}")

                # Play Hindi audio
                st.audio("final_sentiment.mp3", format="audio/mp3")
            
            else:
                st.error("Failed to fetch data. Please try again.")
        
        except Exception as e:
            st.error(f"Error: {e}")
    
    else:
        st.warning("Please enter a company name.")

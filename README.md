# 📰 News Summarization and Sentiment Analysis Application

## 📖 Overview
This project is a web-based application that extracts key details from multiple news articles related to a given company, performs sentiment analysis, conducts a comparative analysis, and generates a text-to-speech (TTS) output in Hindi.

## 🛠️ Project Setup
### Prerequisites
- Python 3.7+
- Install the required libraries:
  ```bash
  pip install -r requirements.txt
  ```

### Running the Application
1. **Clone the repository**:
   ```bash
   git clone https://github.com/Robbin808/News_Summarizer.git
   cd <repository-directory>
   ```
2. **Run the Flask API**:
   ```bash
   python api.py
   ```
3. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

## 🧠 Model Details
### Summarization
- The summarization model extracts key details from news articles using BeautifulSoup for web scraping.

### Sentiment Analysis
- Sentiment analysis is performed using TextBlob to categorize the sentiment as Positive, Negative, or Neutral.

### Text-to-Speech (TTS)
- The TTS model uses Google Translator to translate text to Hindi and gTTS to convert the translated text to speech.

## 🌐 API Development
### Endpoints
- **`/fetch-news`**: Fetches news articles related to a given company.
- **`/analyze-sentiment`**: Analyzes the sentiment of the fetched news articles.
- **`/compare-news`**: Compares the sentiment across the fetched news articles.
- **`/generate-tts`**: Generates a text-to-speech (TTS) output for the provided text.

### Accessing APIs
- Use tools like Postman to test the APIs. Provide the company name as a query parameter.

## 🔗 API Usage
### Third-Party APIs
- **NewsAPI**: Used to fetch news articles.
  - **API Key**: Store the API key in an environment variable.

## ⚠️ Assumptions & Limitations
- The application assumes that the NewsAPI will return relevant articles for the given company name.
- The sentiment analysis is based on the summary of the articles and may not reflect the full content.
- The TTS output is generated in Hindi and may have limitations in pronunciation and accuracy.

## 🚀 Deployment
- The application is deployed on Hugging Face Spaces. Deployment Link

## 🏁 Conclusion
This project provides a comprehensive solution for news summarization, sentiment analysis, and text-to-speech conversion. It offers valuable insights into the company's news coverage and presents the information in an accessible format.

```

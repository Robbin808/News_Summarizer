# 📰 News Summarization and Sentiment Analysis Application

## 📖 Overview
This project is a web-based application that extracts key details from multiple news articles related to a given company, performs sentiment analysis, conducts a comparative analysis, and generates a text-to-speech (TTS) output in Hindi.


![68747470733a2f2f692e7974696d672e636f6d2f76692f39506f4b656c6c4e7242632f6d617872657364656661756c742e6a7067](https://github.com/user-attachments/assets/454c6699-7b60-484a-a2f6-21f54d513958)


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
   cd Robbin808/News_Summarizer
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
- The application is deployed on Hugging Face Spaces. https://huggingface.co/spaces/karthik808/News_Summarizer
- ✅ The app will open in your browser at http://localhost:8501
  

## 🖼️ Snapshots:
  
![Screenshot (91)](https://github.com/user-attachments/assets/1cdb18d6-d2a0-4ee8-a423-a17fc95f1202)


![Screenshot (92)](https://github.com/user-attachments/assets/b7501dc5-6e1f-4582-9970-4641ca422ad3)



## 🙌 Acknowledgments

-Thanks to:

**NewsAPI** :for providing real-time news data.

**Streamlit** :for an interactive UI.

**Google Translator** :API for Hindi translation.

## 📩 Contact

💡 If you have any questions or feedback, feel free to reach out!

-📧 Email: karthikbrinfpro@gmail.com

-🔗 GitHub: https://github.com/Robbin808

## 🏁 Conclusion
This project provides a comprehensive solution for news summarization, sentiment analysis, and text-to-speech conversion. It offers valuable insights into the company's news coverage and presents the information in an accessible format.

```

**News Summarization and Sentiment Analysis App**


Project Overview

This web-based application extracts key details from multiple news articles related to a given company, performs sentiment analysis, conducts a comparative analysis, and generates a text-to-speech (TTS) output in Hindi. The tool allows users to input a company name and receive a structured sentiment report along with an audio output.

FEATURES:

News Extraction: Fetches at least 10 news articles related to the given company, including the title, summary, and relevant metadata.

Sentiment Analysis: Performs sentiment analysis (Positive, Negative, Neutral) on the article content.

Comparative Analysis: Provides insights into how the company's news coverage varies across different articles.

Text-to-Speech (TTS): Converts the summarized content into Hindi speech.

User Interface: Simple web-based interface developed using Streamlit or Gradio.

TECHNOLOGIES USED:

News Extraction: BeautifulSoup (bs4)

Sentiment Analysis: TextBlob

Text-to-Speech: gTTS (Google Text-to-Speech)

Translation: Google Translator (deep_translator)

Web Framework: Streamlit 

Version Control: Git, GitHub

Installation
Clone the Repository
To get started with the project, first clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/News_Summarizer.git
Install Dependencies
You need to install the required dependencies. Use the following command to install them:

bash
Copy
Edit
pip install -r requirements.txt
Run the Application
To start the application, run:

bash
Copy
Edit
streamlit run app.py
API Setup (Optional)
The application uses APIs for the frontend and backend communication. Ensure that the API is properly set up if needed.

File Structure
graphql
Copy
Edit
News_Summarizer/
│
├── app.py                  # Main script for Streamlit web app
├── requirements.txt        # List of project dependencies
├── utils.py                # Utility functions (e.g., news extraction, sentiment analysis)
├── api.py                  # API support for communication between frontend and backend
└── README.txt              # Project documentation
API Usage
The communication between the frontend and backend is managed via APIs. Use Postman or other API testing tools to check the API endpoints. Make sure to follow the API documentation provided in api.py to interact with the backend.

Deployment
The app is deployed on Hugging Face Spaces. You can access the deployed app using the following link: https://huggingface.co/spaces/karthik808/News_Summarizer

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Thanks to Hugging Face for hosting the space.

Thanks to the authors of BeautifulSoup, TextBlob, gTTS, and GoogleTranslator for their open-source libraries.

 

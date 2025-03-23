from flask import Flask, request, jsonify,send_file
from utils import get_news_articles, analyze_sentiment, compare_sentiments,generate_tts

app = Flask(__name__)

# Enable CORS for frontend requests
from flask_cors import CORS
CORS(app)

@app.route("/")
def home():
    return jsonify({"message": "Welcome to the News Summarization API!"})

# 1️ Fetch News Articles API
@app.route("/fetch-news", methods=["GET"])
def fetch_news():
    company_name = request.args.get("company")
    
    if not company_name:
        return jsonify({"error": "Please provide a company name in the request URL."}), 400

    news = get_news_articles(company_name)
    return jsonify({"company": company_name, "articles": news})

# 2️ Sentiment Analysis API
@app.route("/analyze-sentiment", methods=["GET"])
def analyze_news_sentiment():
    company_name = request.args.get("company")
    
    if not company_name:
        return jsonify({"error": "Please provide a company name in the request URL."}), 400

    news = get_news_articles(company_name)
    if not news:
        return jsonify({"error": "No news articles found."}), 404

    for article in news:
        article["sentiment"] = analyze_sentiment(article["summary"])

    return jsonify({"company": company_name, "articles": news})

# 3️ Comparative Analysis API
@app.route("/compare-news", methods=["GET"])
def compare_news():
    company_name = request.args.get("company")
    
    if not company_name:
        return jsonify({"error": "Please provide a company name in the request URL."}), 400

    news = get_news_articles(company_name)
    if not news:
        return jsonify({"error": "No news articles found."}), 404

    sentiment_summary = compare_sentiments(news)
    return jsonify({"company": company_name, "analysis": sentiment_summary})

# Run API
if __name__ == "__main__":
    app.run(debug=True)

# to get audio
@app.route("/generate-tts", methods=["GET"])
def generate_tts_api():
    text = request.args.get("text")
    
    if not text:
        return jsonify({"error": "No text provided for TTS"}), 400

    filename = generate_tts(text)
    
    if filename:
        return send_file(filename, mimetype="audio/mp3")
    else:
        return jsonify({"error": "TTS generation failed"}), 500

if __name__ == "__main__":
    app.run(debug=True)


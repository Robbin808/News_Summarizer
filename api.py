from flask import Flask, request, jsonify
from utils import get_news_articles, analyze_sentiment, compare_sentiments

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

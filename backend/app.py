import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS
from scraper import search_shopee

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route("/api/search", methods=["GET"])
def search():
    keyword = request.args.get("keyword", "").strip()
    if not keyword:
        return jsonify({"success": False, "error": "Parameter 'keyword' wajib diisi."}), 400

    try:
        products = search_shopee(keyword)
        return jsonify({"success": True, "keyword": keyword, "data": products})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy", "message": "Shopee Scraper API is running"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=False)

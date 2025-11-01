from flask import Flask, request, jsonify, render_template
import requests
import os

app = Flask(__name__)

# ✅ Replace with your actual Gemini API key or set as environment variable
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "AIzaSyBwEdgr2FnftO4HhWdMqqnCC3IslciVzV0")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_message = request.json.get("message")
        if not user_message:
            return jsonify({"error": "Message is required"}), 400

        # ✅ Using the correct Gemini 2.5 Flash endpoint
        url = "https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent"

        payload = {
            "contents": [{
                "role": "user",
                "parts": [{"text": user_message}]
            }],
            "generationConfig": {
                "temperature": 1.0,
                "topP": 0.95,
                "topK": 64
            }
        }

        headers = {
            "Content-Type": "application/json",
            "x-goog-api-key": GEMINI_API_KEY
        }

        response = requests.post(url, headers=headers, json=payload)

        if response.status_code != 200:
            return jsonify({
                "error": f"Gemini API error: {response.text}",
                "status": response.status_code
            }), response.status_code

        data = response.json()
        ai_message = (
            data.get("candidates", [{}])[0]
            .get("content", {})
            .get("parts", [{}])[0]
            .get("text", "No reply received.")
        )

        return jsonify({"reply": ai_message})

    except Exception as e:
        return jsonify({"error": f"Error while contacting Gemini API: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(debug=True)

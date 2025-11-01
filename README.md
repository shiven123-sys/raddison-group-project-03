Gemini/Claude-style Demo (Flask)

Run:
1. cp .env.example .env and paste your GEMINI_API_KEY
2. python -m venv venv && source venv/bin/activate  # optional
3. pip install -r requirements.txt
4. python app.py

Open http://localhost:5000

Security: Do not commit your API keys. If you accidentally pasted a key in public chat, revoke it immediately in Google Cloud Console.

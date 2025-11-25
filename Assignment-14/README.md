# Student Info Portal — Local Flask demo

This tiny demo serves the static `task1.html` homepage and receives the login form on `/login`.

Quick start (Windows / PowerShell):

1. Create and activate a virtualenv (optional):

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Run the Flask app:

```powershell
python app.py
```

4. Open http://127.0.0.1:5000 in your browser. Submit the login form — the server will print the username in the console and show a small confirmation page.

Notes
- This is a development demo only and **must not** be used in production as-is (no authentication, no HTTPS, no CSRF, etc.).

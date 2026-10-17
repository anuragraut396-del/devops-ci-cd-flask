
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>DevOps Status Dashboard</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                margin-top: 100px;
                background: #f1f5f9;
            }
            .card {
                background: white;
                padding: 35px;
                margin: auto;
                max-width: 500px;
                border-radius: 12px;
                box-shadow: 0 4px 12px #0002;
            }
            .status { color: green; font-weight: bold; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>DevOps Status Dashboard</h1>
            <p>Your Python application is running.</p>
            <p class="status">Application Status: ONLINE</p>
            <p>Next: Docker, Jenkins and Kubernetes</p>
            <a href="/health">Check application health</a>
        </div>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify(status="healthy"), 200

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000, debug=False)

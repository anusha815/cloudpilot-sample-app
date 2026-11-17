import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head><title>CloudPilot Sample App</title></head>
    <body>
        <h1>Welcome to CloudPilot!</h1>
        <h2>Sample Python Application</h2>
        <p>Your application has been deployed successfully.</p>
        <p>Build. Deploy. Scale.</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

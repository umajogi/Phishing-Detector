from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load models
email_model = joblib.load("models/email_model.pkl")
email_vectorizer = joblib.load("models/vectorizer_email.pkl")
url_model = joblib.load("models/url_model.pkl")
url_vectorizer = joblib.load("models/vectorizer_url.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    email_result = None
    url_result = None
    checkType = None
    result = None

    if request.method == "POST":
        checkType = request.form.get("checkType")

        if checkType == "email":
            email_text = request.form.get("email_text", "").strip()
            if email_text:
                email_features = email_vectorizer.transform([email_text])
                email_prediction = email_model.predict(email_features)[0]
                email_result = "🚨 Phishing Email" if email_prediction == 1 else "✅ Safe Email"
        
        elif checkType == "url":
            url = request.form.get("url", "").strip()
            if url:
                url_features = url_vectorizer.transform([url])
                url_prediction = url_model.predict(url_features)[0]
                url_result = "🚨 Phishing URL" if url_prediction == 1 else "✅ Safe URL"

        result = email_result or url_result

    return render_template("index.html", result=result, checkType=checkType)

if __name__ == "__main__":
    import webbrowser
    import threading

    def open_browser():
        webbrowser.open_new("http://127.0.0.1:5000")

    threading.Timer(1.0, open_browser).start()
    app.run(debug=True,use_reloader=False)
import joblib

# Load models & vectorizers
email_model = joblib.load("models/email_model.pkl")
email_vectorizer = joblib.load("models/vectorizer_email.pkl")
url_model = joblib.load("models/url_model.pkl")
url_vectorizer = joblib.load("models/vectorizer_url.pkl")

def predict_email(email_text):
    email_features = email_vectorizer.transform([email_text])
    print("\n🔍 Extracted Email Features:", email_features.toarray())
    
    prediction = email_model.predict(email_features)[0]
    probability = email_model.predict_proba(email_features)[0][1] * 100  # Confidence score
    
    print(f"📊 Email Model Raw Prediction: {prediction} (Confidence: {probability:.2f}%)")
    
    result = "🚨 Phishing Email" if probability > 60 else "✅ Likely Safe Email"
    return f"{result} (Confidence: {probability:.2f}%)"

def predict_url(url):
    url_features = url_vectorizer.transform([url])
    print("\n🌍 Extracted URL Features:", url_features.toarray())
    
    prediction = url_model.predict(url_features)[0]
    probability = url_model.predict_proba(url_features)[0][1] * 100  # Confidence score

    print(f"📊 URL Model Raw Prediction: {prediction} (Confidence: {probability:.2f}%)")

    result = "🚨 Phishing URL" if probability > 60 else "✅ Likely Safe URL"
    return f"{result} (Confidence: {probability:.2f}%)"

# Take user input
email = input("Enter email content to check: ")
url = input("Enter URL to check: ")

# Display results
print("\n📧 Email Test Result:", predict_email(email))
print("\n🌍 URL Test Result:", predict_url(url))

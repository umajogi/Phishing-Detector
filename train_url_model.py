import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

# Load dataset
df = pd.read_csv("data/phishing_urls.csv")

# Split into training & testing data
X_train, X_test, y_train, y_test = train_test_split(df['url'], df['label'], test_size=0.2, random_state=42)

# Convert text to numerical features
vectorizer = TfidfVectorizer()
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Train model
model = MultinomialNB()
model.fit(X_train_tfidf, y_train)

# Save model & vectorizer
joblib.dump(model, "models/url_model.pkl")
joblib.dump(vectorizer, "models/vectorizer_url.pkl")

print("✅ URL Phishing Model Trained & Saved!")

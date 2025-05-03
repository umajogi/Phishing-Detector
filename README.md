# Phishing-Detector
Checking the emails content and URLs links are safe or not

Guide to create the folders

phishing-detection/
│── data/
│   ├── emails.csv                 # Email dataset
│   ├── phishing_urls.csv           # URL dataset
│── models/
│   ├── email_model.pkl             # Trained email model
│   ├── url_model.pkl               # Trained URL model
│   ├── vectorizer_email.pkl        # Email feature vectorizer
│   ├── vectorizer_url.pkl          # URL feature vectorizer
│── scripts/
│   ├── train_email_model.py        # Train email classifier
│   ├── train_url_model.py          # Train URL classifier
│   ├── predict.py                  # Prediction script
│── app/
│   ├── main.py                     # Flask Web App
│   ├── templates/
│   │   ├── index.html               # Web UI
│── requirements.txt                 # Dependencies
│── README.md                        # Project Documentation

Entering the commands to run the phishing-detector on VS Code Terminal

PS D:\phishing-detection> python -m venv venv
>> 
PS D:\phishing-detection> .\venv\Scripts\activate
>>
(venv) PS D:\phishing-detection> pip install pandas scikit-learn joblib flask
>>
venv) PS D:\phishing-detection> python scripts/train_model.py
>>
(venv) PS D:\phishing-detection> python scripts/predict.py
>>
(venv) PS D:\phishing-detection> python app/main.py
>>


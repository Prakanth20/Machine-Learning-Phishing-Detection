# 🛡️ Machine Learning Phishing URL Detection

This project demonstrates how to use **machine learning** (specifically a `RandomForestClassifier`) to detect **phishing websites** based on URL features. It is a lightweight prototype intended for educational purposes.

## 🚀 Features

- Classifies URLs as **Legitimate** ✅ or **Phishing** 🚨
- Uses manually defined features such as:
  - URL length
  - Presence of `@` symbol
  - Use of HTTPS
  - Number of dots in the URL
  - Use of IP address
  - URL shortening (e.g., bit.ly, tinyurl)

## 🧠 Technologies Used

- Python 3
- `pandas` for data handling
- `scikit-learn` for machine learning
- `urllib` and `re` for feature extraction from URLs

## 📂 Dataset

A small **hardcoded list of labeled URLs** is used for demonstration. You can expand this to include larger real-world datasets such as:
- [PhishTank](https://www.phishtank.com/)
- [UCI Phishing Websites Data Set](https://archive.ics.uci.edu/ml/datasets/Phishing+Websites)

## 📦 Installation

1. Install required libraries:

```bash
pip install pandas scikit-learn numpy matplotlib
````

2. Run the Python script:

```bash
python phishing_detector.py
```

## 🧪 How It Works

1. **Feature Extraction**
   URLs are converted into numeric features that capture suspicious patterns.

2. **Model Training**
   A `RandomForestClassifier` is trained using the extracted features.

3. **Evaluation**
   The script prints accuracy and a classification report.

4. **Prediction**
   A test list of new URLs is passed to the model for prediction.

### 🔍 Sample Output

```bash
Accuracy: 1.0
Classification Report:
              precision    recall  f1-score   support

           0       1.00      1.00      1.00         1
           1       1.00      1.00      1.00         1

=== Test URLs ===
URL: http://secure-apple.com-login-update@phish.me
Prediction: Phishing 🚨
URL: https://login.microsoftonline.com/
Prediction: Legitimate ✅
```
## ✍️ Customization

You can:

* Replace the hardcoded URLs with a real dataset (CSV)
* Add more sophisticated features (e.g., domain age, WHOIS data)
* Save and load the model using `joblib`
* Turn this into a web app using Flask or Streamlit

## ⚠️ Disclaimer

This is an educational project. Accuracy will vary significantly with small or synthetic datasets. Always test on real, labeled data for practical use cases.

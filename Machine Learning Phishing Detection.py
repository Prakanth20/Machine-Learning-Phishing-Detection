import pandas as pd
from urllib.parse import urlparse
import re
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# === Feature Extraction ===
def extract_features(url):
    features = {}
    parsed = urlparse(url)

    features['URL_Length'] = len(url)
    features['Has_At_Symbol'] = 1 if '@' in url else 0
    features['Uses_HTTPS'] = 1 if parsed.scheme == 'https' else 0
    features['Num_Dots'] = url.count('.')
    features['Contains_IP'] = 1 if re.match(r"^\d{1,3}(\.\d{1,3}){3}$", parsed.netloc) else 0
    features['Is_Shortened_URL'] = 1 if any(s in url for s in ["bit.ly", "tinyurl", "goo.gl"]) else 0

    return features

# === Sample Dataset ===
urls = [
    # Legitimate
    ("https://www.google.com", 0),
    ("https://www.openai.com/research", 0),
    ("https://www.github.com", 0),
    ("http://example.com", 0),

    # Phishing
    ("http://192.168.0.1/login", 1),
    ("http://bit.ly/secure-login", 1),
    ("http://secure-login.com@malicious.net", 1),
    ("http://paypal.login.user.auth-update.com", 1)
]

# Convert to DataFrame
data = []
labels = []

for url, label in urls:
    features = extract_features(url)
    data.append(features)
    labels.append(label)

df = pd.DataFrame(data)
df['Label'] = labels

# === Train Model ===
X = df.drop("Label", axis=1)
y = df["Label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# === Evaluate ===
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred, zero_division=0))

# === Predict New URL ===
def predict_url(url):
    feats = extract_features(url)
    df_url = pd.DataFrame([feats])
    prediction = model.predict(df_url)[0]
    print(f"URL: {url}")
    print("Prediction:", "Phishing 🚨" if prediction == 1 else "Legitimate ✅")

# === Test Prediction ===
print("\n=== Test URLs ===")
test_urls = [
    "http://secure-apple.com-login-update@phish.me",
    "https://login.microsoftonline.com/",
    "http://bit.ly/fakebank",
    "https://www.python.org"
]

for test_url in test_urls:
    predict_url(test_url)

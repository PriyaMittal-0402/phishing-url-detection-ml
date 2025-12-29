import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

print("🔹 Loading dataset...")
df = pd.read_csv("dataset/phishing_urls.csv")

X = df.drop("target", axis=1)
y = df["target"]

print("🔹 Splitting dataset...")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("🔹 Training Random Forest model...")
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)
model.fit(X_train, y_train)

with open("phishing_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as phishing_model.pkl")

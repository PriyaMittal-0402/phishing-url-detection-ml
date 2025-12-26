from flask import Flask, render_template, request
import joblib
from features import extract_features

app = Flask(__name__)

model = joblib.load("model/phishing_model.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    reason = None
    explanation = None
    url = None

    if request.method == "POST":
        url = request.form["url"]

        features = extract_features(url)
        prediction = model.predict([features])[0]

        if prediction == 1:
            result = "YES — Phishing Detected"
            reason = "Suspicious URL Pattern"
            explanation = (
                "The URL contains patterns commonly used in phishing attacks such as "
                "abnormal structure, misleading keywords, or unsafe formatting."
            )
        else:
            result = "NO — Safe URL"
            reason = "No Suspicious Patterns"
            explanation = (
                "The URL structure matches legitimate websites and does not show "
                "known phishing characteristics."
            )

    return render_template(
        "index.html",
        result=result,
        reason=reason,
        explanation=explanation,
        url=url
    )

if __name__ == "__main__":
    app.run(debug=True)

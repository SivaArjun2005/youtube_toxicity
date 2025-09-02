
import joblib

def load_model():
    model = joblib.load("app/utils/toxicity_model.pkl")
    vectorizer = joblib.load("app/utils/vectorizer.pkl")
    return model, vectorizer

def predict_toxicity(text):
    model, vectorizer = load_model()
    X = vectorizer.transform([text])
    prediction = model.predict(X)[0]
    return "Toxic" if prediction == 1 else "Non-Toxic"

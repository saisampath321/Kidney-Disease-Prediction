
import joblib

def load_model(model_path):
    return joblib.load(model_path)

def predict(model, scaler, input_data):
    input_scaled = scaler.transform([input_data])
    return model.predict(input_scaled)[0]

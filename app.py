from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load models with error handling
models = {}
model_files = {
    'diabetes': 'models/diabetes.pkl',
    'breast_cancer': 'models/breast_cancer.pkl',
    'heart': 'models/heart.pkl',
    'kidney': 'models/kidney.pkl',
    'liver': 'models/liver.pkl'
}

for name, path in model_files.items():
    try:
        models[name] = pickle.load(open(path, 'rb'))
        print(f"Loaded {name} model successfully.")
    except FileNotFoundError:
        print(f"Warning: {path} not found. Routes using this model will not work.")
        models[name] = None

def validate_kidney_inputs(values):
    if len(values) != 18:
        return False, "Exactly 18 inputs are required."
    
    specs = [
        (int, 1, 100), (int, 50, 200), (int, 0, 5), (int, 0, 5), (int, 0, 1),
        (int, 0, 1), (int, 0, 1), (int, 0, 1), (int, 50, 500), (int, 10, 300),
        (float, 0.1, 20), (float, 2, 10), (int, 3000, 20000), (int, 0, 1),
        (int, 0, 1), (int, 0, 1), (int, 0, 1), (int, 0, 1)
    ]
    
    for i, (val, (type_func, min_val, max_val)) in enumerate(zip(values, specs)):
        try:
            val = type_func(val)
            if not (min_val <= val <= max_val):
                return False, f"Input {i+1} must be between {min_val} and {max_val}."
        except ValueError:
            return False, f"Input {i+1} must be a valid {type_func.__name__}."
    
    return True, None

def predict(values, model):
    values = np.asarray(values)
    return model.predict(values.reshape(1, -1))[0]

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/diabetes", methods=['GET', 'POST'])
def diabetesPage():
    if models['diabetes'] is None:
        return render_template('diabetes.html', message="Diabetes model not available.")
    return render_template('diabetes.html')

@app.route("/cancer", methods=['GET', 'POST'])
def cancerPage():
    if models['breast_cancer'] is None:
        return render_template('breast_cancer.html', message="Breast cancer model not available.")
    return render_template('breast_cancer.html')

@app.route("/heart", methods=['GET', 'POST'])
def heartPage():
    if models['heart'] is None:
        return render_template('heart.html', message="Heart model not available.")
    return render_template('heart.html')

@app.route("/kidney", methods=['GET', 'POST'])
def kidneyPage():
    if models['kidney'] is None:
        return render_template('kidney.html', message="Kidney model not available.")
    return render_template('kidney.html')

@app.route("/liver", methods=['GET', 'POST'])
def liverPage():
    if models['liver'] is None:
        return render_template('liver.html', message="Liver model not available.")
    return render_template('liver.html')

@app.route("/predict", methods=['POST'])
def predictPage():
    try:
        if request.method == 'POST':
            to_predict_dict = request.form.to_dict()
            
            if not to_predict_dict or len(to_predict_dict) == 0:
                return render_template('kidney.html', message="All fields are required.")
            
            to_predict_list = []
            for key in ['age', 'bp', 'al', 'su', 'rbc', 'pc', 'pcc', 'ba', 'bgr', 'bu', 'sc', 'pot', 'wc', 'htn', 'dm', 'cad', 'pe', 'ane']:
                if key not in to_predict_dict or not to_predict_dict[key].strip():
                    return render_template('kidney.html', message=f"{key.upper()} is required.")
                to_predict_list.append(to_predict_dict[key])
            
            is_valid, error_message = validate_kidney_inputs(to_predict_list)
            if not is_valid:
                return render_template('kidney.html', message=error_message)
            
            to_predict_list = [
                int(to_predict_list[0]), int(to_predict_list[1]), int(to_predict_list[2]),
                int(to_predict_list[3]), int(to_predict_list[4]), int(to_predict_list[5]),
                int(to_predict_list[6]), int(to_predict_list[7]), int(to_predict_list[8]),
                int(to_predict_list[9]), float(to_predict_list[10]), float(to_predict_list[11]),
                int(to_predict_list[12]), int(to_predict_list[13]), int(to_predict_list[14]),
                int(to_predict_list[15]), int(to_predict_list[16]), int(to_predict_list[17])
            ]
            
            if len(to_predict_list) == 8:
                if models['diabetes'] is None:
                    return render_template('diabetes.html', message="Diabetes model not available.")
                pred = predict(to_predict_list, models['diabetes'])
            elif len(to_predict_list) == 26:
                if models['breast_cancer'] is None:
                    return render_template('breast_cancer.html', message="Breast cancer model not available.")
                pred = predict(to_predict_list, models['breast_cancer'])
            elif len(to_predict_list) == 13:
                if models['heart'] is None:
                    return render_template('heart.html', message="Heart model not available.")
                pred = predict(to_predict_list, models['heart'])
            elif len(to_predict_list) == 18:
                if models['kidney'] is None:
                    return render_template('kidney.html', message="Kidney model not available.")
                pred = predict(to_predict_list, models['kidney'])
            elif len(to_predict_list) == 10:
                if models['liver'] is None:
                    return render_template('liver.html', message="Liver model not available.")
                pred = predict(to_predict_list, models['liver'])
            else:
                return render_template('kidney.html', message="Invalid number of inputs.")
            
            return render_template('predict.html', pred=pred)
    
    except Exception as e:
        return render_template('kidney.html', message=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True, port=5000)
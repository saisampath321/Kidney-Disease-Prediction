
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

def train_and_save_model(X_train, y_train, model_path):
    model = LogisticRegression()
    model.fit(X_train, y_train)
    joblib.dump(model, model_path)
    return model

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))

import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import os

# Create models directory if it doesn't exist
if not os.path.exists('models'):
    os.makedirs('models')

# 1. Kidney Model (18 features)
X_kidney = np.array([
    [24, 100, 2, 0, 1, 0, 1, 0, 136, 60, 1.9, 3.7, 9600, 1, 1, 0, 0, 1],
    [68, 80, 3, 0, 0, 1, 0, 0, 157, 162, 9.6, 4.9, 11000, 0, 1, 0, 0, 1],
    [51, 0, 0, 0, 1, 0, 0, 0, 121, 27, 0.8, 3.7, 8300, 0, 0, 0, 0, 0]
])
y_kidney = np.array([1, 1, 0])
kidney_model = RandomForestClassifier(n_estimators=10, random_state=42)
kidney_model.fit(X_kidney, y_kidney)
with open('models/kidney.pkl', 'wb') as f:
    pickle.dump(kidney_model, f)

# 2. Diabetes Model (8 features)
X_diabetes = np.array([[1, 2, 3, 4, 5, 6, 7, 8], [2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7]])
y_diabetes = np.array([1, 1, 0])
diabetes_model = RandomForestClassifier(n_estimators=10, random_state=42)
diabetes_model.fit(X_diabetes, y_diabetes)
with open('models/diabetes.pkl', 'wb') as f:
    pickle.dump(diabetes_model, f)

# 3. Breast Cancer Model (26 features)
X_breast_cancer = np.array([
    [1]*26, [2]*26, [0]*26
])
y_breast_cancer = np.array([1, 1, 0])
breast_cancer_model = RandomForestClassifier(n_estimators=10, random_state=42)
breast_cancer_model.fit(X_breast_cancer, y_breast_cancer)
with open('models/breast_cancer.pkl', 'wb') as f:
    pickle.dump(breast_cancer_model, f)

# 4. Heart Model (13 features)
X_heart = np.array([
    [1]*13, [2]*13, [0]*13
])
y_heart = np.array([1, 1, 0])
heart_model = RandomForestClassifier(n_estimators=10, random_state=42)
heart_model.fit(X_heart, y_heart)
with open('models/heart.pkl', 'wb') as f:
    pickle.dump(heart_model, f)

# 5. Liver Model (10 features)
X_liver = np.array([
    [1]*10, [2]*10, [0]*10
])
y_liver = np.array([1, 1, 0])
liver_model = RandomForestClassifier(n_estimators=10, random_state=42)
liver_model.fit(X_liver, y_liver)
with open('models/liver.pkl', 'wb') as f:
    pickle.dump(liver_model, f)

print("All models created successfully in the models/ directory.")
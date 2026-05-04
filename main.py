from sklearn.model_selection import train_test_split
from data import load_data
from model import train_model, evaluate_model
from utils import scale_data
from predict import predict_students, user_prediction

df = load_data()

X = df[['study_hours', 'attendance', 'past_marks']]
y = df['final_marks']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

scaler, X_train_scaled, X_test_scaled = scale_data(X_train, X_test)

model = train_model(X_train_scaled, y_train)

mae, r2, y_pred = evaluate_model(model, X_test_scaled, y_test)

print(f"MAE: {mae:.2f}")
print(f"R2 Score: {r2:.2f}")

results = predict_students(model, scaler)
for i, (pred, res) in enumerate(results):
    print(f"Student {i+1}: {pred:.1f} -> {res}")

user_prediction(model, scaler)
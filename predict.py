import pandas as pd

def predict_students(model, scaler):
    new_students = pd.DataFrame({
        'study_hours': [7, 2, 5],
        'attendance':  [85, 45, 70],
        'past_marks':  [75, 30, 60]
    })

    scaled = scaler.transform(new_students)
    predictions = model.predict(scaled)

    results = []
    for pred in predictions:
        pred = max(0, min(100, pred))
        result = "PASS" if pred >= 40 else "FAIL"
        results.append((pred, result))

    return results


def user_prediction(model, scaler):
    try:
        sh = float(input("Enter Study Hours: "))
        att = float(input("Enter Attendance %: "))
        pm = float(input("Enter Past Marks: "))

        user_df = pd.DataFrame({
            'study_hours': [sh],
            'attendance': [att],
            'past_marks': [pm]
        })

        scaled = scaler.transform(user_df)
        pred = model.predict(scaled)[0]
        pred = max(0, min(100, pred))

        result = "PASS" if pred >= 40 else "FAIL"

        print(f"Predicted Marks: {pred:.1f}")
        print(f"Result: {result}")

    except:
        print("Invalid input")
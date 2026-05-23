# Student Result Prediction AI

This project uses a Linear Regression model to predict a student's final academic marks based on their study hours, attendance percentage, and past marks. The model is trained on a sample dataset and can be used to predict outcomes for new students, including an interactive prompt for user-inputted data.

## Features

*   **Data-driven Prediction:** Utilizes a linear regression model to forecast student performance.
*   **Model Evaluation:** Measures model accuracy using Mean Absolute Error (MAE) and R-squared (R2) metrics.
*   **Interactive Prediction:** Allows users to input their own data (study hours, attendance, past marks) to receive a real-time prediction.
*   **Pass/Fail Classification:** Classifies the predicted marks into "PASS" (score >= 40) or "FAIL" categories.

## Getting Started

Follow these instructions to set up and run the project locally.

### Prerequisites

*   Python 3.x
*   pip

### Installation & Execution

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/shobhit-pixel/Student-Result-Prediction-AI.git
    cd Student-Result-Prediction-AI
    ```

2.  **Install the required dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3.  **Run the main script:**
    ```sh
    python main.py
    ```

## How It Works

When you run `main.py`, the script performs the following actions:

1.  Loads the student dataset from `data.py`.
2.  Splits the data into training and testing sets.
3.  Scales the features (`study_hours`, `attendance`, `past_marks`) using `StandardScaler`.
4.  Trains a `LinearRegression` model on the scaled training data.
5.  Evaluates the model's performance on the test data and prints the MAE and R2 score.
6.  Predicts results for a predefined set of new student profiles.
7.  Prompts the user to enter custom student data to generate a new prediction and a Pass/Fail result.

### Example Interaction

```
$ python main.py
MAE: 1.15
R2 Score: 0.99
Student 1: 76.8 -> PASS
Student 2: 32.7 -> FAIL
Student 3: 61.3 -> PASS
Enter Study Hours: 8
Enter Attendance %: 90
Enter Past Marks: 85
Predicted Marks: 87.2
Result: PASS
```

## Project Structure

```
.
├── main.py          # Main script to run the full pipeline
├── data.py          # Contains the sample student dataset
├── model.py         # Functions for model training and evaluation
├── predict.py       # Functions for making predictions on new data
├── utils.py         # Utility functions (e.g., data scaling)
├── requirements.txt # Project dependencies
└── How to Run.txt   # Simple instructions file

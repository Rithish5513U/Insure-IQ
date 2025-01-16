# Medical Cost Prediction

This project leverages machine learning to assist medical insurance companies in accurately predicting healthcare costs for individuals. By analyzing key factors such as age, BMI, smoking habits, and region, the model helps in determining fair and balanced insurance premiums.

## Features

- **Data Preprocessing:**
  - Handles missing values with appropriate imputations.
  - Standardizes numerical features and applies one-hot encoding to categorical features.

- **Machine Learning Models:**
  - Implements and evaluates multiple regression models including Linear Regression, Random Forest, Gradient Boosting, XGBoost, CatBoost, and AdaBoost.
  - Hyperparameter tuning for optimal performance.

- **Prediction Pipeline:**
  - Seamless data flow from input preprocessing to final predictions.
  - Supports dynamic user inputs for real-time premium estimation.

- **Streamlit Application:**
  - Interactive and user-friendly web interface for predicting medical costs.
  - Input parameters include age, BMI, number of children, smoking status, and region.
  - Displays predicted healthcare costs in an intuitive format.

## Tech Stack

- **Languages:** Python
- **Frameworks:** Streamlit
- **Libraries:** Pandas, NumPy, Scikit-learn, XGBoost, CatBoost, Matplotlib
- **Tools:** dill for model serialization

## Dataset

The dataset includes:
- Age, BMI, and number of children as numerical features.
- Smoking status, gender, and region as categorical features.
- Healthcare charges as the target variable.

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/Rithish5513U/Medical-Cost-Prediction.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Medical-Cost-Prediction
   ```

3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows: venv\Scripts\activate
   ```

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

## Usage

1. Open the Streamlit application in your browser.
2. Enter the required input details:
   - Age
   - BMI
   - Number of children
   - Smoking status
   - Region
3. Click "Predict" to view the estimated healthcare cost.

## Results

The application provides:
- Predicted healthcare costs based on the user inputs.
- Insights into the contribution of various factors to the overall cost.

---
Developed with ❤️ by [Rithish S](https://github.com/Rithish5513U)

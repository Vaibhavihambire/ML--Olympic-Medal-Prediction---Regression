# Olympic Medal Prediction (Machine Learning)

This project predicts the number of Olympic medals a country can win based on the number of athletes and the previous number of medals using a simple machine learning model.

## Project Steps

### 1. Problem Statement
Predict the number of medals a country can win in the upcoming Olympics using historical data.

### 2. Data Collection
- Columns considered:
  - **Number of Athletes**: Total athletes representing the country.
  - **Previous Medals**: Number of medals won in the previous Olympics.
  - **Medals**: Target variable (Number of medals predicted).

### 3. Data Preprocessing
- Checked for missing values.
- No null values were found.
- Features and target variables were separated.

### 4. Model Selection
- **Algorithm Used**: Linear Regression
  - Chosen because the target is a continuous numerical value (number of medals).

### 5. Model Training
- Split the data into independent variables (**X**) and dependent variable (**y**).
- Trained a Linear Regression model on the entire dataset.

### 6. Model Evaluation
- Evaluated using:
  - **R² Score** (coefficient of determination).
- Achieved a good R² score indicating the model fit the data well.

### 7. Model Saving
- Saved the trained model using **Joblib**.
- File created: `model.pkl`

This saved model will be used later for deployment with a web application (Flask).

---

## Files Included

| File         | Description                       |
|--------------|------------------------------------|
| `olympic_medal_prediction.ipynb` | Jupyter Notebook with full ML model training code. |
| `model.pkl`  | Saved machine learning model (Linear Regression). |

---

## How to Run (ML Part)

1. Clone this repository.
2. Open the `olympic_medal_prediction.ipynb` file.
3. Run all cells to understand data preparation, model training, and saving.
4. The final output will create a `model.pkl` file.

---

## Requirements

- Python 3.x
- Libraries:
  - pandas
  - scikit-learn
  - joblib

Install using:

```bash
pip install pandas scikit-learn joblib
```

---


## Author

Vaibhavi Hambire
https://github.com/account
---

# 📊 Assessment Model Collection

A comprehensive toolkit for implementing various evaluation methods tailored for multi-criteria decision-making and risk assessment.

---

## 📁 Project Structure

```
Assessment_model/
├── AHP/
│   ├── combine.py              # Combines multiple expert judgments
│   ├── level2_1.py             # Natural factor weights calculation
│   └── level2_2.py             # Social factor weights calculation
├── FCE/
│   └── fce.py                  # Fuzzy Comprehensive Evaluation implementation
├── coupled_model/
│   ├── cm-ahp-weights.py       # Coupled model AHP weight calculation
│   └── mutiply_with_weights.py # Weight multiplication implementation
├── generate_membership_degree/
│   ├── calculation.py          # Main membership degree calculation
│   ├── generate_membership_degree_matrix.py # Matrix generation
│   └── mutiply_with_weights.py # Weight multiplication for membership
└── level_classification/
    └── level_classification.py # Level classification implementation
```

---

## 📚 Module Descriptions

### 1. Analytic Hierarchy Process (AHP) 🧮

- **Combines** multiple expert judgments into a single assessment.
- **Calculates** weights for natural and social factors.
- **Performs** consistency checks to validate the judgment matrix.
- **Supports** hierarchical decision-making for complex evaluations.

---

### 2. Fuzzy Comprehensive Evaluation (FCE) 🌫️

- Implements **membership function calculations**:
  - Sharpened membership
  - Intermediate membership
  - Both ends membership
- **Processes** indicator values against defined levels.
- **Supports** multi-criteria evaluation to handle fuzziness in assessments.

---

### 3. Coupled Model 🔗

- **Calculates** coupling degrees and weights.
- Implements **Ex, En, He** calculations for system interactions.
- Supports **consistency ratio (CR)** checking to ensure model reliability.
- Includes **Random Index (RI)** values for consistency validation (up to n=30).

---

### 4. Membership Degree Generation 🎛️

- **Generates** membership degree matrices based on input data.
- Supports **multiple calculation methods** to accommodate diverse evaluation needs.
- Processes **batch data** from Excel files for efficient analysis.
- Implements **matrix multiplication with weights** for enhanced evaluation.

---

### 5. Level Classification 🏅

- Implements **cloud model calculations** for classification.
- Processes **classification data** directly from Excel.
- Generates **Ex, En, He parameters** for classification boundaries.
- Supports **multiple level divisions** for flexible result categorization.

---

## 📋 Requirements

- **Python Version:** 3.6+
- **Libraries:**
  - [NumPy](https://numpy.org/)
  - [Pandas](https://pandas.pydata.org/)
  - [SciPy](https://scipy.org/)
- **Excel files** for input data (Level classification data, expert judgment matrices, indicator values, etc.)

---

## 📥 Data Requirements

The system expects specific **Excel files** for input:
- Level classification data
- Expert judgment matrices
- Indicator values
- Membership degree data

Ensure all input files are correctly formatted to avoid processing issues.

---

## 📈 Output Format

Results are typically **exported to Excel files**, containing:
- Membership degrees
- Classification results
- Combined expert judgments
- Final assessment scores

---

## ⚠️ Usage Notes

1. Ensure all **required Excel files** are in the correct format.
2. **Check consistency ratios** in AHP calculations to maintain model accuracy.
3. **Verify membership function parameters** before proceeding with calculations.
4. **Review classification boundaries** to ensure correct results before processing.

---

## 🤝 Contributing

We welcome contributions! If you find any issues or would like to enhance the project, feel free to open [issues](#) or submit [pull requests](#).

---


*Happy Evaluating! 🎉*

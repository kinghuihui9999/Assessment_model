# 📊 Assessment Model Collection

Welcome to the **Assessment Model Collection** project! This toolkit offers a comprehensive suite of evaluation methods tailored for multi-criteria decision-making and comprehensive evaluation challenges.

---

## 📁 Project Structure

```
Assessment_model/
├── AHP/
│   └── AHP.py                 # Analytic Hierarchy Process
├── FCE/
│   └── FCE.py                 # Fuzzy Comprehensive Evaluation
├── coupled_model/
│   └── coupled_model.py       # Coupled Model Implementation
├── generate_membership_degree/
│   └── generate_membership.py  # Membership Degree Generation Tool
└── level_classification/
    └── level_class.py         # Level Classification Implementation
```

---

## 📚 Module Descriptions

### 1. Analytic Hierarchy Process (AHP) 🧮
**Implementation:** `AHP/AHP.py`

**Features:**
- 📊 **Judgment Matrix Construction:** Build hierarchical structures for decision-making.
- ⚖️ **Weight Vector Calculation:** Determine the relative weights of criteria.
- ✔️ **Consistency Check:** Ensure the judgment matrix is consistent.
- 🥇 **Hierarchical Total Ranking:** Rank alternatives based on the hierarchy.

**Use Case:** Ideal for complex decision problems involving multiple levels and factors.

---

### 2. Fuzzy Comprehensive Evaluation (FCE) 🌫️
**Implementation:** `FCE/FCE.py`

**Features:**
- 📝 **Evaluation Factor Set Establishment:** Define the factors for evaluation.
- 💬 **Comment Set Creation:** Create qualitative assessments.
- 🏋️ **Weight Determination:** Assign weights to different factors.
- 🔗 **Fuzzy Relation Matrix Construction:** Establish relationships between factors.
- 📈 **Fuzzy Comprehensive Calculation:** Perform the evaluation based on fuzzy logic.

**Use Case:** Suitable for multi-factor evaluation problems with inherent fuzziness.

---

### 3. Coupled Model 🔗
**Implementation:** `coupled_model/coupled_model.py`

**Features:**
- 🔄 **Coupling Degree Calculation:** Measure the degree of interaction between systems.
- 📉 **Coordination Degree Analysis:** Analyze the harmony between coupled systems.
- 🏗️ **System Coupling Coordination Evaluation:** Assess the coordinated development of systems.

**Use Case:** Evaluates system interactions and their coordinated development.

---

### 4. Generate Membership Degree 🎛️
**Implementation:** `generate_membership_degree/generate_membership.py`

**Features:**
- ➕ **Positive Indicator Membership Calculation:** Calculate memberships for positive indicators.
- ➖ **Negative Indicator Membership Calculation:** Calculate memberships for negative indicators.
- 🔄 **Intermediate Indicator Membership Calculation:** Handle intermediate indicators.

**Use Case:** Facilitates quantitative processing of fuzzy evaluation indicators.

---

### 5. Level Classification 🏅
**Implementation:** `level_classification/level_class.py`

**Features:**
- 📂 **Evaluation Result Level Division:** Divide results into different levels.
- ⚙️ **Classification Criteria Setting:** Define criteria for classification.
- 🏆 **Level Determination:** Determine the appropriate level for evaluation results.

**Use Case:** Used for grade division and classification of evaluation outcomes.

---

## 📋 Requirements

- **Python:** 3.6+
- **Libraries:**
  - [NumPy](https://numpy.org/)
  - [Pandas](https://pandas.pydata.org/)

---

## 🚀 Usage Examples

### AHP Example

```python
from AHP.AHP import AHP

# Create judgment matrix
matrix = [
    [1, 2, 7],
    [1/2, 1, 4],
    [1/7, 1/4, 1]
]

ahp = AHP(matrix)
weights = ahp.get_weights()
print("AHP Weights:", weights)
```

### FCE Example

```python
from FCE.FCE import FCE

# Initialize evaluation matrix and weights
R = [
    [0.2, 0.3, 0.5],
    [0.3, 0.5, 0.2],
    [0.4, 0.4, 0.2]
]
W = [0.4, 0.3, 0.3]

fce = FCE(R, W)
result = fce.evaluate()
print("FCE Result:", result)
```

---

## ⚠️ Important Notes

1. **AHP Consistency:** Ensure the judgment matrix meets consistency requirements when using AHP.
2. **FCE Weight Sum:** In FCE evaluation, the sum of weight vector components should equal 1.
3. **Data Standardization:** Required before using the coupled model.
4. **Membership Degree Generation:** Choose appropriate calculation methods based on indicator characteristics.

---

## 🤝 Contributing

Contributions are welcome! Feel free to open [issues](#) or submit [pull requests](#) to help improve the project.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 📝 Contact

For any inquiries or support, please reach out to [your-email@example.com](mailto:your-email@example.com).

---

*Happy Evaluating! 🎉*

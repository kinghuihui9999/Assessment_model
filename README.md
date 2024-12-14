# ASSESSMENT MODEL COLLECTION

This project is a comprehensive assessment model toolkit that implements various commonly used evaluation methods for solving multi-criteria decision-making and comprehensive evaluation problems.

## PROJECT STRUCTURE

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

MODULE DESCRIPTION
-----------------

1. Analytic Hierarchy Process (AHP)
   Implementation: AHP/AHP.py
   Main Features:
   - Judgment matrix construction
   - Weight vector calculation
   - Consistency check
   - Hierarchical total ranking
   Use Case: Complex decision problems with multiple levels and factors

2. Fuzzy Comprehensive Evaluation (FCE)
   Implementation: FCE/FCE.py
   Main Features:
   - Evaluation factor set establishment
   - Comment set creation
   - Weight determination
   - Fuzzy relation matrix construction
   - Fuzzy comprehensive calculation
   Use Case: Multi-factor evaluation problems with fuzziness

3. Coupled Model
   Implementation: coupled_model/coupled_model.py
   Main Features:
   - Coupling degree calculation
   - Coordination degree analysis
   - System coupling coordination evaluation
   Use Case: Evaluation of system interaction and coordinated development

4. Generate Membership Degree
   Implementation: generate_membership_degree/generate_membership.py
   Main Features:
   - Positive indicator membership calculation
   - Negative indicator membership calculation
   - Intermediate indicator membership calculation
   Use Case: Quantitative processing of fuzzy evaluation indicators

5. Level Classification
   Implementation: level_classification/level_class.py
   Main Features:
   - Evaluation result level division
   - Classification criteria setting
   - Level determination
   Use Case: Grade division and classification of evaluation results

REQUIREMENTS
-----------
- Python 3.6+
- NumPy
- Pandas

USAGE EXAMPLES
-------------

AHP Example:
from AHP.AHP import AHP

# Create judgment matrix
matrix = [
    [1, 2, 7],
    [1/2, 1, 4],
    [1/7, 1/4, 1]
]

ahp = AHP(matrix)
weights = ahp.get_weights()

FCE Example:
from FCE.FCE import FCE

# Initialize evaluation matrix and weights
R = [[0.2, 0.3, 0.5],
     [0.3, 0.5, 0.2],
     [0.4, 0.4, 0.2]]
W = [0.4, 0.3, 0.3]

fce = FCE(R, W)
result = fce.evaluate()

IMPORTANT NOTES
--------------
1. When using AHP, ensure the judgment matrix meets consistency requirements
2. In FCE evaluation, the sum of weight vector components should equal 1
3. Data standardization is required before using the coupled model
4. Choose appropriate calculation methods based on indicator characteristics when generating membership degrees

CONTRIBUTING
-----------
Issues and Pull Requests are welcome to help improve the project.

LICENSE
-------
This project is licensed under the MIT License. 

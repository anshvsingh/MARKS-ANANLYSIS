# 📊 Student Marks Analysis Using Linear Algebra

A mini project that applies **Linear Algebra concepts** to analyze, predict, and classify student performance using Python and NumPy.

---

## 📁 Project Structure

```
student-marks-analysis/
│
├── student.py        # Main Python script
├── report.pdf        # Project report
└── README.md         # Project documentation
```

---

## 🎯 Objective

To apply core Linear Algebra techniques on a real-world student marks dataset and derive meaningful insights such as:
- Identifying independent subjects
- Predicting missing marks
- Discovering performance patterns

---

## 🧮 Linear Algebra Pipeline

| Step | Concept | Purpose |
|------|---------|---------|
| 1 | Matrix Representation | Store student marks as a matrix |
| 2 | RREF Simplification | Simplify and reduce the matrix |
| 3 | Rank & Nullity | Find independent vs redundant subjects |
| 4 | Redundancy Removal | Keep only useful data |
| 5 | Gram-Schmidt Orthogonalization | Make subject vectors independent |
| 6 | Projection | Approximate overall performance |
| 7 | Least Squares Prediction | Predict missing/future marks |
| 8 | Eigenvalues & Eigenvectors | Discover performance patterns |
| 9 | System Simplification | Focus on dominant patterns |
| 10 | Average Analysis | Classify students by performance |

---

## 📌 Dataset

A 4×3 matrix where:
- **Rows** → Students (4 students)
- **Columns** → Subjects (Math, Physics, Chemistry)

```
Student Marks Matrix:
 [[85, 78, 92],
  [88, 76, 95],
  [90, 85, 59],
  [40, 50, 40]]
```

---

## 📈 Key Results

- **Rank:** 3 | **Nullity:** 0 → All subjects are independent
- **Predicted Chemistry Mark** (for new student with [80, 75]): **≈ 74.65**
- **Dominant Eigenvalue:** 1290.91 → Contributes **85.26%** of variance
- **Student Classifications:**
  - Student 1 (avg 85.00) → Average 👍
  - Student 2 (avg 86.33) → Topper 🏆
  - Student 3 (avg 78.00) → Average 👍
  - Student 4 (avg 43.33) → Needs Improvement ⚠️

---

## 🛠️ Requirements

- Python 3.x
- NumPy

Install dependencies:
```bash
pip install numpy
```

---

## ▶️ How to Run

```bash
python student.py
```

---


## 📚 Concepts Used

- Matrix Operations (NumPy)
- Row Reduced Echelon Form (RREF)
- Rank & Nullity Theorem
- Gram-Schmidt Orthogonalization
- Vector Projection
- Least Squares Approximation
- Eigenvalues & Eigenvectors
- Covariance Matrix

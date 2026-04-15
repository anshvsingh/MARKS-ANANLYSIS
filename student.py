import numpy as np   # Import numpy for matrix operations
from numpy.linalg import matrix_rank, eig, inv   # Import functions for rank, eigenvalues, inverse

print("\n          MINI PROJECT          ")
print("Title: Student Marks Analysis Using Matrices")
print("===============================================")


# REAL WORLD DATA

print("\n🔷 REAL WORLD DATA")

# Create matrix of student marks
# Rows = students, Columns = subjects
A = np.array([
    [85, 78, 92],
    [88, 76, 95],
    [90, 85, 59],
    [40, 50, 40]
])

print("Student Marks Matrix:\n", A)   # Display matrix


# MATRIX REPRESENTATION

print("\n🔷 MATRIX REPRESENTATION")

print("Rows → Students, Columns → Subjects")   # Explain structure
print("Matrix Shape:", A.shape)               # Show dimensions


# MATRIX SIMPLIFICATION (RREF)

print("\n🔷 MATRIX SIMPLIFICATION (RREF)")

# Function to convert matrix into RREF (simplified form)
def rref(matrix):
    M = matrix.astype(float)   # Convert to float for division
    rows, cols = M.shape       # Get size of matrix
    r = 0                      # Row pointer

    for c in range(cols):      # Loop through columns
        if r >= rows:
            break

        pivot = np.argmax(abs(M[r:, c])) + r   # Find pivot row

        if M[pivot, c] == 0:   # Skip if column is zero
            continue

        M[[r, pivot]] = M[[pivot, r]]   # Swap rows

        M[r] = M[r] / M[r, c]   # Make pivot = 1

        for i in range(rows):   # Make other elements = 0
            if i != r:
                M[i] = M[i] - M[i, c] * M[r]

        r += 1

    return M

print("RREF Matrix:\n", rref(A))   # Print simplified matrix


# STRUCTURE OF SPACE

print("\n🔷 STRUCTURE OF SPACE")

rank = matrix_rank(A)   # Rank = number of independent subjects
nullity = A.shape[1] - rank   # Nullity = dependent subjects

print("Rank:", rank)
print("Nullity:", nullity)


# REMOVE REDUNDANCY

print("\n🔷 REMOVE REDUNDANCY")

# Check if subjects are independent or redundant
if nullity == 0:
    print("No redundant subjects. All are independent.")
else:
    print("Some subjects are redundant.")


# ORTHOGONALIZATION

print("\n🔷 ORTHOGONALIZATION (Gram-Schmidt)")
# Function to make vectors perpendicular (orthogonal)

def gram_schmidt(A):       #overlaping to non overlaping
    Q = []   # Store orthogonal vectors

    for a in A.T:   # Loop through columns (subjects)
        u = a.copy() #copy the current vector

        for q in Q:   # Remove overlap with previous vector
            u = u - np.dot(q, a) * q

        u = u / np.linalg.norm(u)   # Normalize vector (length = 1)

        Q.append(u) #stores result

    return np.array(Q).T    #return ortho matrics

Q = gram_schmidt(A)   # Compute orthogonal basis
print("Orthogonal Basis:\n", Q)

# PROJECTION

print("\n🔷 PROJECTION") # closest representation of data

b = A[:, 0]   # take one subject (first column)

# Projection = best approximation using orthogonal vectors
projection = Q @ Q.T @ b   #closest version of data b

print("Projection Result:\n", projection)


# PREDICTION (LEAST SQUARES)

print("\n🔷 PREDICTION / APPROXIMATION (Least Squares)")

A_ls = A[:, :2]   # First 2 subjects (inputs)
b_ls = A[:, 2]    # Third subject (target)

# Least squares = best-fit solution minimizing error
x = inv(A_ls.T @ A_ls) @ A_ls.T @ b_ls

new_student = np.array([80, 75])   # New student marks

predicted = new_student @ x   # Predict Chemistry marks

print("Predicted Chemistry Mark:", predicted)


# PATTERN DISCOVERY (EIGENVALUES)

print("\n🔷 PATTERN DISCOVERY (Eigenvalues & Eigenvectors)")

cov_matrix = np.cov(A.T)   # Covariance matrix (relationships between subjects)

# Eigenvalues = strength of patterns
# Eigenvectors = direction of patterns
eigenvalues, eigenvectors = eig(cov_matrix)

print("Eigenvalues:\n", eigenvalues)

# 🔥 Convert eigenvalues into percentage contribution
total = np.sum(eigenvalues)
percentages = (eigenvalues / total) * 100

print("\nEigenvalue Percentages (%):\n", percentages)


# SYSTEM SIMPLIFICATION

print("\n🔷 SYSTEM SIMPLIFICATION")

dominant_index = np.argmax(eigenvalues)   # Index of largest eigenvalue

print("Dominant Eigenvalue:", eigenvalues[dominant_index])
print("Dominant Pattern Contribution: {:.2f}%".format(percentages[dominant_index]))


# FINAL APPLICATION OUTPUT

print("\n🔷 FINAL APPLICATION OUTPUT")

print("✔ Student performance analyzed")
print("✔ Independent subjects identified")
print("✔ Missing marks predicted")
print("✔ Patterns discovered using eigenvalues")


# AVERAGE ANALYSIS

print("\n🔷 FINAL PERFORMANCE ANALYSIS")

averages = np.mean(A, axis=1)   # Average marks of each student

for i, avg in enumerate(averages):
    print(f"\nStudent {i+1} Average: {avg:.2f}")

    # Classify performance
    if avg > 85:
        print("Performance: Topper 🏆")
    elif avg >= 70:
        print("Performance: Average 👍")
    else:
        print("Performance: Needs Improvement ⚠️")

print("\n          END          ")

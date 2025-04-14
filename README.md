
#DAA: Design and Analysis of Algorithms

This repository contains beginner-friendly implementations of classical algorithms covered in the Design and Analysis of Algorithms (DAA) course. Each problem is explained in simple terms, with working Python code using techniques like **Dynamic Programming**, **Greedy**, **Divide and Conquer**, and **Backtracking**.

---

##Table of Contents

1. [Longest Common Subsequence (LCS) - DP](#1-longest-common-subsequence-lcs---dp)
2. [Matrix Chain Multiplication - DP](#2-matrix-chain-multiplication---dp)
3. [Huffman Coding - Greedy](#3-huffman-coding---greedy)
4. [Strassen’s Matrix Multiplication - Divide and Conquer](#4-strassens-matrix-multiplication---divide-and-conquer)
5. [Karatsuba Multiplication - Divide and Conquer](#5-karatsuba-multiplication---divide-and-conquer)
6. [N-Queens Problem - Backtracking](#6-n-queens-problem---backtracking)
7. [Simplex Method - Linear Programming](#7-simplex-method---linear-programming)
8. [Bellman-Ford Algorithm - DP on Graphs](#8-bellman-ford-algorithm---dp-on-graphs)

---

## 1. Longest Common Subsequence (LCS) - DP

###Problem:
Given two strings, find the length of the **longest subsequence** that exists in both strings (not necessarily continuous characters).

###Key Idea:
- Use a 2D table `L[i][j]` to store the LCS length of prefixes.
- Build up the solution bottom-up.

###Formula:
```python
if X[i-1] == Y[j-1]:
    L[i][j] = L[i-1][j-1] + 1
else:
    L[i][j] = max(L[i-1][j], L[i][j-1])
```

---

## 2. Matrix Chain Multiplication - DP

###Problem:
You are given dimensions of matrices to be multiplied. Find the **minimum number of scalar multiplications** required.

###Key Idea:
- Use a 2D table `dp[i][j]` to store the minimum cost to multiply matrices `i` to `j`.

###Formula:
```python
dp[i][j] = min(dp[i][k] + dp[k+1][j] + dims[i] * dims[k+1] * dims[j+1])
```

---

## 3. Huffman Coding - Greedy

###Problem:
Compress a string by assigning **shorter binary codes** to more frequent characters using a binary tree.

###Key Idea:
- Use a **min-heap** to always combine the least frequent nodes.
- Characters in the left tree get `'0'`, and right get `'1'`.

###Approach:
```python
for pair in left:
    pair[1] = "0" + pair[1]
for pair in right:
    pair[1] = "1" + pair[1]
```

---

## 4. Strassen’s Matrix Multiplication - Divide and Conquer

###Problem:
Multiply two square matrices faster than traditional O(n³) method.

###Key Idea:
Split matrices A and B into 4 parts each and compute only 7 products using:

###Formulae:
```
P = (A11 + A22)(B11 + B22)
Q = (A21 + A22)(B11)
R = A11(B12 − B22)
S = A22(B21 − B11)
T = (A11 + A12)(B22)
U = (A21 − A11)(B11 + B12)
V = (A12 − A22)(B21 + B22)
```

Then compute:
```
C11 = P + S − T + V
C12 = R + T
C21 = Q + S
C22 = P + R − Q + U
```

---

## 5. Karatsuba Multiplication - Divide and Conquer

###Problem:
Multiply very large integers stored as strings (e.g., 256+ digits) efficiently.

###Key Idea:
Split each number into halves and use this clever formula:
```
X = (10^m * a + b), Y = (10^m * c + d)

XY = ac * 10^(2m) + ( (a+b)(c+d) - ac - bd ) * 10^m + bd
```

Only **3 recursive multiplications** instead of 4!

---

## 6. N-Queens Problem - Backtracking

###Problem:
Place `N` queens on an `N×N` chessboard such that:
- No two queens are in the same row, column, or diagonal.

###Key Idea:
- Place queens row by row.
- Use recursion + backtracking to try each column safely.

###Output Format:
Each solution is a list like `[1, 3, 0, 2]`  
→ Queen in column 1 of row 0, column 3 of row 1, and so on.

---

## 7. Simplex Method - Linear Programming

###Problem:
Solve optimization problems (maximize or minimize) under linear constraints.

###Key Idea:
- Use a **tableau method** to find the optimal solution.
- Pivot the matrix to improve the result until optimality is reached.

➡️ [Code is implemented for educational test cases.]

---

## 8. Bellman-Ford Algorithm - DP on Graphs

###Problem:
Find shortest paths from a source node to all other nodes in a graph that **may have negative edge weights**.

###Key Idea:
- Relax all edges `V - 1` times.
- Detect negative weight cycles if relaxation is still possible after that.

➡Graphs are provided in **Adjacency Matrix** format.

---

## 🧾 How to Use This Repository

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/daa-algorithms.git
   ```

2. Navigate to the folder and run any Python file using:
   ```bash
   python filename.py
   ```

3. Each file has:
   - Clear comments
   - Beginner-level logic
   - Printable test cases

---

##Author

This repository was created as part of a college **DAA course** and is written with a focus on **understanding and clarity** for beginners.

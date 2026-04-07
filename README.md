# COP4533 Programming Assignment 3: Highest Value Longest Common Sequence

## Yi Su [31833267]
An implementation of a dynamic programming solution to find the **highest value longest common sequence** between two strings, where each character has an associated value.

## Input File
- First line: integer `K`, the number of characters in the alphabet
- Next `K` lines: each line contains a character `x_i` and its integer value `v_i`
- Next line: string `A`
- Next line: string `B`
```text
K
x1 v1
x2 v2
...
xK vK
A
B
```
## Usage
Using an input file (e.g., `tests/test1.in`), you can pass the input file's filepath as a command line argument.
```Bash
python src/main.py tests/test1.in
```
The program computes the maximum total value of a common substring between A and B, and outputs the result. The output is printed and written to a .out file with the same filepath (e.g., tests/test1.out).
## Assumptions
- `K >= 1`
- `v_i > 0` (values are positive)
- All characters in `A` and `B` are included in the given alphabet
- Subsequences are contiguous

## Test Generator
`tests/generateTest.py` generates a test to the filepath given as a parameter to the function. It selects `K` random alphabet characters and assigns each with a random value with a default range of `(0, 50)`.

## Question 1
Using the test files `test[2-11].in` generated with the test generator, strings of various sizes `25` to `5000` are used to measure the runtime of the algorithm.

## Question 2
### Recurrence
Let OPT(i, j) be the maximum total of a value common subsequence ending at `A[i-1]` and `B[j-1]`.
$$
OPT(i, j) =
\begin{cases} 
\max(\text{value}(A[i-1]),\ OPT(i-1, j-1) + \text{value}(A[i-1])) & \text{if } A[i-1] = B[j-1] \\ 
0 & \text{otherwise} 
\end{cases}
$$
### Base Cases
$$
OPT(i, 0) = 0 \quad \forall i, \qquad OPT(0, j) = 0 \quad \forall j
$$
### Explanation
- If `A[i-1] = B[j-1]`, `OPT(i, j)` is the maximum of starting a new substring with `value(A[i-1])` or extending the previous substring with `OPT(i-1, j-1) + value(A[i-1])`.
- `If A[i-1] ≠ B[j-1]`, the substring cannot continue, so `OPT(i, j) = 0`.
- The maximum-value common substring is the largest value among all `OPT(i, j)` for `1 ≤ i ≤ len(A)` and `1 ≤ j ≤ len(B)`.

## Question 3
### Pseudocode:
```text
Input: Strings A[1..n], B[1..m], value map value[c] for each character c
Output: Maximum total value of a common substring (HVLCS)

Initialize OPT[0..n][0..m] = 0
max_value = 0

for i = 1 to n:
    for j = 1 to m:
        if A[i-1] == B[j-1]:
            OPT[i][j] = max(value[A[i-1]], OPT[i-1][j-1] + value[A[i-1]])
            max_value = max(max_value, OPT[i][j])
        else:
            OPT[i][j] = 0

return max_value
```
### Runtime Analysis
- The algorithm uses two nested loops over `n` and `m`, so the total runtime is `O(nm)` with a space complexity of `O(nm)`.
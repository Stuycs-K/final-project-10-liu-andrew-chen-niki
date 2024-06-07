# Hill Cipher
### By: Andrew Liu & Niki Chen  

## What is the Hill Cipher?
* Polygraphic Substitution Cipher
    * Divides the plaintext into blocks of size n, and substitutes each character through linear algebra.
    * Symmetric key encryption algorithm, which means it is uses the same key for both encryption and decryption.
* Created by Lester S. Hill in 1929
* Linear Algebra concepts used:
    * Matrix Multiplication
    * Matrix Inverses
    * Determinants
    * Adjoint Matrices
* Practical Use Cases
    * Military Communications - to prevent messages from being intercepted
    * Banking - to protect financial transactions and customer data from malicious access.
    * Computer security - used to encrypt passwords and sensitive information on computers
* Strengths 
    * Very tough to crack if block size and key size is large
    * Efficient and easy to implement
* Weaknesses
    * Vulnerable to brute force attacks
    * Vulnerable to known plaintext attacks, where an attacker can crack the cipher with access to both the plaintext and ciphertext.

## Encoding Plaintext using the Hill Cipher
Parameters: Plaintext and a square key matrix of dimension n.


Example: 

Plaintext: "CYBER"

Key Matrix:

$$
\begin{pmatrix}
3 & 1 & 4 \\
2 & 0 & 1 \\
2 & 1 & 3
\end{pmatrix}
$$

### Step #1 
Convert plaintext into array of ascii values

"CYBER" -> [67, 89, 66, 69, 82]

### Step #2 
Take modolus 26 to create characters that have values from 0 - 25

[67, 89, 66, 69, 82] -> [2, 24, 1, 4, 17]

### Step #3

Split array into groups of size n, where n is the dimension of our square key matrix. Since our key matrix in the example is dimension 3, we will split our character array into groups of size 3.

[2, 24, 1, 4, 17] -> [2, 24, 1], [4, 17]]

### Step #4

Since the length of our plain text is not a multiple of n, which is 3 in this case, we need to pad the character groups that have sizes less than n with zeroes. 

[2, 24, 1], [4, 17]] -> [[2, 24, 1], [4, 17, 0]]

### Step #5

Now that we have our triplets, we need to convert them into column vectors and multiply each one by the key matrix.

$$
[[2, 24, 1], [4, 17, 0]]   
->
\begin{pmatrix}
2 \\
24 \\
1
\end{pmatrix},
\begin{pmatrix}
4 \\
17 \\
0
\end{pmatrix}
$$



$$
\begin{pmatrix}
3 & 1 & 4 \\
2 & 0 & 1 \\
2 & 1 & 3
\end{pmatrix}
\begin{pmatrix}
2 \\
24 \\
1
\end{pmatrix} = 
\begin{pmatrix}
34\\
5 \\
31
\end{pmatrix}
$$


$$
\begin{pmatrix}
3 & 1 & 4 \\
2 & 0 & 1 \\
2 & 1 & 3
\end{pmatrix}
\begin{pmatrix}
4 \\
17 \\
0
\end{pmatrix} = 
\begin{pmatrix}
29\\
8 \\
25
\end{pmatrix}
$$

### Step #6

We need to the encoded message to be a valid ASCII value. First, we take the modulos 26 to get values between 0 and 25. Then, we add back 65 to get the equivalent ASCII representation.


$$
 \begin{pmatrix}
34\\
5 \\
31
\end{pmatrix}
mod 26 = 
 \begin{pmatrix}
8\\
5 \\
5
\end{pmatrix}
 + 
  \begin{pmatrix}
65\\
65 \\
65
\end{pmatrix}
 = 
\begin{pmatrix}
73\\
70 \\
70
\end{pmatrix}
$$


$$
\begin{pmatrix}
29 \\
8 \\
25
\end{pmatrix}
mod 26 = 
\begin{pmatrix}
3 \\
8 \\
25
\end{pmatrix}
 + 
  \begin{pmatrix}
65\\
65 \\
65
\end{pmatrix}
 = 
\begin{pmatrix}
68\\
73 \\
90
\end{pmatrix}
$$


### Step #7 
These column vectors need to be converted back to arrays and then to their ASCII value.

$$
\begin{pmatrix}
73\\
70 \\
70
\end{pmatrix}
 = [73,70,70]
 = IFF
$$



$$
\begin{pmatrix}
68\\
73 \\
90
\end{pmatrix}
 = [68,73,90]
 = DIZ
$$

### Step #8 
Viola! Now you just have to combine these two strings. The encoded message is IFFDIZ.

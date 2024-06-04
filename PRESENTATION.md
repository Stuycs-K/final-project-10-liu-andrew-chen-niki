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

Plaintext: "cybersecurity"

Key Matrix:
<div align="left">

$$
\begin{array}{l}
\begin{pmatrix}
3 & 1 & 4 \\
2 & 0 & 1 \\
2 & 1 & 3
\end{pmatrix}
\end{array}
$$

</div>


### Step #1 
Divide the 
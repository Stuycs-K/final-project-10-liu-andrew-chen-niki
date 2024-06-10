# Hill Cipher
### By: Andrew Liu & Niki Chen  

## What is the Hill Cipher?
* Polygraphic Substitution Cipher
    * Divides the plaintext into blocks of size n, and substitutes each character through linear algebra.
    * Symmetric key encryption algorithm, which means it uses the same key for both encryption and decryption.
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
Take modolus 65 to create characters that have values from 0 - 25

[67, 89, 66, 69, 82] -> [2, 24, 1, 4, 17]

### Step #3

Split array into groups of size n, where n is the dimension of our square key matrix. Since our key matrix in the example is dimension 3, we will split our character array into groups of size 3.

[2, 24, 1, 4, 17] -> [ [2, 24, 1], [4, 17] ]

### Step #4

Since the length of our plain text is not a multiple of n, which is 3 in this case, we need to pad the character groups that have sizes less than n with zeroes. 

[ [2, 24, 1], [4, 17] ] -> [ [2, 24, 1], [4, 17, 0] ]

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

We need the encoded message to be a valid ASCII value. First, we take the modulos 26 to get values between 0 and 25. Then, we add back 65 to get the equivalent ASCII representation.


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
\end{pmatrix} = 
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
\end{pmatrix} = 
\begin{pmatrix}
68\\
73 \\
90
\end{pmatrix}
$$


### Step #7 
These column vectors need to be converted back to arrays and then to their ASCII values.

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


## Decoding Ciphertext Using the Hill Cipher
Parameters: Ciphertext and a square key matrix of dimension n.

Let's decode the ciphertext we generated from the encryption example.

Example: 

Ciphertext: "IFFDIZ"


As mentioned earlier, Hill Cipher uses the same key matrix for both encryption and decryption.

Key Matrix:

$$
\begin{pmatrix}
3 & 1 & 4 \\
2 & 0 & 1 \\
2 & 1 & 3
\end{pmatrix}
$$


Something very cool about Hill Cipher is that the encryption and decryption logics are the same. In other words, we can use the same function to encode and decode messages (which is what we did!) ... with a caveat ...

We have to use the inverse of the key matrix! An inverse matrix, $m^{-1}$ is a matrix that when multiplied with a given matrix, $m$, gives the identity matrix, $I$, a square matrix in which all the elements of principal diagonals are one, and all other elements are zeros.

$$
mm^{-1} = I
$$



$$
\begin{pmatrix}
4 & 3 \\
3 & 2
\end{pmatrix}
\begin{pmatrix}
-2 & 3 \\
3 & -4
\end{pmatrix}=
\begin{pmatrix}
1 & 0 \\
0 & 1
\end{pmatrix}
$$

To do that, we can use the matrix inverse formula: 

$$
m^{-1}=
(det(m))^{-1}
\begin{pmatrix} 
d & -b \\ 
-c & a
\end{pmatrix} 
$$

where $(det(m))^{-1}$ is the multiplicative inverse of the determinant

$$
\begin{pmatrix}
d & -b \\
-c & a
\end{pmatrix}
$$ 

is the adjugate, or adjoint, matrix of $m$, which is obtained by taking the transpose of the co-factor elements of the given matrix. 

For simplicity, let's consider the 2x2 matrix, 

$$
A=
\begin{pmatrix}
3 & 6 \\
-4 & 8
\end{pmatrix}
$$

The three important steps involved in finding the adjoint of a matrix are:
1. Find the minor matrix M of all the elements of matrix A.
2. Find the cofactor matrix C of all the minor elements of matrix M.
3. Find the adj B by taking the transpose of the cofactor matrix C.

For step 1, the minor matrix $M$ is found by replacing each entry with its minor. To do this, you have to cover the row and column of the entry; the remaining entry is the minor.

Minor of 3:

$$
\begin{pmatrix}
0 & 0 \\
0 & 8
\end{pmatrix}=
8
$$

Minor of 6:

$$
\begin{pmatrix}
0 & 0 \\
-4 & 0
\end{pmatrix}=
-4
$$

Minor of -4:

$$
\begin{pmatrix}
0 & 6 \\
0 & 0
\end{pmatrix}=
6
$$

Minor of 8:

$$
\begin{pmatrix}
3 & 0 \\
0 & 0
\end{pmatrix}=
3
$$

Minor matrix M:

$$
\begin{pmatrix}
8 & -4 \\
6 & 3
\end{pmatrix}
$$

For step 2, the cofactor of an element $a_{ij}$ is obtained by multiplying its minor by $(-1)^{i+j}$. For 2x2 matrices like $A$ and $M$, the cofactor matrix, $C$, is the minor matrix with its elements multiplied by the following signs:

$C$ = 
[ [+  -]
[-  +] ]

Cofactor matrix C: 

$$
\begin{pmatrix}
8 & 4 \\
-6 & 3
\end{pmatrix}
$$

For step 3, the transpose of a matrix is obtained by simply interchanging its rows and columns.

Transpose matrix $C^{T}$ = 

$$
\begin{pmatrix}
8 & -6 \\
4 & 3
\end{pmatrix}
$$

This is the adjugate/adjoint matrix.

The determinant of the original matrix $A$ = 

$$
\begin{pmatrix}
3 & 6 \\
-4 & 8
\end{pmatrix}
$$

can be calculated using the formula $ad-bc$ where $a, b, c, d$ refer to the elements of the matrix 

$$
\begin{pmatrix}
a & b \\
c & d
\end{pmatrix}
$$


$det(A)$ = 48. So $A^{-1}$ = $\frac{1}{48}$ 

$$
\begin{pmatrix}
8 & -6 \\
4 & 3
\end{pmatrix}=
\begin{pmatrix}
1/6 & -1/8 \\
1/12 & 1/16
\end{pmatrix}
$$

Note: The matrix $m$ will have an inverse $m^{-1} (mod 26)$  if and only if $det(m) (mod 26)$ has a multiplicative inverse. That being said, in order for the key matrix to actually work for encryption and decryption using the Hill Cipher, it has to be invertible. Interestingly, the example matrix 

$$
A= 
\begin{pmatrix}
3 & 6 \\
-4 & 8
\end{pmatrix}
$$ 

we used to demonstrate how to find an inverse of a matrix is actually not invertible $mod 26$ because $48(mod 26)$ doesn't have a multiplicative inverse.
Rule: $a$ is invertible $mod(p)$ when $a$ and $p$ are coprime.

Other than this caveat, the decryption method is the same as encryption, except the two parameters are ciphetext and inverse of key matrix, rather than plaintext and key matrix.


Going back to decrypting the message "IFFDIZ", we first need to invert our key matrix 

$$
\begin{pmatrix}
3 & 1 & 4 \\
2 & 0 & 1 \\
2 & 1 & 3
\end{pmatrix} ^{-1}=
\begin{pmatrix}
25 & 1 & 1 \\
22 & 1 & 5 \\
2 & 25 & 24
\end{pmatrix}
$$

### Step #1 
Convert ciphertext into array of ascii values

"IFFDIZ" -> [73, 70, 70, 68, 73, 90]

### Step #2 
Take modolus 65 to create characters that have values from 0 - 25

[73, 70, 70, 68, 73, 90] -> [8, 5, 5, 3, 8, 25]

### Step #3

Split array into groups of size n, where n is the dimension of our square key matrix. Since our key matrix in the example is dimension 3, we will split our character array into groups of size 3.

[8, 5, 5, 3, 8, 25] -> [ [8, 5, 5], [3, 8, 25] ]

### Step #4

As opposed to when we're encrypting a plaintext message, the length of our ciphertext array should always be a multiple of n because we padded the message while encoding. Therefore, we do not need to worry about padding the character groups during decryption.

[ [8, 5, 5], [3, 8, 25] ]

### Step #5

Given our triplets, we need to convert them into column vectors and multiply each one by the inverse key matrix.


$$
[ [8, 5, 5], [3, 8, 25] ]->
\begin{pmatrix}
8 \\
5 \\
5
\end{pmatrix},
\begin{pmatrix}
3 \\
8 \\
25
\end{pmatrix}
$$



$$
\begin{pmatrix}
25 & 1 & 1 \\
22 & 1 & 5 \\
2 & 25 & 24
\end{pmatrix}
\begin{pmatrix}
8 \\
5 \\
5
\end{pmatrix} =
\begin{pmatrix}
210 \\
206 \\
261
\end{pmatrix}
$$


$$
\begin{pmatrix}
25 & 1 & 1 \\
22 & 1 & 5 \\
2 & 25 & 24
\end{pmatrix}
\begin{pmatrix}
3 \\
8 \\
25
\end{pmatrix}= 
\begin{pmatrix}
108 \\
199 \\
806
\end{pmatrix}
$$

### Step #6

We need revert the decoded message back into valid ASCII values. So, we have to take the modulos 26 to get values between 0 and 25. Then, we add back 65 to get the equivalent ASCII representation.


$$
\begin{pmatrix}
210\\
206 \\
261
\end{pmatrix}
mod 26= 
\begin{pmatrix}
2\\
24 \\
1
\end{pmatrix}+ 
\begin{pmatrix}
65 \\
65 \\
65
\end{pmatrix}= 
\begin{pmatrix}
67\\
89 \\
66
\end{pmatrix}
$$


$$
\begin{pmatrix}
108 \\
199 \\
806
\end{pmatrix}
mod 26= 
\begin{pmatrix}
4 \\
17 \\
0
\end{pmatrix}
+ 
\begin{pmatrix}
65\\
65 \\
65
\end{pmatrix}= 
\begin{pmatrix}
69 \\
82 \\
65
\end{pmatrix}
$$


### Step #7 
These column vectors need to be converted back to arrays and then to their ASCII values.

$$
\begin{pmatrix}
67\\
89 \\
66
\end{pmatrix}
 = [67, 89, 66]
 = CYB
$$



$$
\begin{pmatrix}
69\\
82 \\
65
\end{pmatrix}
 = [69, 82, 65]
 = ERA
$$

### Step #8 
Viola! Now you just have to combine these two strings. The decoded message is CYBERA.
Notice: There is an extra 'A' at the end of the message because we had to pad the plaintext before encryption. This shouldn't be too big of an issue because the message should still be human-understandable.

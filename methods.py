import numpy as np

def encode(message: str ,keyMatrix: list) -> str:
    keyMatrix = np.array(keyMatrix)
    size = len(keyMatrix)
    print(f'Original Message: {message}')
    # store message as their ascii values
    message = [ord(char) for char in message]
    print(f'Converting Into ASCII: {message}')
    # 0-25 the ascii values
    message = [char%65 for char in message]
    print(f'Taking Modulos 65 {message}')
    # split into triplets
    n_plets = [message[i:i+size] for i in range (0,len(message),size)]
    print(f'Splitting into {size}-plets: {n_plets}')
    # pad triplets with zeros 
    n_plets = [n_plet + [0] * (size-len(n_plet)) for n_plet in n_plets]
    print(f'Padding {size}-plets with zeros: {n_plets}')
    # convert into np 
    n_plets = [np.array(n_plet) for n_plet in n_plets]
    # multiply each triplet with the keyMatrix
    encoded_message = []
    for index, triplet in enumerate(n_plets):
        column = np.transpose(triplet)
        encoded_product = np.dot(keyMatrix, column)%26
        encoded_triplet = encoded_product.flatten().tolist()
        print(f'{size}-plets {index}: {encoded_triplet}')
        encoded_message += encoded_triplet
    
    encoded_message = [chr(int(value) + 65) for value in encoded_message]

    encoded_string = "".join(encoded_message)

    return encoded_string

def modinv(val, modulus):
    m, a, b = modulus, 0, 1
    if modulus == 1: return 0 # base case
    
    while val > 1:
        q = val // modulus # floor division
        modulus, val = val % modulus, modulus

        a, b = b - q * a, a
    if b < 0: b += m # make b positive
    
    return b


def inverse(keyMatrix: list) -> list:
    # M^-1 = ( 1 / |M| ) * adj(M)
    # inv  =   det_inv   * adjoint matrix

    keyMatrix = np.array(keyMatrix)
    det = int( np.round(np.linalg.det(keyMatrix)) )
    det_inv = modinv(det % 26, 26)
    
    adj = np.round( det * np.linalg.inv(keyMatrix) ).astype(int)
    adj %= 26
    keyMatrixinv = adj * det_inv
    keyMatrixinv %= 26
    keyMatrixinv = keyMatrixinv.astype(int)
    
    return keyMatrixinv.tolist()

def keytomatrix(key: str) -> list:
    
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
    n_plets = [n_plet + [0] * (3-len(n_plet)) for n_plet in n_plets]
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
    
    encoded_message = [chr(value + 65) for value in encoded_message]

    encoded_string = "".join(encoded_message)

    return encoded_string



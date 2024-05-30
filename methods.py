import numpy as np

def encode(message: str ,keyMatrix: list) -> str:
    keyMatrix = np.array(keyMatrix)
    return_string = ""
    print(f'Original Message: {message}')
    # store message as their ascii values
    message = [ord(char) for char in message]
    print(f'Converting Into ASCII: {message}')
    # 0-25 the ascii values
    message = [char%65 for char in message]
    print(f'Taking Modulos 65 {message}')
    # split into triplets
    triplets = [message[i:i+3] for i in range (0,len(message),3)]
    print(f'Splitting into Triplets: {triplets}')
    # pad triplets with zeros 
    triplets = [triplet + [0] * (3-len(triplet)) for triplet in triplets]
    print(f'Padding triplets with zeros: {triplets}')
    # convert into np 
    triplets = [np.array(triplet) for triplet in triplets]
    # multiply each triplet with the keyMatrix
    encoded_message = []
    for index, triplet in enumerate(triplets):
        column = np.transpose(triplet)
        encoded_product = np.dot(keyMatrix, column)%26
        encoded_triplet = encoded_product.flatten().tolist()
        print(f'Triplet {index}: {encoded_triplet}')
        encoded_message += encoded_triplet
    
    encoded_message = [chr(value + 65) for value in encoded_message]

    encoded_string = "".join(encoded_message)

    return encoded_string



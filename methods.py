import numpy as np

def encode(message: str ,keyMatrix: list) -> str:
    keyMatrix = np.array(keyMatrix)
    return_string = ""
    # store message as their ascii values
    message = [ord(char) for char in message]
    print(message)
    # 0-25 the ascii values
    message = [char%65 for char in message]
    print(message)
    # split into triplets
    triplets = [message[i:i+3] for i in range (0,len(message),3)]
    print(triplets)
    # pad triplets with zeros 
    triplets = [triplet + [0] * (3-len(triplet)) for triplet in triplets]
    print(triplets)
    # convert into np 
    triplets = [np.array(triplet) for triplet in triplets]
    # multiply each triplet with the keyMatrix
    encoded_message = []
    for triplet in triplets:
        column = np.transpose(triplet)
        encoded_product = np.dot(keyMatrix, column)%26
        encoded_triplet = encoded_product.flatten().tolist()
        # print(encoded_triplet)
        encoded_message += encoded_triplet
    
    encoded_message = [chr(value + 65) for value in encoded_message]

    encoded_string = "".join(encoded_message)

    return encoded_string




encode("ASFLJDA", [[6,24,1],[13,16,10],[20,17,15]])




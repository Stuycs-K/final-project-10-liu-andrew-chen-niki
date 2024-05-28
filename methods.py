import numpy as np

def encode(message: str ,keyMatrix: list) -> list:
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
    triplets = (np.array(triplet) for triplet in triplets)
    
    # for triplet in triplets:
    #     print(triplet)
    #     [print (a,b,c) for a,b,c in triplet]

    # print(triplets)




encode("ASFLJDA", [[6,24,1],[13,16,10],[20,17,15]] )


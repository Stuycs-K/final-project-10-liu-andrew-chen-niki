def encode(message ,keyMatrix):
    message = [ord(char) for char in message]
    print(message)
    message = [char%65 for char in message]
    print(message)
    # message = [ for i in range((int)(len(message)/3 + 1))]

    triplets = []
    # slice the message string into smaller string of size 3
    for i in range((int)(len(message)/3 + 1)):
        triplets.append(message[i * 3:(min((i+1) * 3, len(message)))])
    print(triplets)

encode("ASFLJDA", 0 )


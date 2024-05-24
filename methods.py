def encode(message ,keyMatrix):
    message = [ord(char) for char in message]
    print(message)
    message = [char%65 for char in message]
    print(message)
    triplets = [message[i:i+3] for i in range (0,len(message),3)]
    print(triplets)

encode("ASFLJDA", 0 )


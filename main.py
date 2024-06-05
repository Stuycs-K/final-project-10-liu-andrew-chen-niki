import sys
import math
import methods
import numpy as np

if __name__ == '__main__':
    option = input("encode or decode? (e/d): ").strip().lower()
    if option not in ['e', 'd']:
        print("invalid option")
        sys.exit(1)
    
    if option == 'e':
        # helloworld
        # 6 24 1 13 16 10 20 17 15
        # XFJMPINSGCNY
        plain = input("enter message to encode: ").strip()
        key = input("enter a square matrix to use as key (ie: a b c d): ").strip()
        matrixinput = list(map(int, key.split()))
        size = int(math.sqrt(len(matrixinput)))
        if size * size != len(matrixinput):
            print("Invalid key matrix size")
            sys.exit(1)
        keymatrix = np.array(matrixinput).reshape(size, size)
        print(f"Key matrix:\n{keymatrix}")
        encrypted = methods.encode(plain, keymatrix)
        print(f"Encoded message: {encrypted}")
    elif option == 'd':
        cipher = input("enter message to decode: ").strip()
        key = input("enter a square matrix to use as key (ie: a b c d): ").strip()
        matrixinput = list(map(int, key.split()))
        size = int(math.sqrt(len(matrixinput)))
        if size * size != len(matrixinput):
            print("Invalid key matrix size")
            sys.exit(1)
        keymatrix = np.array(matrixinput).reshape(size, size)
        print(f"Key matrix:\n{keymatrix}")
        decrypted = methods.encode(cipher, methods.inverse(keymatrix))
        print(f"Decoded message: {decrypted}")

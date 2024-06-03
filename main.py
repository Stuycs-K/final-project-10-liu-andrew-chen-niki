import sys
import math
import methods
import numpy as np

if __name__ == '__main__':
    option = input("encode or decode? (e/d): ").strip()
    if option not in ['e', 'd']: print("invalid")
    
    if option == 'e':
        # helloworld
        # 6 24 1 13 16 10 20 17 15
        # XFJMPINSGCNY
        plain = input("enter message to encode: ").strip()
        key = input("enter a square matrix to use as key (ie: a b c d): ").strip()
        matrixinput = list(map(int, input().split()))
        keymatrix = np.array(matrixinput).reshape(math.sqrt(matrixinput), math.sqrt(matrixinput))
        print(keymatrix.flatten().tolist())
        encrypted = methods.encode(plain, keymatrix)
        print(encrypted)
    if option == 'd':
        cipher = input("enter message to decode: ").strip()
        key = input("enter a square matrix to use as key: (ie: a b c d)").strip()
        matrixinput = list(map(int, input().split()))
        keymatrix = np.array(matrixinput).reshape(math.sqrt(matrixinput), math.sqrt(matrixinput))
        print(keymatrix.flatten().tolist())
        decrypted = methods.encode(cipher, keymatrix)
        print(decrypted)
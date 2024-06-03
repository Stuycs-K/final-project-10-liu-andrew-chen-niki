import sys
import math
import methods

if __name__ == '__main__':
    option = input("encode or decode? (e/d): ").strip()
    if option not in ['e', 'd']: print("invalid")
    
    if option == 'e':
        plain = input("enter message to encode: ").strip()
        key = input("enter key: ").strip()
        if (math.sqrt(len(key)).is_integer()):
            keymatrix = methods.keytomatrix(key)
            print(keymatrix.flatten().tolist())
            encrypted = methods.encode(plain, keymatrix)
            print(encrypted)
        else:
            print("invalid key")
    if option == 'd':
        cipher = input("enter message to decode: ").strip()
        key = input("enter key: ").strip()
        if (math.sqrt(len(key)).is_integer()):
            keymatrix = methods.keytomatrix(key)
            print(keymatrix.flatten().tolist())
            decrypted = methods.encode(cipher, keymatrix)
            print(decrypted)
        else:
            print("invalid key")
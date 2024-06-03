import sys
import methods

if __name__ == '__main__':
    input = input("encode or decode? (e/d): ").strip()
    if input not in ['e', 'd']: print("invalid")
    
    if input == 'e':
        plain = input("enter message to encode: ").strip()
        key = input("enter key: ").strip()
        keymatrix = methods.keytomatrix(key)
        print(keymatrix.flatten().tolist())
        encrypted = methods.encode(plain, keymatrix)
        print(encrypted)
    if input == 'd':
        cipher = input("enter message to decode: ").strip()
        key = input("enter key: ").strip()
        keymatrix = methods.keytomatrix(key)
        print(keymatrix.flatten().tolist())
        decrypted = methods.encode(cipher, keymatrix)
        print(decrypted)
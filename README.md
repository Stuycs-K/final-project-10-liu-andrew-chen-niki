[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/ecp4su41)
# Hill Cipher
## Group Info
Members: Andrew Liu and Niki Chen
## Overview
Our project includes an encoder and decoder for the encryption method, hill cipher.
## Instructions
There are a few options to how you want to input the plain/cipher text and key. You can choose between DEFAULT and CLI. DEFAULT takes in the information from the program and text file - a string message as an argument to the encoding function and the file name of the key text file as the other argument (i.e. make encode ARGS="helloworld key3.txt"). CLI waits for user input in the terminal. Running the program will output the encrypted/decrypted cipher/plain text into the command line. i.e.
```
encode or decode? (e/d): e
enter message to encode: helloworld
enter a square matrix to use as key (ie: a b c d): 6 24 1 13 16 10 20 17 15
Key matrix:
[[ 6 24  1]
 [13 16 10]
 [20 17 15]]
Original Message: HELLOWORLD
Converting Into ASCII: [72, 69, 76, 76, 79, 87, 79, 82, 76, 68]
Taking Modulos 65 [7, 4, 11, 11, 14, 22, 14, 17, 11, 3]
Splitting into 3-plets: [[7, 4, 11], [11, 14, 22], [14, 17, 11], [3]]
Padding 3-plets with zeros: [[7, 4, 11], [11, 14, 22], [14, 17, 11], [3, 0, 0]]
3-plets 0: [19, 5, 9]
3-plets 1: [8, 15, 8]
3-plets 2: [9, 18, 6]
3-plets 3: [18, 13, 8]
Encoded message: TFJIPIJSGSNI
```
There are a few options to how you want to input the plain/cipher text and key. You can choose between DEFAULT, FILE, and CLI. DEFAULT takes in the information from the program - that is, as arguments to the encoder function. FILE takes into two files: plain text and key. CLI waits for user input in the terminal. Running the program will output the encrypted/decrypted cipher/plain text into the command line. 

Tryhackme Practice Room: https://tryhackme.com/r/room/hillcipherencoding

Link to our Video: https://drive.google.com/drive/folders/1YSg7YPk33Mbo98IveXjS5ThoyDLLQX1N?usp=drive_link



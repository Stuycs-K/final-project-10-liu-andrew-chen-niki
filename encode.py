import sys
import methods

inputTextFile = sys.argv[1]

with open(inputTextFile,'r') as f:
    lines = f.readlines()

keyMatrix = [[int(num) for num in line.split()] for line in lines]

print(keyMatrix)
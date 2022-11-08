from pynput.keyboard import Key,Controller
import json

charsToBinary = open('charsToBinary.json')
data = json.load(charsToBinary)

def transformBinary(char):
    return data[char]

frase = str(input("Coloque a frase que voce quer transformar em binario : \n"))

binary = ""
for char in list(frase):
    binary = binary + transformBinary(char)

print(binary)
charsToBinary.close()
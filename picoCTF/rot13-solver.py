import string
import sys

'''
ROT13 is a simple letter substitution cipher that replaces a letter with the 13th letter after it in the alphabet.
This is a simple python implementation of ROT13
'''
def rot13(s: string) -> str:
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    shifted_letters = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
    rot13 = str.maketrans(letters, shifted_letters)
    return s.translate(rot13)

if __name__ == "__main__":
    # Collect input from the command line - super simple and bad no error handling
    input_string = sys.argv[1]

    print("Input: ", input_string)
    # Calling the ROT13 function 
    decrypted_string = rot13(input_string)
    print("Decrypted: ", decrypted_string)
    


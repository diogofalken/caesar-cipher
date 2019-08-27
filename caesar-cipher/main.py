import os
import time
from caesarcipher import CaesarCipher


def main():
    ans = True

    fileName = getFileName()
    cc = CaesarCipher(fileName)
    while ans:
        unused_variable = os.system('clear')
        print("Caeser-Cipher encryption by DC")
        print("""
        1.Encrypt file
        2.Decrypt file
        3.Exit
        """)
        ans = input("What would you like to do? ")
        if ans == "1":
            cc.encondeFile()
            print("File was encrypted with success")
            time.sleep(2)
        elif ans == "2":
            cc.decodeFile()
            print("File was decrypted with success")
            time.sleep(2)
        elif ans == "3":
            ans = False
        elif ans != "":
            print("\n Not Valid Choice Try again")


def getFileName():
    unused_variable = os.system('clear')
    print("Insert the file name with the proper extension (.txt).\n")
    print("Pay attention you need to have the file in the opposite folder what you want to do.\n")
    print("If you want to decrypt insert the file in encrypted folder.")

    return input("\nInsert the file name: ")


main()

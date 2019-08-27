import random


class CaesarCipher:
    def __init__(self, fileName):
        self.fileName = fileName
        key = 0
        for x in fileName:
            key += ord(x)
        self.key = int(str(key)[:2])

    def encondeFile(self):
        in_file = open("decrypted/" + self.fileName, "r")
        out_file = open("encrypted/" + self.fileName, "w")

        for line in in_file:
            encryptedLine = ""
            for ch in line:
                if(ch != '\n'):
                    encryptedLine += chr(ord(ch) + self.key)
            encryptedLine = encryptedLine[::-1]
            out_file.write(encryptedLine + "\n")

        in_file.close()
        out_file.close()

    def decodeFile(self):
        in_file = open("encrypted/" + self.fileName, "r")
        out_file = open("decrypted/" + self.fileName, "w")

        for line in in_file:
            encryptedLine = ""
            for ch in line:
                if(ch != '\n'):
                    encryptedLine += chr(ord(ch) - self.key)
            encryptedLine = encryptedLine[::-1]
            out_file.write(encryptedLine + "\n")

        in_file.close()
        out_file.close()

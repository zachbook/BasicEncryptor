import math

class RSA_encryptor():
    def __init__(self):
        return None
    

    def encrypt(self,public_keyn,e,file ):
        #the output file to be sent
        output_file = open("encrypted.txt","+wb")

        with open(file,"rb") as file:
            data = file.read()
            for byte in data:
                ciphered_byte = int(math.pow(byte,e) % public_keyn)
                output_file.write(int.to_bytes(ciphered_byte))
        output_file.close()
        return output_file
    
    def decrypt(self,d,N,file):
        #the decrypted file to be outputed
        output_file = open("output.txt","+wb")

        with open(file,"rb") as file:
            data = file.read()
            for byte in data:
                deciphered_byte =pow(byte,d,N)        
                output_file.write(int.to_bytes(deciphered_byte))
        print("File successfully decrypted")
        output_file.close()
        return output_file


en = RSA_encryptor()
en.encrypt(187,3,"sample.txt")
#en.decrypt(107,187,"dec.png")
        

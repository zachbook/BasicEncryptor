import math

class RSA_encryptor():
    def __init__(self):
        return None
    

    def encrypt(self,public_keyn,e,file ):
        #the output file to be sent
        with open(file,"rb") as file, open("encrypted.txt","+wb") as output_file:
            data = file.read()
            bit_length = public_keyn.bit_length()
            byte_length = (bit_length + 7) // 8
            for byte in data:
                ciphered_byte = int(math.pow(byte,e) % public_keyn)
                output_file.write(ciphered_byte.to_bytes(byte_length, byteorder='big'))

        output_file.close()
        return "encrypted.txt"
    
    def decrypt(self,d,N,file):
        #the decrypted file to be outputed
        output_file = "output_file.txt";
        with open(file,"rb") as file,  open(output_file, "wb") as output_file:
            data = file.read()
            bit_length = N.bit_length()
            byte_length = (bit_length + 7) // 8
            for byte in data:
                deciphered_byte =pow(byte,d,N)        
                output_file.write(deciphered_byte.to_bytes(byte_length,'big'))
        print("File successfully decrypted")
        return output_file



        

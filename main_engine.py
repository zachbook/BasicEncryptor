from rsa_encryptor import RSA_encryptor
import os
import sys
import socket
from enum import Enum

class State(Enum):
    SENDER =1
    RECIEVER =2

class file_sender:
    def __init__(self):
       pass

    
state = State.RECIEVER

def start_program(main_file = "output.txt"):
    HOST = "127.0.0.1"
    PORT = 65432
    if(state==State.RECIEVER):

        #instantiate sender object and generate phi and N
        sender = file_sender()
        N = sender._generate_n()
        phi = sender._generate_phi()
        
        #create a connection state and recieve the file
       
        decrypt = RSA_encryptor()
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:      
            s.bind((HOST,PORT))
            s.listen()
            conn,addr = s.accept()
            with conn, open(main_file, "wb") as f:
                while True:
                    data = conn.recv(1024)
                    f.write(data)
                    if not data:
                        break
        
            decrypt.decrypt(107,187,main_file)
    elif(state==State.SENDER):
        encrypted = RSA_encryptor()
        output_file= encrypted.encrypt(187,3,main_file)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST,PORT))
            with open(output_file, "rb") as f:
                byte = f.read()
                s.sendall( byte)
            
if __name__ =="__main__":
    if(sys.argv[1] == "send" and len(sys.argv) >2):
        state = State.SENDER
        check_if_file = os.path.isfile(sys.argv[2])
        if(check_if_file):           
            start_program(sys.argv[2])
        else:
            print("Enter a proper file path.")
    elif (sys.argv[1] =="recieve"):
        state = State.RECIEVER
        start_program()
    else:
        print("wrong arguments")
        print("do ./main_engine [recieve] or ./main_engine [send] filename.txt")





from rsa_encryptor import RSA_encrypter
import os
import sys

from enum import Enum

class State(Enum):
    SENDER =1
    RECIEVER =2

class file_sender:
    def __init__(self):
        self.__p = int.from_bytes(os.urandom(1))
        self.__q = int.from_bytes(os.urandom(1))
    
    
    #choose two random prime numbers p and q multiply them to get n
    def _generate_n(self):
        _n = self.__p*self.__q
        return _n
    
    #generate phi
    def _generate_phi(self):
        return ((self.__p-1)*(self.__q-1))

    
state = State.RECIEVER

def start_program():
    if(state==State.RECIEVER):
        #instantiate sender object and generate phi and N
        sender = file_sender()
        N = sender._generate_n
        phi = sender._generate_phi
        decrypt = RSA_encrypter()
        decrypt.decrypt(107,187,"test.txt")

    elif(state==State.SENDER):
        pass
         






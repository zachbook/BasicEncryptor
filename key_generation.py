import math
import random
import os
class key_generator:
    def __init__(self):
        self.__p = int.from_bytes(os.urandom(1))
        self.__q = int.from_bytes(os.urandom(1))
    
    '''
    This function tests whether a number is prime or not using Rabin-Miller primality test
    @param number: the number to be tested
    TODO: make it more efficient 
    '''
    def prime_test(self,number):
        #solve n-1 = 2^k *m
        n = number-1
        counter =1
        prev =0
        while(True):
            next = n%pow(2,counter)
            if(next==0):
                prev = n/pow(2,counter)
                counter+=1
            else:
                break
        #we get k and m
        k = counter-1
        m = prev
        #chose a random a such that 1 < a <n-1
        a = random.randint(2,n-1)

        '''
        first computer b0 = a^m mod number
        if that doesn't yield 1 or -1  do
        b1 
        '''
        bi = pow(a,m) % number
        if(bi == number-1 ):
            return True
        elif ( bi ==1):
            return False
        else:
            second_counter =0
            while(second_counter < k):
                bi = pow(bi,2) %number
                second_counter+=1
                if(bi==1):
                    return False
                elif bi == number - 1:
                    return True
        return True
                
    #calculate and return __p * __q    
    def find_n_phi(self):
        result = []
        __p = int.from_bytes(os.urandom(1))
        __q = int.from_bytes(os.urandom(1))
        while(not self.prime_test(__p)):
             __p = int.from_bytes(os.urandom(1))
        while(not self.prime_test(__q)):
           __q = int.from_bytes(os.urandom(1))
        result[0] = __p* __q
        result[1] = (__p-1)*(__q-1)
        return result

    def calculate_d(self,e,phi):
        return pow(e,-1,phi)


    #method for generating key
    def generate_key(self):
        result = []
        n_phi_arr = self.find_n_phi()
        n = n_phi_arr[0]
        phi = n_phi_arr[1]
        d = self.calculate_d(3,phi)
        result[0] = n
        result[1] = d
        return result

   
    

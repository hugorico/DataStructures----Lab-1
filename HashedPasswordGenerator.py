# Hashed Password Generator
# Author: Hugo Rico
# Last Modified: Sept. 19th

import hashlib

def hash_with_sha256(str): #hash_with_sha256 method to create hashed passwords
    hash_object = hashlib.sha256(str.encode('utf-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig

def main():
    
    print('Welcome to THE HASHED PASSWORD GENERATOR!\n')
    while True:
        print('Enter the REAL password you would like to hash:')
        password = input()
            
        print('Enter the Salt Value you would like to hash your password with:')
        saltValue = input()
            
        hashedPassword = hash_with_sha256(password+saltValue)
            
        print('Your Hashed Password is: ' + hashedPassword)
            
        print('Would you like to generate another hashed password? Y/N')
        decision = input()
            
        if decision == 'N':
            break
main()


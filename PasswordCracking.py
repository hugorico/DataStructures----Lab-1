# Lab 1: Password Cracking (Option C)
# Author: Hugo Rico (UTEP ID#:80531055 )
# Course: Data Structures (CS2302)
# Instructor: Diego Aguirre
# Program uses a recursive method to generate all possible passwords for a list
# of system accounts, determining each account's password in the process. 
# Program receives a .txt file containing a list of records, where each record 
# contains a username, a salt value, and a hashed password.
# ---------------------------------------------------------------------------
# Last Modified: September 19th, 2018

import hashlib
import time

def hash_with_sha256(str): #hash_with_sha256 method to create hashed passwords
    hash_object = hashlib.sha256(str.encode('utf-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig

#Password Generator works recursively to generate all possible passwords between given minimum and maximum lengths
def passGenerator(saltValue,hashPassword,minLength,maxLength): 
    if int(minLength) > int(maxLength):
        print('ERROR: Password not found. Check that user has correctly formatted password and try again.')
        passWord = 'NOT FOUND'
        return passWord
    upperBound = '9' * int(minLength) #Last password to check in a cycle
    passWord = '0' * int(minLength) #Initial password to check 
    hex_dig = hash_with_sha256(passWord+saltValue)
    if hashPassword == hex_dig:
        print('Success!')
        return passWord
    else:
        while int(passWord) < (int(upperBound)+1): 
            passWord = int(passWord) + 1
            passWord = str(passWord)
            
            #Used to format leading zero's 
            if int(minLength) > 1:
                if int(passWord) <= int((int(minLength)-1)*'9'):
                    passWord = passWord.zfill(int(minLength))
                
            hex_dig = hash_with_sha256(passWord+saltValue)
            if  hashPassword == hex_dig:
                print('Success!')
                return passWord
    newMinLength = int(minLength) + 1       
    return passGenerator(saltValue,hashPassword,str(newMinLength),maxLength)
                
def main():
    class Error(Exception):
    #Base class for other exceptions
        pass

    class ZeroValueError(Error):
    #Raised when input value is 0
        pass
    
    class LengthValueError(Error):
    #Raised when inputted minimum length value is greater than or equal to maximum length value 
        pass

    print('Welcome to THE PASSWORD BREAKER!\n')
    while True:
        print('Enter the name of the file containing the system accounts:')
        filename= input()
        
        try:
            
            while True:
                try:
                    print('Enter the minimum length of each password:')
                    minLength = int(input())
   
                    print('Enter the maximum length of each password:')
                    maxLength = int(input())
                    
                    if minLength == 0:
                        raise ZeroValueError
                    
                    if maxLength <= minLength:
                        raise LengthValueError
           
                    break
                except ValueError:
                    print('Lengths should be in integer format! Try Again.')
                except ZeroValueError:
                    print('Lengths cannot be 0! Try Again.')
                except LengthValueError:
                    print('Minimum length must be less than Maximum length! Try Again. ')
    
            #Reading of .txt file with system accounts, line by line
            startTime = time.time()
            file = open(filename + '.txt','r')
            
            while True:
                line = file.readline()
                fields = line.split(",")
        
                #Extracting data:
                userName = fields[0]
        
                #End of File Reached
                if userName == '':
                    break
        
                saltValue = fields[1]
                hashPassword = fields[2].split('\n')[0]
                passWord = passGenerator(saltValue,hashPassword,minLength,maxLength)
        
                print(userName + ' password is: ' + passWord)
                print('')
        
                if not line:
                    break
            file.close()
    
            print('Goodbye!')
            print('--- Execution Time: %s seconds ---' % (time.time() - startTime))
            break
            
        except FileNotFoundError:
            print('Oops! ' + filename + ' was not found! Try again.')
    
main()  



import hashlib

def hash_with_sha256(str):
    hash_object = hashlib.sha256(str.encode('utf-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig

def main():
    hex_dig = hash_with_sha256('This is how you hash a string with sha256')
    print(hex_dig)

main()
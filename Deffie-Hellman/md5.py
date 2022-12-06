# Python 3 code to demonstrate the
# working of MD5 (string - hexadecimal)
import hashlib

# initializing string
str2hash = "My name is Om Londhe"

# encoding GeeksforGeeks using md5 hash
# function 
byteResult = hashlib.md5(b'"My name is Om Londhe"')
# encoding GeeksforGeeks using encode()
# then sending to md5()
hexResult = hashlib.md5(str2hash.encode())

print(f"The byte equivalent of hash is : {byteResult.digest()}")
print(f"The hexadecimal equivalent of hash is : {hexResult.hexdigest()}")

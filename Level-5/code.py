import binascii
import random
import secrets
import hashlib
import os
import bcrypt

class Random_generator:

    # generates a random token
    def generate_token(self, length=8, alphabet=(
    '0123456789'
    'abcdefghijklmnopqrstuvwxyz'
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
    )):
        return ''.join(random.choice(alphabet) for i in range(length))

    # generates salt
    def generate_salt(self, rounds=22):
        return bcrypt.gensalt() 


class SHA256_hasher:

    # produces the password hash by combining password + salt because hashing
    def password_hash(self, password, salt):
        password = password.encode()
        hashed = bcrypt.hashpw(password, salt)
        return hashed.decode()
    
    # verifies that the hashed password reverses to the plain text version on verification
    def password_verification(self, password, password_hash):
        return bcrypt.checkpw(password.encode(), password_hash.encode())


class MD5_hasher:
    
    # same as above but using a different algorithm to hash which is MD5
    def password_hash(self, password):
        salt = secrets.token_hex(16)
        salted_password = password + salt
        hashed = hashlib.md5(salted_password.encode()).hexdigest()
        return f"{hashed}${salt}"

    def password_verification(self, password, password_hash):
        hashed_password, salt = password_hash.split('$')
        salted_password = password + salt
        computed_hash = hashlib.md5(salted_password.encode()).hexdigest()
        return secrets.compare_digest(computed_hash, hashed_password)   

# a collection of sensitive secrets necessary for the software to operate
PRIVATE_KEY = os.environ.get('PRIVATE_KEY')
PUBLIC_KEY = os.environ.get('PUBLIC_KEY')
SECRET_KEY = 'TjWnZr4u7x!A%D*G-KaPdSgVkXp2s5v8'
PASSWORD_HASHER = 'MD5_hasher'
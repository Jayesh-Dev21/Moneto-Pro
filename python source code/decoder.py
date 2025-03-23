import os
import base64
from dotenv import load_dotenv

load_dotenv()
encrypter1 = os.getenv("inte")
encrypter2 = os.getenv("joy")

def decode_username(encoded_username):

    base64_bytes = base64.b64decode(encoded_username)
    mixer = base64_bytes.decode("ascii")

    mixer = mixer.replace(encrypter1, "", 1).replace(encrypter2, "", 1)


    original_bytes = base64.b64decode(mixer)
    original_username = original_bytes.decode("ascii")

    return original_username


encoded_username = input("Here you go:  ")  
decoded_username = decode_username(encoded_username)
print("Decoded Username:", decoded_username)

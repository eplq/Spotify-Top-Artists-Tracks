from random import choice

def generate_random_string(length: int = 16):
    return "".join([choice("qwertyuiopasdfghjkklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789") for _ in range(length)])

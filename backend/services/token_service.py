import string
import random


def generate_token(length):
    letters = string.ascii_letters + string.digits
    token = ''.join(random.choice(letters) for i in range(length))
    return token
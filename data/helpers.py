import random
import string
def generate_email():
    letters = string.ascii_lowercase
    username = ''.join(random.choice(letters) for _ in range(8))
    cohort = "20"
    random_digits = ''.join(random.choice(string.digits) for _ in range(3))
    return f"{username}_{cohort}_{random_digits}@yandex.ru"

def generate_password():
    return str(random.randint(100000, 900000))

def generate_name():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(8))


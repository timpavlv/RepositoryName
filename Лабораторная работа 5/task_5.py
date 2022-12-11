from random import sample
import string

def get_random_password() -> str:

    chars = string.ascii_letters + string.digits
    password = "".join(sample(chars, 8))
    return password

print(get_random_password())
#
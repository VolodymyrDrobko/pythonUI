import secrets
import string

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
underscores = '_'


def get_password() -> str:
    password_s = (secrets.choice(lowercase) +
                  secrets.choice(uppercase) +
                  secrets.choice(digits) +
                  secrets.choice(underscores))
    password_f = ''.join(secrets.choice(lowercase) for _ in range(4))
    return password_s + password_f


def get_email() -> str:
    email = 'VD40'
    for _ in range(6):
        email += secrets.choice(lowercase + uppercase)
    for _ in range(2):
        email += secrets.choice(digits)
    email += '@yopmail.com'
    return email


def get_string(length: int) -> str:
    random_string = 'V'
    for _ in range(length):
        random_string += secrets.choice(lowercase + uppercase)
    return random_string

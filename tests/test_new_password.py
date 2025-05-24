import string
from password.new_password import generate_password

def test_password_characters():
    """Тест, что при генерации используются только допустимые символы"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Генерируем длинный пароль для более надежной проверки
    for char in password:
        assert char in valid_characters

def test_password_char2():
    valid_char = string.ascii_letters + string.digits + string.punctuation
    n = 500
    password = generate_password(n)
    c = 0
    for char in password:
        c += 1
    assert n == c

def test_difference():
    password1 = generate_password(100)
    password2 = generate_password(100)
    assert password1 != password2


"""
Допиши еще один тест из предложенных. Или придумай свой.
Если сможешь написать больше, то будет круто!

Тест, что длина пароля соответствует заданной
Тест, что два сгенерированных подряд пароля различаются
"""
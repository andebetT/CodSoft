import random
import string
def generate_password(minimum_length,numbers=True,special_characters=True):
    letters=string.ascii_letters
    digits=string.digits
    special=string.punctuation
    characters=letters
    if numbers:
        characters+=digits
    if special_characters:
        characters+=special
    password=""
    meet_requirement=False
    has_number=False
    has_special=False
    while not meet_requirement or len(password)<minimum_length:
        new_char=random.choice(characters)
        password+=new_char
        if new_char in digits:
            has_number=True
        elif new_char in special:
            has_special=True
        meet_requirement=True
        if numbers:
            meet_requirement=has_number
        if special_characters:
            meet_requirement=meet_requirement and has_special
    return password
print(generate_password(10))



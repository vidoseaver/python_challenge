from pprint import pformat

def to_snake_case(string):
    word = ""
    for index, letter in enumerate(string):
        if index == 0:
            word = letter.lower()
        elif letter == "-":
            word = word + "_"
        elif letter == letter.capitalize():
            word = word + "_" + letter.lower()
        else:
            word = word + letter.lower()
    return word


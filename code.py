import random

from decodingdict import *
from time import monotonic

t = monotonic()

coding_list = [qwerty_decoding, random_coding, caesar_coding_dict, last_decode]

coding = None

while True:
    if monotonic() - t > 10:
        t = monotonic()
        coding = coding_list[random.randint(0, 3)]


def codding(msg, coding_dict=coding[1]):
    encoded_text = ''
    for i in msg:
        if i.upper() in coding_dict:
            encoded_text += coding_dict[i.upper()]
        else:
            encoded_text += i

    return encoded_text


def decoding(encoded_text, coding_dict=coding[1]):
    decoding_dict = {v: k for k, v in coding_dict.items()}  # Поменяли значения и ключи местами

    decoded_text = ''
    for char in encoded_text:
        upper_char = char.upper()
        if upper_char in decoding_dict:
            decoded_text += decoding_dict[upper_char]
        else:
            decoded_text += char

    return decoded_text

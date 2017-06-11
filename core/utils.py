import os
import string
import binascii

from django.conf import settings


def get_url_hash(length=None):
    alphabet = string.digits + string.ascii_uppercase + string.ascii_lowercase
    if length is None:
        length = settings.SHORTEN_HASH_LEN
    random_num = int(binascii.b2a_hex(os.urandom(length)), 16)
    return int_to_string(
        random_num, alphabet, padding=length
    )[:length]


def int_to_string(number, alphabet, padding=None):
    output = ""
    alpha_len = len(alphabet)
    while number:
        number, digit = divmod(number, alpha_len)
        output += alphabet[digit]
    if padding:
        remainder = max(padding - len(output), 0)
        output = output + alphabet[0] * remainder
    return output

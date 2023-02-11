# -*- coding:utf-8 -*-

import random
import string


def generate_random_string(length: int = 10) -> str:
    """
    Generates a random string of a given length
    :param length: size of the string
    :return: random string
    """

    res = ''.join(random.choices(string.ascii_lowercase +
                                 string.digits, k=length))
    return res

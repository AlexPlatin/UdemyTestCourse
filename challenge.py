"""Coding Challenge Skeleton #1
This counter function purpose is to count how many english letters does your name contain.
After writing your tests, develop the counter function as needed to pass all your tests.

"""
import string


def counter(name: str) -> int:
    if not name:
        raise TypeError("Empty or None input")
    if not isinstance(name, str):
        raise TypeError("Input object not a string")
    name = "".join(name.split())
    if not name.isalpha():
        raise TypeError("NonEnglish input string")
    return len(name)


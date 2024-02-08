import re


def replace_sub_string(regex: str, replacement: str, text: str) -> str:
    return re.sub(regex, replacement, text)
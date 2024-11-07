#!/usr/bin/env python3
""" this module contains the filtered logger function """
import re
from typing import List


def filter_datum(
        fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """
    this fun=ctions returns the log message obfuscated
    Args:
        fields: a list of strings repesenting all fields to obfuscate
        redaction: a string representing by what the field will be obfuscated
        message: a string representing the log line
        separator: a string representing by which caharacter is separating
        all fields in the log line (message)

    Then use a regex to replace all occurances of certain feild value
    """
    pattern = f"({'|'.join(fields)})=([^ {separator}]+)"
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}", message)

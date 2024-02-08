#!/usr/bin/env python3
"""
function called filter_datum that returns the log message obfuscated
"""

import os
import re
import logging
import mysql.connector
from typing import List


PII_FIELDS = ('name', 'password', 'phone', 'ssn', 'email')


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str):
    """
    Function return the log message obfuscated
    Argument:
        fields: a list of string representing all field to obfucated
        redaction: a string representing by what the field will be obfuscated
        message: a string representing the log line
        seperator: a string representing by which character is seperating all
                   field in the log line
    return:
        the log message obfuscated
    """
    for field in fields:
        replace = "{}={}{}".format(field, redaction, separator)
        message = re.sub("{}=.*?{}".format(field, redaction, separator), replace, message)
    return message

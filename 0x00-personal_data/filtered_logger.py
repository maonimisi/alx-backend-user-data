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
    for f in fields:
        message = re.sub(rf"{f}=(.*?)\{separator}",
                         f'{f}={redaction}{separator}', message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Initialization"""
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """Format"""
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)

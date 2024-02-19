#!/usr/bin/env python3
"""User Authentication Module"""

import bcrypt
from bcrypt import hashpw, gensalt


def _hash_password(password: str) -> bytes:
    """Returned bytes is a salted hash of the input password"""
    return hashpw(password.encode('utf-8'), gensalt())

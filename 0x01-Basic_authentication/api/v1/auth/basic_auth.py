#!/usr/bin/env python3
"""Basic Auth implementation module
"""


from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """Basic Auth Class"""
    pass

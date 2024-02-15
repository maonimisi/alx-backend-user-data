#!/usr/bin/env python3
"""Basic Auth implementation module
"""

from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """Basic Auth Class"""

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """Returns the Base64 part of the Authorization header for a
           Basic Authentication
        """
        if authorization_header is None or type(authorization_header) != str:
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header.split("Basic ")[1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """Returns the decoded value of a Base64 string
           base64_authorization_header
        """
        if base64_authorization_header is None or \
           type(base64_authorization_header) != str:
            return None

        try:
            return base64.b64decode(base64_authorization_header).\
                decode('utf-8')
        except Exception:
            return None

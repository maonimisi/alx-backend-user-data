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
        """
        Performs base64 encoding on the authorization_header
        extract base64 of authorization header after "Basic "
        """
        if authorization_header is None or type(authorization_header) != str:
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header.split("Basic ")[1]

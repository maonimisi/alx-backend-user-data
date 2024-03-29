#!/usr/bin/env python3
"""Authentication template module"""

import os
from flask import request
from typing import List, Pattern, TypeVar


class Auth:
    """Auth Class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Requires Authentication"""
        if path is None or excluded_paths is None or not excluded_paths:
            return True
        if path in excluded_paths or path + "/" in excluded_paths:
            return False

        for e_path in excluded_paths:
            if e_path.endswith('*'):
                if path.startswith(i[:1]):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """this function add authorization header"""
        if request is not None:
            return request.headers.get('Authorization', None)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """this method gets the current user"""
        None

    def session_cookie(self, request=None):
        """This method returns the cookie value from a request."""
        if request is None:
            return None
        _my_session_id = os.getenv("SESSION_NAME")
        return request.cookies.get(_my_session_id)

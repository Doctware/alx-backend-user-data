#!/usr/bin/env python3
""" this module implement authentications """
from flask import request
from typing import List, TypeVar


class Auth:
    """ the class Auth: the unthentication class """

    def require_auth(self, path: str, excluded_path: List[str]) -> bool:
        """ returning flase for the moment """
        return False

    def authorization_header(self, request=None) -> str:
        """ returning None for the moment """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ returning none for the moment """
        return None

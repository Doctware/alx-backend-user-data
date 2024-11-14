#!/usr/bin/env python3
""" this module implement authentications """
from flask import request
from typing import List, TypeVar


class Auth:
    """ the class Auth: the unthentication class """

    def require_auth(self, path: str, excluded_path: List[str]) -> bool:
        """this methos return True if the path is not in the list
            of strings excluded path

            returns True if path is None
            returns True if excluded_path is none or empty
            returns flase is path in excluded path

        """
        if path is None or not excluded_path:
            return True

        normalize_path = path if path.endswith("/") else path + '/'

        for p in excluded_path:
            if p == normalize_path:
                return False

        return True
    

    def authorization_header(self, request=None) -> str:
        """ returning None for the moment """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ returning none for the moment """
        return None

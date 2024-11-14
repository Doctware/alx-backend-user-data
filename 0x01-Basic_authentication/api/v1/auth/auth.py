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
        """ implement authentication header 
            if request is None, return None
            if reqouest dosent contain the headers key
            Authorization retunrs None
            else return the vlaue of the rqquest auth
        """
        if request is None:
            return None

        header_auth = request.header.get("Authorization")
        if not header_auth:
            return None

        return header_auth

    def current_user(self, request=None) -> TypeVar('User'):
        """ returning none for the moment """
        return None

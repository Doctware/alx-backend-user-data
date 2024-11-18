#!/usr/bin/env python3
""" this module implement basic authentication """
from api.v1.auth.auth import Auth
from typing import TypeVar
from models.user import User
import base64


class BasicAuth(Auth):
    """ the class Basiauth thats inherit from Auth """

    def extract_base64_authorization_header(
            self, authorization_header: str
            ) -> str:
        """
        this method returns base64 part of the
        Authorization header for basic authentication
        """
        if not authorization_header or not\
                isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith("Basic "):
            return None

        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str
            ) -> str:
        """
        this method return the decoded value of Base64 string
        """
        if not base64_authorization_header or not\
                isinstance(base64_authorization_header, str):
            return None

        try:
            decode_byte = base64.b64decode(base64_authorization_header)
            return decode_byte.decode('utf-8')
        except (base64.binascii.Error, UnicodeError):
            return None

    def extract_user_credentials(
            self, decode_base64_authorization_header: str
            ) -> (str, str):
        """
        this method returns the user email and passwword from
        the base64 decode value.
        """
        if decode_base64_authorization_header is None:
            return None, None

        if not isinstance(decode_base64_authorization_header, str):
            return None, None
        if ":" not in decode_base64_authorization_header:
            return None, None

        email, password = decode_base64_authorization_header.split(":", 1)
        return email, password

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str
            ) -> TypeVar('User'):
        """
        this method return user instance base on his
        email and password
        """

        if not user_email or not isinstance(user_emial, str):
            return None
        if not user_pwd or not isinstance(user_pwd, str):
            return None

        users = User.search({"email": user_email})
        if not users or len(users) == 0:
            return None

        for user in users:
            if user.is_valid_password(user_pwd):
                return user

        return None

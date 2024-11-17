#!/usr/bin/env python3
""" this module implement basic authentication """
from api.v1.auth.auth import Auth
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

    def extract_user_credencials(
            self, decode_base64_authorization_header: str
            ) -> (str, str):
        """
        this method returns the user email and passwword from
        the base64 decode value.
        """
        if not decode_base64_authorization_header or\
                not isinstance(decode_base64_authorization_header, str):
            return (None, None)
        if ":" not in decode_base64_authorization_header:
            return (None, None)

        email, password = decode_base64_authorization_header.split(":", 1)
        return email, password

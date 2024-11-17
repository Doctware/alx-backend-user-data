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

        return iauthorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str
            ) -> str:
        """
        this method return the decoded value of Base64 string
        """
        if not authorization_header or not\
                isinstance(authorization_header, str):
            return None

        try:
            decode_byte = base64.b64decode(authorization-header)

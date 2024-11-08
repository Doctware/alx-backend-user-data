#!/usr/bin/env python3
""" this module implement filtter logger """
import logging
import re
from mysql import connector
from typing import List, Tuple
from mysql.connector import connection


PII_FIELDS: Tuple[str, ...] = ("name", "email", "phone", "ssn", "password")


def filter_datum(
        fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """
    this function returns the log message obfuscated
    Args:
        fields: a list of strings repesenting all fields to obfuscate
        redaction: a string representing by what the field will be obfuscated
        message: a string representing the log line
        separator: a string representing by which caharacter is separating
        all fields in the log line (message)

    Then use a regex to replace all occurances of certain feild value
    """
    pattern = f"({'|'.join(fields)})=([^ {separator}]+)"
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}", message)


class RedactingFormatter(logging.Formatter):
    """ Redacting formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ Inisializing """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ the format module """
        record.msg = filter_datum(
                        self.fields, self.REDACTION, record.getMessage(),
                        self.SEPARATOR
                    )

        return super().format(record)


def get_logger() -> logging.Logger:
    """ this function creates and configures a
        logger for user with a redacting formatter """

    logger = logging.logger.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(fields=PII_FIELDS))

    logger.addHandler(handler)

    return logger


def get_db() -> connection.MySQLConnection:
    """
    connect to the database using credencial from environment variables
    """
    username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    database = os.getenv("PERSONAL_DATA_DB_NAME")

    return mysql.connector.connect(
            user=username,
            password=password,
            host=host,
            database=database
    )

"""
Run this with:

$ python app.py

and with:

$ PORT=8080 python app.py
"""
from chick import BaseConfig


class Config(BaseConfig):

    HOST = '127.0.0.1'
    PORT: int = 8000
    DEBUG: bool = False


print(Config.HOST)

import json

class Config(object):

    def __init__(self) -> None:
        with open("config.json", 'rb') as file:
            self.info = json.load(file)
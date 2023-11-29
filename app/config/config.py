from .env import EMAIL, PASSWORD


class Config():
    def __init__(self) -> None:
        self.EMAIL = EMAIL
        self.PASSWORD = PASSWORD
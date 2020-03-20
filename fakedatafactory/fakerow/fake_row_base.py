from abc import ABCMeta, abstractmethod
from faker import Faker


class FakeRowBase(metaclass=ABCMeta):

    fake = Faker()

    @abstractmethod
    def __init__(self):
        raise TypeError(
            "Can't instantiate. Need to implement __init__ method"
        )

    @staticmethod
    def generate_email(first_name, last_name, domain):
        """Generates email address using provided arguments
        """
        return (first_name + last_name + "@" + domain).lower()

    @classmethod
    def get_new_row(cls):
        """Allows the class's instance to be called
        without arguments
        """
        return cls.__call__()

    def to_dict(self):
        """Returns A dictionary bject used to
        store an object's (writable) attributes
        """
        return self.__dict__

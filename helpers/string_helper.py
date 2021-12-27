import re


class StringHelper:
    @staticmethod
    def is_float(value):
        if isinstance(value, float):
            return True
        if isinstance(value, str) and re.search(r'^-?[0-9]+\.[0-9]+$', value):
            return True
        return False

    @staticmethod
    def is_int(value):
        if isinstance(value, int):
            return True
        if isinstance(value, str) and re.search(r'^-?[0-9]+$', value):
            return True
        return False

    @staticmethod
    def is_number(value):
        return StringHelper.is_int(value) or StringHelper.is_float(value)

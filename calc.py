import math

class Calc:

    @staticmethod
    def add(arg1, arg2):
        return arg1 + arg2

    @staticmethod
    def subtract(arg1, arg2):
        return arg1 - arg2

    @staticmethod
    def multiply(arg1, arg2):
        return arg1 * arg2

    @staticmethod
    def divide(arg1, arg2):
        try:
            result = arg1 / arg2
        except ZeroDivisionError:
            return None

        return result

    @staticmethod
    def sqrt(arg):
        try:
            result = math.sqrt(arg)
        except ValueError:
            return None

        return result

"""
null spectrum (needed as other formulations require parameters
 to be set before instantiation of Formulae)
"""


class Null:
    def __init__(self, _):
        pass

    @staticmethod
    def cdf(const, T):
        pass

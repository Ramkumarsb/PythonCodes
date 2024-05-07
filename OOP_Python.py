#  Object Oriented Programming
'''
All the Values in Python are object.
Class helps us define Objects.
Note:
    1. As With functions, there are predefined classes in python. But user can also define his own class.
    2. OOP languages, provide three fundamental features that support OOP ---
        a. encapsulation.
        b. inheritance.
        c. polymorphism.
'''

class Fraction(object):
    def __init__(self,numerator,denominator):
        "Inits Fraction with values numerator and denominator."

        self.__numerator = numerator         # Private Instance variables.
        self.__denominator = denominator
        self.reduce()

    def getNumerator(self):
        """Return the numerator of a fraction"""
        return self.__numerator
    def getDenominator(self):
        "Return the denominator of fraction."
        return self.__denominator
    def setNumerator(self,value):
        "Set the numerator of a fraction to the provided value."
        self.__numerator = value
    def setDenominator(self,value):
        """Set the denominator of a fraction to the provided value.
            Raises a ValueError exception if a value of Zero is provided.
        """
        if value == 0:
            raise ValueError('Divide by Zero error')
        self.__denominator = value
frac1 = Fraction(1,2)
frac2 = Fraction(6,8)



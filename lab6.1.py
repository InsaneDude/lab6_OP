import math
import sympy as sym
from abc import ABC, abstractmethod


class MethodClass(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def used_var(self):
        pass

    @abstractmethod
    def sin_var(self):
        pass

    @abstractmethod
    def sin_diff_var(self):
        pass

    @abstractmethod
    def cos_var(self):
        pass

    @abstractmethod
    def cos_diff_var(self):
        pass


class CreatingVariable(MethodClass):
    def used_var(self):
        used_variable = sym.Symbol(input("Введіть змінну, яку хочете використовувати : "))
        input_expr = input("Введіть вираз із вашою змінною : ")
        if str(used_variable) not in str(input_expr):
            print("Змінна введена невірно.")
            quit()
        return input_expr

    def sin_var(self):
        pass

    def sin_diff_var(self):
        pass

    def cos_var(self):
        pass

    def cos_diff_var(self):
        pass


class SinFromVariable(CreatingVariable):
    def sin_var(self):
        sin_from_variable = sym.sin(self.used_var())
        print("sin від вашою змінної :", sin_from_variable)
        return sin_from_variable


class DiffSinFromVariable(SinFromVariable):
    def sin_diff_var(self):
        sin_differed_var = sym.diff(self.sin_var())
        print("Похідна від sin :", sin_differed_var)


k = DiffSinFromVariable()
k.sin_diff_var()
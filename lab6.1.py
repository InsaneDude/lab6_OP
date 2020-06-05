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
            print("Змінна або вираз введені невірно.")
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
        print("sin від заданого виразу :", sin_from_variable)
        return sin_from_variable


class DiffSinFromVariable(SinFromVariable):
    def sin_diff_var(self):
        sin_differed_var = sym.diff(self.sin_var())
        print("Похідна від заданого виразу :", sin_differed_var)


class CosFromVariable(CreatingVariable):
    def cos_var(self):
        cos_from_variable = sym.cos(self.used_var())
        print("cos від заданого виразу :", cos_from_variable)
        return cos_from_variable


class DiffCosFromVariable(CosFromVariable):
    def cos_diff_var(self):
        cos_differed_var = sym.diff(self.cos_var())
        print("Похідна від заданого виразу :", cos_differed_var)


choosing_method = int(input("Введіть 1 (якщо sin) чи 2 (якщо cos) для обрання відповідного режиму : "))
if choosing_method is 1:
    choosed_algo = DiffSinFromVariable()
    choosed_algo.sin_diff_var()
if choosing_method is 2:
    choosed_algo = DiffCosFromVariable()
    choosed_algo.cos_diff_var()
from abc import ABC, abstractmethod


class MathStrategy(ABC):
    @abstractmethod
    def execute(self, a: float, b: float) -> float:
        pass

class Addition(MathStrategy):
    def execute(self, a: float, b: float) -> float:
        return a + b

class Subtraction(MathStrategy):
    def execute(self, a: float, b: float) -> float:
        return a - b


class Multiplication(MathStrategy):
    def execute(self, a: float, b: float) -> float:
        return a * b

class Division(MathStrategy):
    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Деление на ноль невозможно.")
        return a / b

class Calculator:

    def __init__(self, strategy: MathStrategy = None):
        self._strategy = strategy

    def set_strategy(self, strategy: MathStrategy):
        self._strategy = strategy

    def calculate(self, a: float, b: float) -> float:
        if not self._strategy:
            raise ValueError("Стратегия выполнения не установлена.")
        return self._strategy.execute(a, b)

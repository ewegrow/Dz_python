from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def speak(self) -> str:
        pass

class Dog(Animal):

    def speak(self) -> str:
        return "Гав! Гав!"

class Cat(Animal):

    def speak(self) -> str:
        return "Мяу! Мяу!"

class AnimalFactory:

    def create_animal(self, animal_type: str) -> Animal:
        target_type = animal_type.strip().lower()

        if target_type == "dog":
            return Dog()
        elif target_type == "cat":
            return Cat()
        else:
            raise ValueError(f"Неизвестный тип животного: '{animal_type}'")



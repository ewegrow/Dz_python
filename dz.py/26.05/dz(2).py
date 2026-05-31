
class BeeElephant:
    def __init__(self, bee_part: int, elephant_part: int):
        self._bee = max(0, min(100, bee_part))
        self._elephant = max(0, min(100, elephant_part))

    def fly(self) -> bool:
        return self._bee >= self._elephant

    def trumpet(self) -> str:
        if self._elephant >= self._bee:
            return "tu-doo"   
        else:
            return "wzzz"  

    def eat(self, meal:str, value: int):
        if meal not in ("nectar", "grass"):
            return
        
        if meal == "nectar":
            self._bee += value
            self._elephant -= value
        
        elif meal == "grass":
            self._elephant += value
            self._bee -= value

        self._bee = max(0, min(100, self._bee))
        self._elephant = max(0, min(100, self._elephant))

    def __str__(self) -> str:
        return (f"ПчелоСлон (Пчела: {self._bee}, Слон: {self._elephant})")
    
if __name__ == "__main__":
    monster = BeeElephant(30, 70)
    print(monster)


    print(f"Может летать ? {monster.fly()}")
    print(f"Звук: {monster.trumpet()}")

    print("Пчелослон ест нектар ?")
    monster.eat("nectar", 40)
    print(monster)

    print(f"Теперь может летать ? {monster.fly()}")
    print(f"Звук: {monster.trumpet()}")

    print("Проверка ограничений")
    monster.eat("grass", 150)
    print(monster)

class Bus:
    def __init__(self, max_seats: int, max_speed: float):
        self.speed: float = 0
        self.max_seats:int = max_seats
        self.max_speed:float = max_speed
        self.passengers: list[str] = []


        self.seats_map: dict[int, str | None] = {seat:None for seat in range(1, max_seats + 1)}


    @property
    def has_empty_seats(self) -> bool:
        return len(self.passengers) < self.max_seats
    
    def increase_speed(self, value:float) -> None:
        if value < 0:
            raise ValueError("Значение должно быть положительным")
        self.speed = min(self.speed + value, self.max_speed)


    def decrese_spped(self, value:float) -> None:
        if value < 0:
            raise ValueError("Значение должно быть положительным")
        self.speed = max(self.speed - value, 0)

    def board_passengers(self, *passengers: str) -> None:
        for passenger in passengers:
            if not self.has_empty_seats:
                print(f"Автобус полон. Пассажиру {passenger} не хватило места.")
                break

    def dischange_passengers(self, *passengers:str) -> None:
        for passenger in passengers:
            if passenger in self.passengers:
                self.passengers.remove(passenger)
                for seat, occupant in self.seats_map.items():
                    if occupant == passenger:
                        self.seats_map[seat] = None
                        break
            else:
                print(f"Пассажира: {passenger} нет в автобусе")

    def __contains__(self, passenger:str) -> bool:
        return passenger in self.passengers
    
    def __iadd__(self, passenger:str):
        self.board_passengers(passenger)
        return self
    
    def __isub__(self, passenger: str):
        self.dischange_passengers(passenger)
        return self
    
    def __str__(self) -> str:
        return (f"Автобус (Скорость: {self.speed} / {self.max_speed}),"
                f"Места: {len(self.self.passengers)} / {self.self.max_seats},"
                f"Свободные места: {self.self.has_empty_seats})")
        

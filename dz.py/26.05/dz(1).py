class Product:
    def __init__(self, name:str, store:str, price:float):
        self._name = name
        self._store = store
        self._price = price


    @property
    def name(self) -> str:
        return self._name
    
    @property
    def store(self) -> str:
        return self._store
    
    @property
    def price(self) -> float:
        return self._price
    
    def __add__(self, other) -> float:
        return self._price + other.price
    
    def __str__(self) -> str:
        return f"Товар: {self._name}, Магазин: {self._store}, Цена: {self._price} BYN"
    
class Warehouse:
    def __init__(self):
        self._products = []

    def add_products(self, product = Product):
        self._products.append(product)

    def print_by_index(self, index:int):
        if 0 <= index < len(self._products):
            print(self._products[index])
        else:
            print(f"Ошибка: Индекс {index} вне диапазона склада.")
    
    def print_by_name(self, name:str):
        found = False
        for product in self._products:
            if product.name == name:
                print(product)
                found = True

        if not found:
            print(f"Товар с названием {name} не найден")

    def sort_by_name(self):
        self._products.sort(key=lambda p: p.name)

    def sort_by_store(self):
        self._products.sort(key=lambda p: p.store)

    def sort_by_price(self):
        self._products.sort(key=lambda p: p.price)

    def print_all(self):
        if not self._products:
            print("Склад пуст.")
            return
        for product in self._products:
            print(product)
        print("-" * 50)

if __name__ == "__main__":
    wh = Warehouse()

    wh.add_products(Product("Молоко", "Евроопт", 2.50))
    wh.add_products(Product("Хлеб", "Соседи", 1.80))
    wh.add_products(Product("Кофе", "Алми", 15.20))
    wh.add_products(Product("Молоко", "Корона", 3.10))

    print("Исходный склад")
    wh.print_all()

    print("Поиск по индексу 2")
    wh.print_by_index(2)

    print(" Поиск по имени 'Молоко' ")
    wh.print_by_name("Молоко")

    print("Сортировка по названию")
    wh.sort_by_name()
    wh.print_all()

    print("Сортировка по цене")
    wh.sort_by_price()
    wh.print_all()   

    p1 = Product("Чай", "Грин", 5.50)
    p2 = Product("Печенье", "Грин", 4.20)

    total_price = p1 + p2
    print(f"Сумма цен товаров {p1.name} b {p2.name} : {total_price} BYN ")


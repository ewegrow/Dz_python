class Pizza:
    def __init__(self):
        self.size = None
        self.cheese = False
        self.pepperoni = False
        self.mushrooms = False
        self.onions = False
        self.bacon = False

    def __str__(self):
        ingredients = []
        if self.cheese: ingredients.append("сыр")
        if self.pepperoni: ingredients.append("пепперони")
        if self.mushrooms: ingredients.append("грибы")
        if self.onions: ingredients.append("лук")
        if self.bacon: ingredients.append("бекон")
        
        return f"Пицца (Размер: {self.size}, Ингредиенты: {', '.join(ingredients) if ingredients else 'нет'})"


class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def set_size(self, size: str):
        self.pizza.size = size
        return self 

    def add_cheese(self):
        self.pizza.cheese = True
        return self

    def add_pepperoni(self):
        self.pizza.pepperoni = True
        return self

    def add_mushrooms(self):
        self.pizza.mushrooms = True
        return self

    def add_onions(self):
        self.pizza.onions = True
        return self

    def add_bacon(self):
        self.pizza.bacon = True
        return self

    def build(self) -> Pizza:
        return self.pizza


class PizzaDirector:
    def __init__(self, builder: PizzaBuilder):
        self.builder = builder

    def make_pizza(self, pizza_type: str) -> Pizza:
        if pizza_type == "Маргарита":
            return (self.builder
                    .set_size("L")
                    .add_cheese()
                    .build())
        
        elif pizza_type == "Мясная":
            return (self.builder
                    .set_size("XL")
                    .add_cheese()
                    .add_pepperoni()
                    .add_bacon()
                    .build())
        
        elif pizza_type == "Особая":
            return (self.builder
                    .set_size("M")
                    .add_cheese()
                    .add_mushrooms()
                    .add_onions()
                    .build())
            
        else:
            return self.builder.set_size("M").build()
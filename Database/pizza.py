import abc
# import admin
from Database import admin



class Pizza(abc.ABC):

    @abc.abstractmethod
    def get_price(self):
        pass

    @abc.abstractmethod
    def get_status(self):
        pass


class ConcretePizza(Pizza):
    def __init__(self, name, status, price):
        self.name = name
        self.status = status
        self.price = price

    def get_price(self):
        return self.price

    def get_status(self):
        return self.name + ':\n' + self.status


class Margherita(Pizza):
    __pizza_price = 10.0

    def get_price(self):
        return self.__pizza_price

    def get_status(self):
        return "Margherita:\nTomato sauce, Mozzarella cheese, Leaves of Basil"


class Pepperoni(Pizza):
    __pizza_price = 14.0

    def get_price(self):
        return self.__pizza_price

    def get_status(self):
        return "Pepperoni:\nCheese Mozzarella, Pepperoni, Beef"


class PizzaDecorator(Pizza):
    def __init__(self, pizza):
        self.pizza = pizza

    def get_price(self):
        return self.pizza.get_price()

    def get_status(self):
        return self.pizza.get_status()


class Tomato(PizzaDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self._tomato_price = 2.0

    @property
    def price(self):
        return self._tomato_price

    def get_price(self):
        return super().get_price() + self._tomato_price

    def get_status(self):
        return super().get_status() + ", Tomato"


class Cheese(PizzaDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self._cheese_price = 1.5

    @property
    def price(self):
        return self._cheese_price

    def get_price(self):
        return super().get_price() + self._cheese_price

    def get_status(self):
        return super().get_status() + ", Cheese"


class Beef(PizzaDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self._beef_price = 3

    @property
    def price(self):
        return self._beef_price

    def get_price(self):
        return super().get_price() + self._beef_price

    def get_status(self):
        return super().get_status() + ", Beef"
#=============================== Business Layer ====================================


class PizzaBuilder:
    def __init__(self, pizza_type, row=None):
        self.pizza_type = pizza_type
        if pizza_type == "ConcretePizza":
            self.pizza = ConcretePizza(row[0], row[1], row[2])
            self.name = row[0]
            self.status = row[1]
            self.price = row[2]
        else:
            self.pizza = eval(pizza_type)()
        self.extention_list = []

    def add_extension(self, extention):
        self.pizza = eval(extention)(self.pizza)
        self.extention_list.append(extention)

    def remove_extension(self, extention):
        if extention in self.extention_list:
            self.extention_list.remove(extention)

        if self.pizza_type == "ConcretePizza":
            self.pizza = ConcretePizza(self.name, self.status, self.price)
        else:
            self.pizza = eval(self.pizza_type)()
        for ex in self.extention_list:
            self.pizza = eval(ex)(self.pizza)

    def get_price(self):
        return self.pizza.get_price()

    def get_status(self):
        return self.pizza.get_status()


#==================== CLient Part ===================================================
# my_pizza = ConcretePizza()
# my_pizza = Tomato(my_pizza)
# print(my_pizza.get_price())
# print(my_pizza.get_status())


# pizza = PizzaBuilder("Pepperoni")
# pizza.add_extention("Tomato")
# pizza.add_extention("Cheese")
# pizza.add_extention("Cheese")

# print(pizza.get_status())
# print(pizza.get_price())

# pizza.remove_extention("Tomato")
# print("-" * 60)
# print(pizza.get_status())
# print(pizza.get_price())


# obj = ConcretePizza("lahmacun", "dadli", 3)

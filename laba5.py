class Sneakers:
    def __init__(self, brand="Невідомий", size=0, color="Невідомий",
                 price=0, quantity=0, material="Невідомий", numberOfSales=0):
        self.__brand = brand
        self.__size = size
        self.__color = color
        self.__price = price
        self.__quantity = quantity
        self.__material = material
        self.__numberOfSales = numberOfSales

    def get_brand(self):
        return self.__brand

    def get_size(self):
        return self.__size

    def get_color(self):
        return self.__color

    def get_price(self):
        return self.__price

    def get_quantity(self):
        return self.__quantity

    def get_material(self):
        return self.__material

    def get_numberOfSales(self):
        return self.__numberOfSales

    def set_price(self, price):
        self.__price = price

    def set_quantity(self, quantity):
        self.__quantity = quantity

    def __str__(self):
        return (f"Бренд: {self.__brand}, розмір: {self.__size}, "
                f"колір: {self.__color}, ціна: {self.__price} грн, "
                f"кількість: {self.__quantity}, матеріал: {self.__material}, "
                f"продажі: {self.__numberOfSales}")

    def __del__(self):
        print("Об'єкт кросівок видаляється")


class SportShoeStore:
    def __init__(self):
        self.sneakers = []

    def add_sneakers(self, shoe):
        self.sneakers.append(shoe)

    def show_sneakers(self):
        for shoe in self.sneakers:
            print(shoe)

    def sort_by_price(self):
        self.sneakers.sort(key=lambda shoe: shoe.get_price())

    def sort_by_quantity(self):
        self.sneakers.sort(key=lambda shoe: shoe.get_quantity())

    def top_popular(self):
        popular = sorted(self.sneakers,
                         key=lambda shoe: shoe.get_numberOfSales(),
                         reverse=True)

        print("\nТоп-3 найпопулярніших кросівок:")
        for shoe in popular[:3]:
            print(shoe)


def main():
    shoe1 = Sneakers("Nike", 42, "Чорний", 3500, 10, "Шкіра", 150)
    shoe2 = Sneakers("Adidas", 40, "Білий", 2800, 15, "Текстиль", 120)
    shoe3 = Sneakers("Puma", 43, "Сірий", 2200, 8, "Замша", 90)
    shoe4 = Sneakers("New Balance", 41, "Синій", 4000, 5, "Замша", 200)

    store = SportShoeStore()

    store.add_sneakers(shoe1)
    store.add_sneakers(shoe2)
    store.add_sneakers(shoe3)
    store.add_sneakers(shoe4)

    print("Весь асортимент кросівок:")
    store.show_sneakers()

    print("\nСортування за ціною:")
    store.sort_by_price()
    store.show_sneakers()

    print("\nСортування за кількістю:")
    store.sort_by_quantity()
    store.show_sneakers()

    store.top_popular()

    print("\nЗміна ціни перших кросівок:")
    shoe1.set_price(3000)
    print(shoe1)

if __name__ == "__main__":
    main()

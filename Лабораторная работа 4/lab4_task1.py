class Conifers:
    """
    Базовый класс Хвойные деревья.
    Attributes:
    name(str): название дерева
    height(int): высота дерева
    age(int): возраст дерева
    """
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        """
        Метод, который должен быть реализован
        в дочерних классах для того, чтобы показать,
        на сколько см выросло дерево за год.

        Returns:
            int: кол-во см за год
        """
        pass

    def age(self):
        """
        Метод, который показывает возраст дерева.
        Returns:
            int: сколько лет дереву
        """
        pass

    def __str__(self):
        return f"{self.__class__.__name__}: {self.name}, возраст {self.age} лет."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, height={self.height!r}, age={self.age!r})"


class Spruce(Conifers):
    """
    Дочерний класс Ель, наследуется от
    базового класса Хвойные деревья
    """
    def __init__(self, height: int, age: int, cut_down: int):
        super().__init__(height, age)
        self.cut_down = cut_down
    def grow(self):
        return self.grow

    def cut_down(self):
        """
        Метод только для Ели: сколько деревьев срубают
        перед Новым Годом
        Returns:
            int: количество деревьев в год
        """
        pass


class Larch(Conifers):
    """
    Дочерний класс Лиственница, наследуется от
    базового класса Хвойные деревья.
    """
    def __init__(self, height: int, age: int, fallen_leaves: bool):
        super().__init__(height, age)
        self.fallen_leaves = fallen_leaves
    def age(self):
        return self.age

    def fallen_leaves(self):
        """
        Метод только для Лиственницы: сбросить хвою на зиму
        Returns:
            bool: да или нет
        """
        pass




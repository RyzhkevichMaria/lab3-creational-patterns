from abc import ABC, abstractmethod


# Абстрактные продукты
class Chair(ABC):
    @abstractmethod
    def sit_on(self):
        pass


class Sofa(ABC):
    @abstractmethod
    def lie_on(self):
        pass


# Конкретные продукты — Модерн
class ModernChair(Chair):
    def sit_on(self):
        return "Сижу на современном кресле"


class ModernSofa(Sofa):
    def lie_on(self):
        return "Лежу на современном диване"


# Конкретные продукты — Викторианский стиль
class VictorianChair(Chair):
    def sit_on(self):
        return "Сижу на викторианском кресле"


class VictorianSofa(Sofa):
    def lie_on(self):
        return "Лежу на викторианском диване"


# Абстрактная фабрика
class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self) -> Chair:
        pass

    @abstractmethod
    def create_sofa(self) -> Sofa:
        pass


# Конкретные фабрики
class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return ModernChair()

    def create_sofa(self) -> Sofa:
        return ModernSofa()


class VictorianFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return VictorianChair()

    def create_sofa(self) -> Sofa:
        return VictorianSofa()


# Демонстрация
if __name__ == "__main__":
    modern = ModernFurnitureFactory()
    print(modern.create_chair().sit_on())  # Сижу на современном кресле
    print(modern.create_sofa().lie_on())   # Лежу на современном диване

    victorian = VictorianFurnitureFactory()
    print(victorian.create_chair().sit_on())  # Сижу на викторианском кресле
    print(victorian.create_sofa().lie_on())   # Лежу на викторианском диване

from abc import ABC, abstractmethod


class Transport(ABC):
    """Абстрактный продукт — транспорт."""
    
    @abstractmethod
    def deliver(self):
        pass


class Truck(Transport):
    """Конкретный продукт — грузовик."""
    
    def deliver(self):
        return "Доставка грузовиком по дороге"


class Ship(Transport):
    """Конкретный продукт — корабль."""
    
    def deliver(self):
        return "Доставка кораблём по морю"


class TransportFactory(ABC):
    """Абстрактный создатель."""
    
    @abstractmethod
    def create_transport(self) -> Transport:
        pass

    def plan_delivery(self):
        """Операция, использующая продукт."""
        transport = self.create_transport()
        return f"Планируем доставку: {transport.deliver()}"


class RoadLogistics(TransportFactory):
    """Конкретный создатель для дорог."""
    
    def create_transport(self) -> Transport:
        return Truck()


class SeaLogistics(TransportFactory):
    """Конкретный создатель для моря."""
    
    def create_transport(self) -> Transport:
        return Ship()


# Демонстрация
if __name__ == "__main__":
    road = RoadLogistics()
    print(road.plan_delivery())  # Планируем доставку: Доставка грузовиком по дороге

    sea = SeaLogistics()
    print(sea.plan_delivery())   # Планируем доставку: Доставка кораблём по морю

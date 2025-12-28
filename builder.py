from abc import ABC, abstractmethod


class Computer:
    """Сложный продукт — компьютер."""
    
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None
        self.gpu = None

    def __str__(self):
        return f"Компьютер: CPU={self.cpu}, RAM={self.ram}, Storage={self.storage}, GPU={self.gpu}"


class ComputerBuilder(ABC):
    """Абстрактный строитель."""
    
    def __init__(self):
        self.computer = Computer()

    @abstractmethod
    def build_cpu(self):
        pass

    @abstractmethod
    def build_ram(self):
        pass

    @abstractmethod
    def build_storage(self):
        pass

    def build_gpu(self):
        pass  # опционально

    def get_computer(self) -> Computer:
        return self.computer


class GamingPCBuilder(ComputerBuilder):
    """Конкретный строитель для игрового ПК."""
    
    def build_cpu(self):
        self.computer.cpu = "Intel Core i9"

    def build_ram(self):
        self.computer.ram = "32 GB DDR5"

    def build_storage(self):
        self.computer.storage = "2 TB SSD"

    def build_gpu(self):
        self.computer.gpu = "NVIDIA RTX 4090"


class OfficePCBuilder(ComputerBuilder):
    """Конкретный строитель для офисного ПК."""
    
    def build_cpu(self):
        self.computer.cpu = "Intel Core i5"

    def build_ram(self):
        self.computer.ram = "16 GB DDR4"

    def build_storage(self):
        self.computer.storage = "512 GB SSD"

    def build_gpu(self):
        self.computer.gpu = "Встроенная графика"


class Director:
    """Директор — управляет процессом сборки."""
    
    def construct(self, builder: ComputerBuilder):
        builder.build_cpu()
        builder.build_ram()
        builder.build_storage()
        builder.build_gpu()


# Демонстрация
if __name__ == "__main__":
    director = Director()

    gaming_builder = GamingPCBuilder()
    director.construct(gaming_builder)
    print(gaming_builder.get_computer())
    # Компьютер: CPU=Intel Core i9, RAM=32 GB DDR5, Storage=2 TB SSD, GPU=NVIDIA RTX 4090

    office_builder = OfficePCBuilder()
    director.construct(office_builder)
    print(office_builder.get_computer())
    # Компьютер: CPU=Intel Core i5, RAM=16 GB DDR4, Storage=512 GB SSD, GPU=Встроенная графика

class Singleton:
    """Паттерн Singleton — гарантирует, что у класса будет только один экземпляр."""
    
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Создаём единственный экземпляр Singleton")
            cls._instance = super(Singleton, cls).__new__(cls)
            cls._instance.value = 0
        return cls._instance

    def increment(self):
        self.value += 1
        print(f"Значение: {self.value}")


if __name__ == "__main__":
    s1 = Singleton()
    s1.increment() 
    s2 = Singleton()
    s2.increment() 

    print(f"s1 is s2: {s1 is s2}")  

class Human():
    @abstractmethod
    def walk(self):
        pass
    @abstractmethod
    def run(self):
        pass
    @abstractmethod
    def jump(self):
        pass

class Men(Human):
    # overriding abstract method
    def walk(self):
        print("sing the song")

class Child()
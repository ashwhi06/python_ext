class Car:
    def __init__(self, name) -> None:
        self.name = name
        print(f"Car created for, {self.name}.")
         
    def talk(self, driver):
        print(f"Hi, from, {driver}")
    
    class ElectricCar(Car):
        def __init__(self, driver, type):
            #Call constructor of parent class
            self.type = type
            super().__init__(driver)
            print(f"I am a {self.type} and I am driven by {driver}")


    electricCar = ElectricCar("John", "Electric")
    electricCar.talk("Ashe")
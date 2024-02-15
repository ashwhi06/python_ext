class Car:
  def __init__(self, name, max_speed):
    self.name = name
    self.max_speed = max_speed

  def start(self):
    print('Vroom!')

  def talk(self, driver):
    print(f'Hello, {driver}, I am {self.name}.')

# myCar = Car('Kitt', 180)
# myOtherCar = Car('Speedy', 55)

# myCar.talk('Michael')

class Race:
    def __init__(self,name, driver_limit) -> None:
        self.name = name
        self.driver_limit = driver_limit
        self.drivers = []
    def add_driver(self,driver):
        if len(self.drivers) < self.driver_limit:
            self.drivers.append(driver)
            return True
        else:   
            return False
# my_course = Race('Seattle 500', 4)
# print(my_course.name, my_course.driver_limit, my_course.drivers)

# # prints Seattle 500 4 []
   
class Driver:
    number_of_drivers = 0
    def __init__(self, name, age, ranking) -> None:
        self.name = name
        self.age = age
        self.ranking = ranking
#get_average_ranking
#Return the average ranking of all drivers
    def get_ranking(self):
        avg = 0
        for driver in self.drivers:
            avg += driver.ranking
        return avg/len(self.drivers)
# race = Race("F1", 4, Driver("Lewis Hamilton", 36, 83),Driver("Eliud Kipchog", 36, 95), Driver("Sebastian Vettel", 34, 76),Driver("Ayrton Senna", 34, 99))
# # print(Race.get_ranking(4))

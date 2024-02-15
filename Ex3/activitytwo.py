class Person:
    def __init__(self,in_name,in_age):
        self.name = in_name
        self.age = in_age
      
    def get_name(self):
        return self.name

# Next, let's try defining a class to represent a customer. 
# A customer is a person, so the Customer class inherits from the Person class, and should call the Person constructor inside the Customer constructor. 
# In addition to their name and age, a customer should have two Booleans, one each for whether they have a ticket for the zoo, and whether they are currently in the zoo. 
# Initialize these Booleans to false in the constructor for your Customer class.
class Customer(Person):
    def __init__(self,in_name,in_age):
        super().__init__(in_name,in_age)
        self.has_ticket = False
        self.in_zoo = False
        
    def buy_ticket(self):
        if self.age >= 12:
            print(f"{self.name} has bought a child ticket.")
        else: 
            print(f"{self.name} has bought a adult ticket.")
            self.has_ticket = True
            
    def enter_zoo(self,zoo):
        if self.has_ticket:
            self.in_zoo = True
            self.has_ticket = False
            zoo.add_customer(self.name)
            print(f"{self.name} has entered {zoo.name}")
        else:
            print(f"{self.name} does not have a ticket to enter Zoo.")
            
    def exit_zoo(self,zoo):
        if self.in_zoo:
            self.in_zoo = False
            zoo.remove_customer(self.name)
            print(f"{self.name} has left {zoo.name}")
        else:
            print(f"{self.name} is not in {zoo.name}")
class Zoo:
    def __init__(self,name="Local Zoo"):
        self.name = name
        self.animals = []
        self.customers = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{self.name} has a(n) {animal}")
  
    def add_animals(self, animals):
        self.animals.extend(animals)
        print(f"{self.name} has many animals")
  
    def add_customer(self, name):
        self.customers.append(name)
        print(f"{name} has entered {self.name}")

    def remove_customer(self, name):
        self.customers.remove(name)
        print(f"{name} has left {self.name}")
    
    def visit_animals(self):
        for a in self.animals:
            print(f"visiting {a.get_name()}")
            a.make_noise()
            a.eat_food()

class Animal:
    def __init__(self,name):
        self.name = name
    def get_name(self):
        return self.name
    
    def make_noise(self):
        print("Every animal makes noise")
        
    def eat_food(self):
        print("All creatures need sustenance")

#     Now that your Customer class is complete, let's create some animal classes. 
# Each subclass should call the Animal constructor in its own constructor and should override the make_noise and eat_food methods to print appropriate messages.

# Make sure to create at least three different Animal subclasses. We suggest Fish, Bird, and Chimp.
class Fish(Animal):
    def __init__(self,name):
        super().__init__(name)
        
    def make_noise(self):
        print(f"{self.name} blows bubbles.")
        
    def eat_food(self):
        print(f"{self.name} eats food.")

class Bird(Animal):
    def __init__(self,name):
        super().__init__(name)
        
    def make_noise(self):
         print(f"{self.name} tweets loudly!")
         
    def eat_food(self):
        print(f"{self.name} eats nuts and berries!")

class Chimp(Animal):
    def __init__(self,name):
        super().__init__(name)
        
    def make_noise(self):
        print(f"{self.name} makes weird noises.")
        
    def eat_food(self):
        print(f"{self.name} eats leaves and fruit.")


nycZoo = Zoo("NYC Zoo")


salmon = Fish("salmon")
robin = Bird("robin")
bonobo = Chimp("bonobo")
nycZoo.add_animals([salmon, robin, bonobo])

# Now, let's create some customers and add them to the zoo.
alice = Customer("Alice",25)
bob = Customer("Bob",20)
charlie = Customer("Charlie",10)
dave = Customer("Dave",30)
for c in [alice, bob, charlie, dave]:
    c.buy_ticket()
    c.enter_zoo(nycZoo)
nycZoo.visit_animals()
for c in [alice, bob, charlie, dave]:
    c.exit_zoo(nycZoo)
# Watto needs a new system for organizing his inventory of podracers. 
# Help him do this by implementing an Object Oriented solution according to the following criteria.

# First, he'll need a general Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes. 
class Podracer:
  def __init__(self, max_speed, condition, price):
    self.max_speed = max_speed
    self.condition = condition
    self.price = price

  # Define a repair() method that will update the condition of the podracer to "repaired".
  def repair(self):
    self.condition = "repaired"
    
# Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2.
class AnakinsPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super().__init__(max_speed, condition, price)
  
  def boost(self):
    self.max_speed *= 2
    
# Define another class that inherits Podracer and call this one SebulbasPod. 
# This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".
class SebulbasPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super().__init__(max_speed, condition, price)
  
  def flame_jet(self,other):
    other.condition = "trashed"



Anakins_pod = AnakinsPod(300, "good", 5000)
print(f"Anakin's pod max speed: {Anakins_pod.max_speed}")
Anakins_pod.boost()
print(f"Anakin's pod max speed after boost: {Anakins_pod.max_speed}")
SebulbasPod = SebulbasPod(280, "excellent", 10000)
SebulbasPod.flame_jet(Anakins_pod)
print(f"Anakin's pod condition after flame jet: {Anakins_pod.condition}")

'''
Make sure to answer the following prompts about your coding experience:

How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)

Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?

How in particular did Object Oriented Programming assist in the solving of this problem?

'''
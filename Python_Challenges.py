# program to create all possible permutations from a given collection of distinct numbers.
# Source: https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-12.php
def permute(nums):
  empty_list = []
  result_perms = [empty_list]
  for n in nums:
    new_perms = []
    for perm in result_perms:
      for i in range(len(perm)+1):
        new_perms.append(perm[:i] + [n] + perm[i:])
        print(new_perms)
        result_perms = new_perms
        print(result_perms)
        print("")
  return result_perms

my_nums = [1,2,3]
print("Original Cofllection: ",my_nums)
print("Collection of distinct numbers:\n",permute(my_nums))

#Determine if a number is even or odd
#File name: even_or_odd.py

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
  print(f"\nThe number (number) is even.")
else:
  print(f"\nThe number {number} is odd.")

#While loop: letting the user choose when to quit 
# parrot.py
prompt = "\nTell me something, and I will repeat it back to you:"
 prompt += "\nEnter 'quit' to end the program."
message = ""
while message != 'quit':
  message = input(prompt)
  print(message)
  
  #Adding a FLAG to the program: - when many conditions are involved - having an active state of the system
  prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "n\Enter 'quit' to end the program. "
active = True
while active: 
    message = input(prompt)
    
    if message == 'quit':
        active = False
    else: 
        print(message)
      
      
#Using break to Exit a Loop
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "n\Enter 'quit' to end the program. "
while True: 
    city = input(prompt)
    
    if city == 'quit':
        break
    else: 
        print(f"I'd love to go to {city.title()}!")
#Using CONTINUE in the loop
current_number = 0
while current_number < 10: 
    current_number += 1
    if current_number % 2 == 0: 
        continue

    print(current_number)

#Transferring users from unconfirmed to confirmed pile
#confirmed_users.py from Python Crash Course book
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
#Verify each user until there are no more unconfirmed users
#Move each verified user into the list of confirmed users
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
    
    #Display all confirmed users
    print("\nThe following users have been confirmed:")
    for confirmed_user in confirmed_users: 
        print(confirmed_user.title())
#Removing All Instances of Specific Values from a List pets.py
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets: 
    pets.remove('cat')
print(pets)

#mountain_poll.py Filling a Dictionary with User Input
responses = {}
#Set up a flag to indicate that polling is active.
polling_active = True

while polling_active: 
    # Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    
    #Store the response in the dictionary
    responses[name] = response
    
    #Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/no)")
    
    if repeat == 'no':
        polling_active = False
    
    #Polling is complete. Show the resuls. 
    print("\n--- Poll Results ---")
    for name, response in responses.items():
        print(f"{name} would like to climb {response}.")

#Providing a default value for a parameter 
def describe_pet(pet_name, animal_type = 'dog'):
    """Display Information About a Pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(pet_name='willie')

#formatted_name.py
#Returning a simple value - take first and last name and return a formatted full name
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('jimi','hendrix')
print(musician)

#Make an argument optional - e.g. providing a middle name
def get_formatted_name(first_name, last_name, middle_name =''):
    """Return a full name, neatly formatted."""
    if middle_name: 
        full_name = f"{first_name} {middle_name} {last_name}"
    else: 
        full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

#Passing objects such as dictionaries to a list
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

#Modifying a list in a function
#print_models.py
#Start with some designs thaet need to be printed
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

#Similate printing each design, until none are left
#Move each design to completed_models after printing
while unprinted_designs: 
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

# Display all completed models 
print("\nThe following models have been printed:")
for completed_model in completed_models: 
    print(completed_model)

#Exporting Python classes as modules exercise
#car.py
"""A class that can be used to represent a car."""
class Car: 
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year): 
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.manufacturer} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage 
        else: 
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

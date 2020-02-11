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

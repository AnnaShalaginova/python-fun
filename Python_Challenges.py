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

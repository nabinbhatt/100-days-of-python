import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

# get the total number of items in list 
total = len(names)

random_number = random.randint(1, total - 1)
choice = names[random_number]
print(f"{choice} is going to buy the meal today!")
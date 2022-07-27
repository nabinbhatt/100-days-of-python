# Adding even numbers
#method 1
sum = 0
for number in range(2, 101, 2):
  sum += number
print(sum)

#method 2
total = 0
for number in range(1, 101):
  if number % 2 == 0:
    total += number
print(total)

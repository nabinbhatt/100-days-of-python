from math import ceil

def paint_calc(height, width, cover):
    area = (height * width)
    num_of_cans = ceil(area / cover)
    print(f"You'll need {num_of_cans} cans of paint.")

h = int(input("Height of wall: "))
w = int(input("Width of wall: "))
coverage = 5
print_calc(height=h, width=w, cover=coverage)

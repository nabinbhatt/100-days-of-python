age = input("What is your current age? ")

age = int(age)

years_remaining = 90 - age
days_remaining = 365 * years_remaining
weeks_remaining = 52 * years_remaining
months_remaining = 12 * years_remaining

print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")
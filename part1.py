
years = int(input("Enter the number of years:\n"))
inches = 0

for y in range(0,years):
    for m in range(0,12):
        inches += int(input(f"Enter the number of inches of rain in month {m} of year {y}:\n"))

print(f"In {12*years} months, there was {inches} inches of rainfall, averaging {inches/(12*years):.2f} inches per month")
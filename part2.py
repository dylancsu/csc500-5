books = int(input("Enter the number of books purchased this month:\n"))
if(books<2):
    print("You have earned 0 points")
elif(books<4):
    print("You have earned 5 points")
elif(books<6):
    print("You have earned 15 points")
elif(books<8):
    print("You have earned 30 points")
else:
    print("You have earned 60 points")
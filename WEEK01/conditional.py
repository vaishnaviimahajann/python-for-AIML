a = 18
if(a <= 18):
    print("You are eligible to vote")

b= int(input("Enter your age: "))    
if(b < 18 and b > 0):
    print("You are not eligible to vote")


color = input("Enter your favorite color: ")
if(color == "red"):
    print("Your favorite color is red")
elif(color == "blue"):
    print("Your favorite color is blue")
elif(color == "green"):
    print("Your favorite color is green")
else:
    print("Your favorite color is not red, blue or green")

    #to write default statement in nested we use _ before case statement
fruit = input("Enter your favorite fruit: ")
match fruit:
    case "apple":
        print("Your favorite fruit is apple")
    case "banana":
        print("Your favorite fruit is banana")
    case "mango":
        print("Your favorite fruit is mango")
    case _:
        print("Your favorite fruit is not apple, banana or mango")


number = 1
while(number <= 5):
    print(number)
    number += 1

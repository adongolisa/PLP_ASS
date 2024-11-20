"""Basic Calculator Program

Create a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).
Perform the operation based on the user's input and print the result.
Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15."""



def calculation(First_number,Second_number):

    sum= First_number + Second_number
    subtraction= First_number - Second_number
    multiplication= First_number * Second_number
    division= First_number / Second_number
    return sum,subtraction,multiplication,division

First_number= int(input("enter the first number "))
Second_number= int(input("enter the second number "))

results = calculation(First_number, Second_number)
    

print("Sum:", results[0]) 
print("Subtraction:", results[1]) 
print("Multiplication:", results[2]) 
print("Division:", results[3])
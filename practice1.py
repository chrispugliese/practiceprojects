# function to add numbers

import time

def addition(x, y):
     return x + y

#function to subtract numbers

def subtraction(x, y):
     return x - y

#function to multiply numbers

def multiplication(x, y):
     return x * y

#function to divide numbers

def division(x, y):
     return x / y


print("Select Operation")
print("1 for Addition")
print("2 for Subtraction")
print("3 for Multiplication")
print("4 for Division")


while True:


     choice = input("Enter (1, 2, 3, or 4): ")
    # exit = input("Exit?") #add y/n function


     if choice in ('1', '2', '3', '4'):


          num1 = float(input("Enter first number: "))
          num2 = float(input("Enter second number: "))

          if choice == 'y':
               break

          elif choice == 'n':
               continue

          elif choice == '1':
               print(num1, '+', num2, '=', addition(num1, num2))

          elif choice == '2':
               print(num1, '-', num2, '=', subtraction(num1, num2))

          elif choice == '3':
               print(num1, '*', num2, '=', multiplication(num1, num2))

          elif choice == '4':
               if num2 == 0:
                    print("Cannot divide by zero try again")
               else:
                    print(num1, '/', num2, '=',  division(num1, num2))

          continue_calculator = input("Do you want to continue? (y/n)")
          if continue_calculator.lower() != 'y':
               print('Exiting calculator...')
               time.sleep(2)
               break
     else:
          print("Invalid input")


          



          

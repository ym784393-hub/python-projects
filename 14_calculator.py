def calculator():
  choice = "yes"
  while choice == "yes":
    num1 = int(input("Enter first number: "))
    operation = input("Enter operation: ")
    num2 = int(input("Enter second number: "))
    if operation == "+":
      print(num1 + num2)
    elif operation =="-":
      print(num1 - num2)
    elif operation == "*":
      print(num1 * num2)
    elif operation == "/":
      print(num1 / num2)
    choice = input("Do you want to continue? ")
  if choice!= "yes":
    print("you exit")


calculator()

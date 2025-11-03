def add(x, y):
  """Adds two numbers"""
  return x + y

def subtract(x, y):
  """Subtracts two numbers"""
  return x - y

def multiply(x, y):
  """Multiplies two numbers"""
  return x * y

def divide(x, y):
  """Divides two numbers, handling division by zero"""
  if y == 0:
    return "Error: Cannot divide by zero"
  return x / y

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
  # Get user input
  choice = input("Enter choice (1/2/3/4) or 'q' to quit: ")

  # Check if user wants to quit
  if choice.lower() == 'q':
    break

  # Check if the choice is valid
  if choice in ('1', '2', '3', '4'):
    try:
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))
    except ValueError:
      print("Invalid input. Please enter numbers.")
      continue

    # Perform the calculation based on user's choice
    if choice == '1':
      print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
      print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
      print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
      print(f"{num1} / {num2} = {divide(num1, num2)}")
  else:
    print("Invalid Input. Please select 1, 2, 3, 4, or q.")
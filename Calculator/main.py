#calculator in python using functions

def add():
  num1 = float(input("Enter a 1st value:"))
  num2 = float(input("Enter a 2st value:"))
  return num1 + num2

def sub():
  num1 = float(input("Enter a 1st value:"))
  num2 = float(input("Enter a 2st value:"))
  return num1 - num2

def mult():
  num1 = float(input("Enter a 1st value:"))
  num2 = float(input("Enter a 2st value:"))
  return num1 * num2

def div():
  num1 = float(input("Enter a 1st value:"))
  num2 = float(input("Enter a 2st value:"))
  return num1 / num2

if __name__ == "__main__":
  while True:
    select = int(input("Choose the number: 1.Addition 2.Subtraction 3.Multiplication 4.Division 5.Quit\n"))
    if select == 1:
      print("Addition of two numbers is:",add())
    elif select == 2:
      print("Subtraction of two numbers is:",sub())
    elif select == 3:
      print("Multiplication of two numbers is:",mult())
    elif select == 4:
      print("Division of two numbers is:",div())
    elif select == 5:
      print("Exited!!")
      break
    else:
      print("Incorrect Selection ! TRY AGAIN")
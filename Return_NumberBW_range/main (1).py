#Write a program which will find all such numbers which are #divisible by 7 but are not a multiple of 5, between 2000 and #3200 (both included).

#1 Define Range of Numbers
#2 select proper Loop
#3 Use Selection statement

num1 = 2000
num2 = 3200

def test(a,b):
  lst = []
  for i in range(a,b):
    if(i%7==0 and i%5!=0):
      lst.append(str(i))
  return ",".join(lst)

if __name__ == "__main__":
  print(test(num1,num2))

if(2737 % 5!=0):
  print("True")







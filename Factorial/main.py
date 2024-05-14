#Write a Program which can compute the factorial of a given number.

#1 For Loop
#2 Recursion Function

num = 5               #5 * 4 * 3 * 2 * 1 = 120
fact = 1
while num >= 1:
  fact = fact * num   # 1 * % = 5
  num = num - 1       # 5 - 1 = 4 / 4 - 1 = 3 / 3 - 1 = 2 / 2 - 1 = 1

print(fact)


# Recursion Function

def fact(num):
  if num == 0:
    return 1
  else:
    return num * fact(num - 1) # 5 * (5 - 1) = 4 * (4 - 1) = 3 * (3 - 1) = 2 * (2-1)

a = 5
print(fact(a))
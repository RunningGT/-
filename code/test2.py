a = 200
b = 66
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

c = 300
d = 100
print("A") if a > b else print("B")

# 循环

i = 1
while i < 7:
  print(i)
  if i == 3:
    break
  i += 1

i = 0
while i < 7:
  i += 1
  if i == 3:
    continue
  print(i)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
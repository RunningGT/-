thislist1 = ["apple", "banana", "cherry"]
print(thislist1[-1])

thislist2 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist2[2:5])

thislist3 = ["apple", "banana", "cherry"]
for x in thislist3:
  print(x)

thistuple1 = ("apple", "banana", "cherry")
print(thistuple1)

thistuple2 = ("apple", "banana", "cherry")
print(thistuple2[-1])

# 把元组转换为列表
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

thisdict =	{
  "brand": "Porsche",
  "model": "911",
  "year": 1963
}
print(thisdict)
x = thisdict["model"]
print(x)


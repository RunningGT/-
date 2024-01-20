# 面向对象
# 类/对象
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("ikun", 18)

print(p1.name)
print(p1.age)

class Person:
  def __init__(man, name, age):
    man.name = name
    man.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name
          + " and my age is" + str(abc.age))

p1 = Person("kunkun", 20)
p1.myfunc()

# del p1.age
# p1.myfunc()
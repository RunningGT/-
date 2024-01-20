# 面向对象
# 类/对象
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"姓名: {self.name}, 年龄: {self.age}")

    def set_age(self, new_age):
        self.age = new_age

    def get_age(self):
        return self.age

    def _private_method(self):
        print("这是一个私有方法。")

    @classmethod
    def class_method_example(cls):
        print(f"这是一个类方法。类名: {cls.__name__}")

    @staticmethod
    def static_method_example():
        print("这是一个静态方法。")

# 继承
class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def display_info(self):
        print(f"姓名: {self.name}, 年龄: {self.age}, ID: {self.employee_id}")

# 实例化
employee = Employee("IKUN", 25, "E12345")

# 调用 display_info （覆盖父类）
employee.display_info()

# 多态
def show_info(entity):
    entity.display_info()

show_info(employee)  # 传递 Employee 实例

# 封装
class EncapsulationExample:
    def __init__(self):
        self._protected_variable = "I am protected"
        self.__private_variable = "I am private"

    def get_private_variable(self):
        """
        获取私有变量的值。
        """
        return self.__private_variable

    def set_private_variable(self, new_value):
        """
        设置私有变量的值。
        """
        self.__private_variable = new_value

# 实例化 EncapsulationExample 类
encapsulation_obj = EncapsulationExample()

# 获取并打印受保护的变量
print(encapsulation_obj._protected_variable)

# 打印私有变量
print(encapsulation_obj.get_private_variable())

# 设置新的私有变量值
encapsulation_obj.set_private_variable("New private value")
print(encapsulation_obj.get_private_variable())

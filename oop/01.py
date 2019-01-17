'''
定义一个学生类,用来形容学生
'''
# 定义一个空的类
class Student():
    pass # 一个空类,pass表示直接跳过

# 定义一个对象
shi = Student()

# 定义一个类,用来描述听Python的学生
class PythonStudent():
    # 用None给不确定的值赋值
    name = None
    age = 21
    course = "Python"

    def doHomework(self):
        print("DO homework")
        return None

# 示例化一个学生,是一个具体的人
lin = PythonStudent()
print(lin.name)
print(lin.age)
lin.doHomework()
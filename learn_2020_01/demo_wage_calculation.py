"""
    工资结算系统
    展示Python面向对象的三大支柱
    封装、继承、多态
"""
"""
月薪结算系统 - 部门经理每月15000 程序员每小时200 销售员1800底薪加销售额5%提成
"""
from abc import ABCMeta, abstractmethod

class Employee(metaclass=ABCMeta):
    '''员工（抽象类）'''

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_salary(self):
        '''结算月薪'''
        pass

class Manager(Employee):
    '''部门经理'''

    def get_salary(self):
        return 15000.0

class Programmer(Employee):

    def __init__(self, name, working_hour=0):
        self.working_hour = working_hour
        super().__init__(name)

    def get_salary(self):
        return 200.0 * self.working_hour

class Salesman(Employee):
    '''销售员'''
    def __init__(self, name, sales=0.0):
        self.sales = sales
        super().__init__(name)

    def get_salary(self):
        return 1000.0 + self.sales * 0.05

class EmployeeFactory():

    @staticmethod
    def create(emp_type, *args, **kwargs):
        '''创建员工'''
        emp_type = emp_type.upper()
        emp = None
        if emp_type == 'M':
            emp = Manager(*args, **kwargs)
        elif emp_type == 'P':
            emp = Programmer(*args, **kwargs)
        elif emp_type == 'S':
            emp = Salesman(*args, **kwargs)
        return emp

if __name__ == '__main__':
    emps = [
        EmployeeFactory.create('M', '曹操'),
        EmployeeFactory.create('P', '荀彧', 120),
        EmployeeFactory.create('P', '郭嘉', 85),
        EmployeeFactory.create('S', '典韦', 123000),
    ]
    for emp in emps:
        print('{}的工资：{}元'.format(emp.name, emp.get_salary()))
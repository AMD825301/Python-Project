class Employee:

    def __init__(self, e_name):
        self.e_name = e_name

    def getName(self):
        print(self.e_name)

    def isEmployee(self):
        return False


class SalaryEmployee(Employee):

    def __init__(self, name):
        super().__init__(name)
        print("{} is a Salary Employee.".format(name))

    def isEmployee(self):
        return True


class DailyWageEmployee(Employee):
    def __init__(self, name):
        super().__init__(name)
        print("{} is a Daily Waged Employee.".format(name))

    def isEmployee(self):
        return False


class CommissionEmployee(Employee):
    def __init__(self, name):
        super().__init__(name)
        print("{} is a Commission Employee.".format(name))

    def isEmployee(self):
        return True


s = SalaryEmployee("Rakesh")
d = DailyWageEmployee("Manoj")
c = CommissionEmployee("Ravi")

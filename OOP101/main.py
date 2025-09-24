class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = []

    def update_tricks(self, trick):
        self.tricks.append(trick)

    def show(self):
        return f"The new dog is named {self.name} and his tricks are {str(self.tricks)}"


dog = Dog('Toby')
dog.update_tricks('catch')
dog.update_tricks('spin')


class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []

    def update_tricks(self, trick):
        self.tricks.append(trick)

    def get_name(self):
        return self.name

    def get_tricks(self):
        return self.tricks

dog = Dog('Frito')
dog.update_tricks('spin')
dog.update_tricks('sit')
print(dog.get_name())
print(dog.get_tricks())



class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

new_emp = Employee("Aharon", 60000)


class Employee:

    def __init__(self, name):
        self.name = name
        self.salary = 0

    def show(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

new_emp = Employee("Aharon")
new_emp.show()


class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print("Name: ", self.name, ", Salary: ", self.salary)

new_emp = Employee("Aharon", 2000)
new_emp.show()

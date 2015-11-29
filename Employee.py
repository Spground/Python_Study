class Employee:
        empCount = 0;

        def __init__(self, name, salary):
                self.name = name;
                self.salary = salary;
                Employee.empCount += 1;

        def displayCount(self):
                print("total empCount %d" % Employee.empCount);
                
        def displayEmployee(self):
                print("Tha name of Emloyee is" + self.name);
                
emp1 = Employee("Zara", 2000);
emp2 = Employee("Zara", 2000);
emp3 = Employee("Zara", 2000);
emp4 = Employee("Zara", 2000);

emp1.displayCount();
emp1.displayEmployee();

i = 4;
while i < 16:
        i = i + 1;
        print(i);

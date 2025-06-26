class Employee:
    def __init__(self, name, position, attendance=0):
        self.name = name
        self.position = position
        self.attendance = attendance

    def mark_attendance(self):
        self.attendance += 1
        print(f"{self.name}'s attendance marked. Total days present: {self.attendance}")

    def get_details(self):
        print(f"Name     : {self.name}")
        print(f"Position : {self.position}")
        print(f"Attendance: {self.attendance} days\n")


# Creating employee objects
emp1 = Employee("Alice", "Software Engineer")
emp2 = Employee("Bob", "Project Manager")
emp3 = Employee("Charlie", "HR Executive", attendance=5)

# Marking attendance
emp1.mark_attendance()
emp2.mark_attendance()
emp2.mark_attendance()

# Showing employee details
print("\nEmployee Details:")
emp1.get_details()
emp2.get_details()
emp3.get_details()

class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def role(self):
        print(f"{self.name} is an employee")

class Project:
    def __init__(self, project_name):
        self.project_name = project_name

class TeamLead(Employee, Project):
    def __init__(self, name, project_name):
        Employee.__init__(self, name)
        Project.__init__(self, project_name)

    def details(self):
        print(f"{self.name} leads the project {self.project_name}")


if __name__ == "__main__":
    lead = TeamLead("Sophia", "AI Development")
    lead.role()
    lead.details()
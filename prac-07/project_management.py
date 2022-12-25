import datetime


class Project:
    """Class to represent a project with name, start date, priority, estimate, and completion %."""

    def __init__(self, name, start_date, priority, estimate, completion=0):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.estimate = estimate
        self.completion = completion

    def __lt__(self, other):
        """Method to compare two projects based on priority order."""
        return self.priority < other.priority

    def update_completion(self, completion):
        """Method to update the completion % of a project."""
        self.completion = completion

    def update_priority(self, priority):
        """Method to update the priority of a project."""
        self.priority = priority

    def __str__(self):
        """Method to return a string representation of a project."""
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, estimate: ${self.estimate:.2f}, completion: {self.completion}%"


def load_projects(filename):
    """Function to load a list of projects from a data file."""
    projects = []
    with open(filename, "r") as f:
        for line in f:
            name, start_date_str, priority_str, estimate_str, completion_str = line.strip().split("\t")
            start_date = datetime.datetime.strptime(start_date_str, "%d/%m/%Y").date()
            priority = int(priority_str)
            estimate = float(estimate_str)
            completion = int(completion_str)
            project = Project(name, start_date, priority, estimate, completion)
            projects.append(project)
    return projects


def save_projects(filename, projects):
    """Function to save a list of projects to a data file."""
    with open(filename, "w") as f:
        f.write("name\tstart date\tpriority\testimate\tcompletion\n")
        for project in projects:
            f.write(
                f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.estimate:.2f}\t{project.completion}\n")


def display_projects(projects):
    """Function to display a list of projects in two groups: incomplete and completed, both sorted by priority."""
    incomplete_projects = [project for project in projects if project.completion < 100]
    completed_projects = [project for project in projects if project.completion == 100]
    print("Incomplete projects: ")
    for project in sorted(incomplete_projects):
        print(f"  {project}")
    print("Completed projects: ")
    for project in sorted(completed_projects):
        print(f"  {project}")


def filter_projects_by_date(projects, date):
    """Function to filter a list of projects by"""


# Load the projects from the data file
projects = load_projects("projects.txt")

# Display the menu and handle user input
while True:
    print("""
(L)oad projects
(S)ave projects
(D)isplay projects
(F)ilter projects by date
(A)dd new project
(U)pdate project
(Q)uit
""")
    choice = input(">>> ").upper()
    if choice == "L":
        filename = input("Enter the filename to load projects from: ")
        projects = load_projects(filename)
    elif choice == "S":
        filename = input("Enter the filename to save projects to: ")
        save_projects(filename, projects)
    elif choice == "D":
        display_projects(projects)
    elif choice == "F":
        date_string = input("Enter the date (dd/mm/yyyy): ")
        date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
        filtered_projects = [project for project in projects if project.start_date >= date]
        for project in sorted(filtered_projects, key=lambda x: x.start_date):
            print(project)
    elif choice == "A":
        name = input("Enter the name of the project: ")
        start_date_string = input("Enter the start date (dd/mm/yyyy): ")
        start_date = datetime.datetime.strptime(start_date_string, "%d/%m/%Y").date()
        priority = int(input("Enter the priority (1-10): "))
        estimate = float(input("Enter the estimate ($): "))
        project = Project(name, start_date, priority, estimate)
        projects.append(project)
    elif choice == "U":
        name = input("Enter the name of the project to update: ")
        project = next((p for p in projects if p.name == name), None)
        if project:
            completion = input("Enter the new completion % (leave blank to retain current value): ")
            if completion:
                project.update_completion(int(completion))
            priority = input("Enter the new priority (leave blank to retain current value): ")
            if priority:
                project.update_priority(int(priority))
        else:
            print("Project not found.")
    elif choice == "Q":
        break

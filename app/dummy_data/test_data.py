import json
from pathlib import Path


path = Path(__file__).parent


with open(path/"employees.json") as file:

    employees=json.load(file)


print(
    "Employees:",
    len(employees)
)


print(
    employees[0]
)

employees = {
    101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000},
    102: {'name': 'Amit', 'age': 30, 'department': 'Finance', 'salary': 60000},
    103: {'name': 'Priya', 'age': 25, 'department': 'IT', 'salary': 55000}
}

def add_employee():
    try:
        emp_id = int(input("Enter Employee ID: "))
        if emp_id in employees:
            print("❌ Employee ID already exists. Try a different ID.")
            return
        name = input("Enter Employee Name: ")
        age = int(input("Enter Employee Age: "))
        department = input("Enter Employee Department: ")
        salary = float(input("Enter Employee Salary: "))

        employees[emp_id] = {
            'name': name,
            'age': age,
            'department': department,
            'salary': salary
        }
        print("✅ Employee added successfully.\n")
    except ValueError:
        print("❌ Invalid input. Please enter correct data types.\n")

def view_employees():
    if not employees:
        print("⚠️ No employees available.\n")
        return
    print("\nID\tName\tAge\tDepartment\tSalary")
    print("-" * 50)
    for emp_id, info in employees.items():
        print(f"{emp_id}\t{info['name']}\t{info['age']}\t{info['department']}\t\t{info['salary']}")
    print()

def search_employee():
    try:
        emp_id = int(input("Enter Employee ID to search: "))
        if emp_id in employees:
            emp = employees[emp_id]
            print("\n✅ Employee Found:")
            print(f"ID: {emp_id}")
            print(f"Name: {emp['name']}")
            print(f"Age: {emp['age']}")
            print(f"Department: {emp['department']}")
            print(f"Salary: {emp['salary']}\n")
        else:
            print("❌ Employee not found.\n")
    except ValueError:
        print("❌ Invalid ID. Please enter a number.\n")

def main_menu():
    while True:
        print("====== Employee Management System ======")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search for Employee")
        print("4. Exit")
        try:
            choice = int(input("Enter your choice (1-4): "))
            print()
            if choice == 1:
                add_employee()
            elif choice == 2:
                view_employees()
            elif choice == 3:
                search_employee()
            elif choice == 4:
                print("🙏 Thank you for using the Employee Management System. Goodbye!")
                break
            else:
                print("❌ Invalid choice. Please enter a number between 1 and 4.\n")
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.\n")

# Run the EMS
if __name__ == "__main__":
    main_menu()

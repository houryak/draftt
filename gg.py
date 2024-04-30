'''
The Employee class defines attributes related to an employee such as
name, employee ID, department, job title, basic salary, age, date of birth, and passport details.
'''
class Employee:
    def __init__(self, name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details):
        self.name = name
        self.employee_id = employee_id
        self.department = department
        self.job_title = job_title
        self.basic_salary = basic_salary
        self.age = age
        self.date_of_birth = date_of_birth
        self.passport_details = passport_details

#The get_details method returns a dictionary containing the details of an employee.
    def get_details(self):
        return {
            'Name': self.name,
            'Employee ID': self.employee_id,
            'Department': self.department,
            'Job Title': self.job_title,
            'Basic Salary': self.basic_salary,
            'Age': self.age,
            'Date of Birth': self.date_of_birth,
            'Passport Details': self.passport_details
        }


'''
The Event class represents an event with attributes like event ID, type, theme, date, time, duration, venue address, client ID, guest list, and invoice.
'''
class Event:
    def __init__(self, event_id, type, theme, date, time, duration, venue_address, client_id, guest_list, invoice):
        self.event_id = event_id
        self.type = type
        self.theme = theme
        self.date = date
        self.time = time
        self.duration = duration
        self.venue_address = venue_address
        self.client_id = client_id
        self.guest_list = guest_list
        self.invoice = invoice

#The get_details method returns a dictionary with the details of an event.
    def get_details(self):
        return {
            'Event ID': self.event_id,
            'Type': self.type,
            'Theme': self.theme,
            'Date': self.date,
            'Time': self.time,
            'Duration': self.duration,
            'Venue Address': self.venue_address,
            'Client ID': self.client_id,
            'Guest List': self.guest_list,
            'Invoice': self.invoice
        }

'''
The Client class defines attributes for a client including client ID, name, address, contact details, and budget.
'''
class Client:
    def __init__(self, client_id, name, address, contact_details, budget):
        self.client_id = client_id
        self.name = name
        self.address = address
        self.contact_details = contact_details
        self.budget = budget

#The get_details method returns a dictionary containing the client's details.
    def get_details(self):
        return {
            'Client ID': self.client_id,
            'Name': self.name,
            'Address': self.address,
            'Contact Details': self.contact_details,
            'Budget': self.budget
        }

'''
The Guest class represents a guest with attributes like guest ID, name, address, and contact details.
'''
class Guest:
    def __init__(self, guest_id, name, address, contact_details):
        self.guest_id = guest_id
        self.name = name
        self.address = address
        self.contact_details = contact_details

#The get_details method returns a dictionary with the guest's details.
    def get_details(self):
        return {
            'Guest ID': self.guest_id,
            'Name': self.name,
            'Address': self.address,
            'Contact Details': self.contact_details
        }

'''
The Venue class defines attributes for a venue such as venue ID, name, address, contact, minimum guests, and maximum guests.
'''
class Venue:
    def __init__(self, venue_id, name, address, contact, min_guests, max_guests):
        self.venue_id = venue_id
        self.name = name
        self.address = address
        self.contact = contact
        self.min_guests = min_guests
        self.max_guests = max_guests

#The get_details method returns a dictionary containing the venue's details.
    def get_details(self):
        return {
            'Venue ID': self.venue_id,
            'Name': self.name,
            'Address': self.address,
            'Contact': self.contact,
            'Min Guests': self.min_guests,
            'Max Guests': self.max_guests
        }

'''
The Supplier class represents a supplier with attributes like supplier ID, name, address, contact details, menu, minimum guests, and maximum guests.
'''
class Supplier:
    def __init__(self, supplier_id, name, address, contact_details, menu, min_guests, max_guests):
        self.supplier_id = supplier_id
        self.name = name
        self.address = address
        self.contact_details = contact_details
        self.menu = menu
        self.min_guests = min_guests
        self.max_guests = max_guests

#The get_details method returns a dictionary with the supplier's details.
    def get_details(self):
        return {
            'Supplier ID': self.supplier_id,
            'Name': self.name,
            'Address': self.address,
            'Contact Details': self.contact_details,
            'Menu': self.menu,
            'Min Guests': self.min_guests,
            'Max Guests': self.max_guests
        }


'''
In the test cases section, instances of the classes are created with sample data to demonstrate how the classes can be used.
Employees, events, clients, guests, venues, and suppliers are created with specific details.
Finally, the details of each instance are printed to showcase the information stored in each object.
'''

# Test cases
if __name__ == "__main__":
    # Create employees
    susan = Employee("Susan Meyers", "47899", "Sales", "Sales Manager", 37500, 35, "01-01-1989", "XX1234567")
    shyam = Employee("Shyam Sundar", "11234", "Sales", "Salesperson", 20000, 28, "15-05-1996", "YY2345678")
    salma = Employee("Salma J Sam", "98637", "Sales", "Salesperson", 20000, 30, "20-07-1994", "ZZ3456789")
    joy = Employee("Joy Rogers", "81774", "Sales", "Sales Manager", 24000, 40, "10-10-1984", "AA4567890")
    mariam = Employee("Mariam Khalid", "98394", "Sales", "Salesperson", 20000, 27, "25-12-1997", "BB5678901")

    # Create events
    wedding = Event("EV001", "Wedding", "Traditional", "2024-06-15", "18:00", "5 hours", "123 Main St", "C001",
                    ["G001", "G002"], "INV001")

    # Create clients
    client1 = Client("C001", "Dana Ali", "456 Elm St", "050-456-7890", 20000)

    # Create guests
    guest1 = Guest("G001", "Alia", "457 Elm St", "052-222-3333")
    guest2 = Guest("G002", "Khalid", "458 Elm St", "055-555-6666")

    # Create venues
    venue1 = Venue("V001", "Grand Hall", "789 Maple St", "056-012-3456", 50, 200)

    # Create suppliers
    supplier1 = Supplier("S001", "ABC Catering", "101 Oak St", "050-234-5678", "Buffet", 50, 200)

    # Display details
    print(susan.get_details())
    print(wedding.get_details())
    print(client1.get_details())
    print(guest1.get_details())
    print(venue1.get_details())
    print(supplier1.get_details())

import tkinter as tk
from tkinter import ttk

class EventManagementSystem(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Event Management System")

        # Create notebook
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(pady=10, expand=True, fill="both")

        # Employee tab
        self.employee_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.employee_frame, text="Employees")
        self.create_employee_widgets()

        # Initialize employee database (list of dictionaries)
        self.employee_database = []

    # Employee methods
    def create_employee_widgets(self):
        self.employee_label = ttk.Label(self.employee_frame, text="Employee ID:")
        self.employee_label.grid(row=0, column=0, padx=10, pady=5)

        self.employee_id_entry = ttk.Entry(self.employee_frame)
        self.employee_id_entry.grid(row=0, column=1, padx=10, pady=5)

        self.employee_button = ttk.Button(self.employee_frame, text="Display Details", command=self.display_employee_details)
        self.employee_button.grid(row=0, column=2, padx=10, pady=5)

        # Add/Delete/Modify buttons
        self.add_employee_button = ttk.Button(self.employee_frame, text="Add", command=self.add_employee)
        self.add_employee_button.grid(row=2, column=0, padx=10, pady=5)

        self.delete_employee_button = ttk.Button(self.employee_frame, text="Delete", command=self.delete_employee)
        self.delete_employee_button.grid(row=2, column=1, padx=10, pady=5)

        self.modify_employee_button = ttk.Button(self.employee_frame, text="Modify", command=self.modify_employee)
        self.modify_employee_button.grid(row=2, column=2, padx=10, pady=5)

        self.employee_details_text = tk.Text(self.employee_frame, width=50, height=10)
        self.employee_details_text.grid(row=1, columnspan=3, padx=10, pady=5)

    def display_employee_details(self):
        employee_id = self.employee_id_entry.get()
        # Fetch details from database or the created objects
        employee_details = {"Name": "Susan Meyers", "Employee ID": "E001", "Department": "Sales", "Job Title": "Sales Manager", "Basic Salary": 50000, "Age": 35, "Date of Birth": "01-01-1989", "Passport Details": "XX1234567",}
        self.display_details(employee_details, self.employee_details_text)

    def add_employee(self):
        # Get the input values from entry fields
        name = self.employee_name_entry.get()
        employee_id = self.employee_id_entry.get()
        department = self.employee_department_entry.get()
        job_title = self.employee_job_title_entry.get()
        basic_salary = self.employee_basic_salary_entry.get()
        age = self.employee_age_entry.get()
        date_of_birth = self.employee_date_of_birth_entry.get()
        passport_details = self.employee_passport_details_entry.get()

        # Create a dictionary to represent the new employee
        new_employee = {
            "Name": name,
            "Employee ID": employee_id,
            "Department": department,
            "Job Title": job_title,
            "Basic Salary": basic_salary,
            "Age": age,
            "Date of Birth": date_of_birth,
            "Passport Details": passport_details
        }

        # Add the new employee to the database
        self.employee_database.append(new_employee)

        # Display the details of the new employee
        self.display_details(new_employee, self.employee_details_text)

    def delete_employee(self):
        # Get the employee ID to be deleted
        employee_id = self.employee_id_entry.get()

        # Find and remove the employee from the database
        for employee in self.employee_database:
            if employee["Employee ID"] == employee_id:
                self.employee_database.remove(employee)
                break

        # Clear the display
        self.employee_details_text.delete(1.0, tk.END)

    def modify_employee(self):
        # Get the employee ID
        employee_id = self.employee_id_entry.get()

        # Fetch the employee details from the database based on the employee ID
        for employee in self.employee_database:
            if employee["Employee ID"] == employee_id:
                # Update the employee details based on the input values
                employee["Name"] = self.employee_name_entry.get()
                employee["Department"] = self.employee_department_entry.get()
                employee["Job Title"] = self.employee_job_title_entry.get()
                employee["Basic Salary"] = self.employee_basic_salary_entry.get()
                employee["Age"] = self.employee_age_entry.get()
                employee["Date of Birth"] = self.employee_date_of_birth_entry.get()
                employee["Passport Details"] = self.employee_passport_details_entry.get()

                # Display the modified employee details
                self.display_details(employee, self.employee_details_text)
                break

    def display_details(self, details, text_widget):
        text_widget.delete(1.0, tk.END)
        for key, value in details.items():
            text_widget.insert(tk.END, f"{key}: {value}\n")

if __name__ == "__main__":
    app = EventManagementSystem()
    app.mainloop()

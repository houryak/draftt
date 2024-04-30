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

        # Event tab
        self.event_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.event_frame, text="Events")
        self.create_event_widgets()

        # Client tab
        self.client_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.client_frame, text="Clients")
        self.create_client_widgets()

        # Guest tab
        self.guest_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.guest_frame, text="Guests")
        self.create_guest_widgets()

        # Venue tab
        self.venue_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.venue_frame, text="Venues")
        self.create_venue_widgets()

        # Supplier tab
        self.supplier_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.supplier_frame, text="Suppliers")
        self.create_supplier_widgets()

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
        employee_details = {
            "Name": "Susan Meyers", "Employee ID": "47899", "Department": "Sales Manager", "Job Title": "Sales Manager", "Basic Salary": 37500, "Age": 35, "Date of Birth": "01-01-1989", "Passport Details": "XX1234567"        }
        self.display_details(employee_details, self.employee_details_text)

    def add_employee(self):
        # Implement add employee functionality
        # Here you can add code to create a new employee and save it
        pass

    def delete_employee(self):
        # Implement delete employee functionality
        # Here you can add code to delete an existing employee
        pass

    def modify_employee(self):
        # Implement modify employee functionality
        # Here you can add code to modify an existing employee's details
        pass

    # Event methods
    def create_event_widgets(self):
        # Similar to create_employee_widgets, you can add widgets for events here
        pass

    # Client methods
    def create_client_widgets(self):
        # Similar to create_employee_widgets, you can add widgets for clients here
        pass

    # Guest methods
    def create_guest_widgets(self):
        # Similar to create_employee_widgets, you can add widgets for guests here
        pass

    # Venue methods
    def create_venue_widgets(self):
        # Similar to create_employee_widgets, you can add widgets for venues here
        pass

    # Supplier methods
    def create_supplier_widgets(self):
        # Similar to create_employee_widgets, you can add widgets for suppliers here
        pass

    def display_details(self, details, text_widget):
        text_widget.delete(1.0, tk.END)
        for key, value in details.items():
            text_widget.insert(tk.END, f"{key}: {value}\n")

if __name__ == "__main__":
    app = EventManagementSystem()
    app.mainloop()

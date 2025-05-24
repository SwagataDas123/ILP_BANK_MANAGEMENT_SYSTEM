import random
from datetime import datetime
import re


# main_recent_new.Employee
# admin/employees does  have permission to deposit,withdraw or check balance
# Class for Employee
class Employee:
    def __init__(self, name, email, password, address, contact_number):
        self.employee_id = self._generate_emp_id()
        self.name = self.valid_name(name)
        self.email = self.valid_email(email)
        self.password = password[:30]
        self.address = address[:100]
        self.contact_number = self.valid_contact(contact_number)

    def _generate_emp_id(self):
        """Generate a random 7-digit employee ID that doesn't exist in the system"""
        existing_ids = {emp.employee_id for emp in employees.values()}
        while True:
            emp = random.randint(1000000, 9999999)
            if emp not in existing_ids:  # Check if this employee id is already used
                return emp

    def valid_email(self, email):
        while (True):
            email = email.strip().lower()
            # Validate format
            if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
                email = input("Invalid email format. Enter a valid email: ")
                continue
            # Check uniqueness
            if email in employees:
                email = input("Email already exists. Enter a different email: ")
                continue
            return email

    def valid_contact(self, contact_number):
        con = len(str(contact_number))
        if (con != 10):
            print("Contact number must be exactly 10 digits.")
            contact_number = int(input("enter contact no of 10 digits"))
            return contact_number
        else:
            return contact_number

    def valid_name(self, name):
        con = len(name)
        if (con > 50 or len(name.strip().split()) == 1):
            if (re.match(r"^[A-Za-z]+ [A-Za-z]+$", name.strip()) == None):
                name = input(
                    "Name cannot have more than 50 characters also it has to have both first name and last name"
                    " and doesnt match criteria so enter a matching criteria name "
                    "of less or equal to 50 characters")
                return name

            else:
                name = input(
                    "Name cannot have more than 50 characters so enter a name of less or equal to 50 characters")
                return name
        else:
            if (re.match(r"^[A-Za-z]+ [A-Za-z]+$", name.strip()) == None):
                name = input(
                    "Name doesnt match criteria so enter a matching criteria name of less or equal to 50 characters")
                return name
            else:
                return name


# Class for Customer
class Customer:
    def __init__(self, name, email, address, contact_number, aadhar_number, pan_number,
                 password):
        self.ssn_no = self._generate_ssn_id()
        self.name = self.valid_name(name)
        self.email = self.valid_email(email)
        self.address = address[:100]
        self.contact_number = self.valid_contact(contact_number)
        self.aadhar_number = self.valid_aadhar(aadhar_number)
        self.pan_number = self.valid_pan(pan_number)
        self.password = password[:30]  # Added password field for login

    def _generate_ssn_id(self):
        """Generate a random 7-digit SSN ID that doesn't exist in the system"""
        while True:
            ssn = random.randint(1000000, 9999999)
            if ssn not in customers:
                # Check if this SSN is already used
                return ssn

    def valid_pan(self, pan_number):
        con = len(pan_number)
        if (con != 10):
            if (re.fullmatch(r"[A-Z]{5}\d{4}[A-Z]", pan_number.strip().upper()) == None):
                pan_number = input("enter valid pan number of 10 digits")
                return pan_number
            else:
                pan_number = input("enter valid pan number of 10 digits ")
                return pan_number
        else:
            if (re.fullmatch(r"[A-Z]{5}\d{4}[A-Z]", pan_number.strip().upper()) == None):
                pan_number = input("enter valid pan number of 10 digits")
                return pan_number
            else:
                return pan_number

    def valid_email(self, email):
        while (True):
            email = email.strip().lower()
            # Validate format
            if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
                email = input("Invalid email format. Enter a valid email: ")
                continue
            # Check uniqueness
            if any(cust.email == email for cust in customers.values()):
                email = input("Email already exists. Enter a different email: ")
                continue
            return email

    def valid_name(self, name):
        con = len(name)
        if (con > 50 or len(name.strip().split()) == 1):
            if (re.match(r"^[A-Za-z]+ [A-Za-z]+$", name.strip()) == None):
                name = input(
                    "Name cannot have more than 50 characters also it has to have both first name and last name"
                    " and doesnt match criteria so enter a matching criteria name "
                    "of less or equal to 50 characters")
                return name

            else:
                name = input(
                    "Name cannot have more than 50 characters so enter a name of less or equal to 50 characters")
                return name
        else:
            if (re.match(r"^[A-Za-z]+ [A-Za-z]+$", name.strip()) == None):
                name = input(
                    "Name doesnt match criteria so enter a matching criteria name of less or equal to 50 characters")
                return name
            else:
                return name

    def valid_contact(self, contact_number):
        con = len(str(contact_number))
        if (con != 10):
            print("Contact number must be exactly 10 digits.")
            contact_number = int(input("enter contact no of 10 digits"))
            return contact_number
        else:
            return contact_number

    def valid_aadhar(self, aadhar_number):
        con = len(str(aadhar_number))
        if (con != 12):
            print("Aadhar number must be exactly 12 digits.")
            aadhar_number = int(input("enter aadhar no of 12 digits"))
            return aadhar_number
        else:
            return aadhar_number


class Account:
    def __init__(self, customer_ssn_no, account_type, initial_deposit):
        self.account_number = self._generate_account_number()
        self.account_type = account_type
        self.balance = initial_deposit
        self.customer_ssn_no = customer_ssn_no
        self.date_of_creation = datetime.now().strftime("%Y-%m-%d")

    def _generate_account_number(self):
        """Generate a random 12-digit account number that doesn't exist in the system"""
        while True:
            acc_num = str(random.randint(100000000000, 999999999999))
            if acc_num not in accounts:  # Check if this account number exists
                return acc_num


# Storage
employees = {}  # Changed from list to dict for easier lookup by email
customers = {}
accounts = {}


def employee_login():
    print("\n--- Employee Login ---")
    email = input("Enter Email: ").strip().lower()
    password = input("Enter Password: ")
    employee_id = int(input("Enter Employee ID: "))
    emp = employees.get(email)
    if emp and emp.password == password and emp.employee_id == employee_id:
        print(f"Welcome {emp.name}")
        return emp
    else:
        print("Invalid credentials.")
        return None


# Functions
def login_customer():
    print("\n--- Customer Login ---")
    ssn_id = int(input("Enter SSN ID: "))
    password = input("Enter Password: ")

    customer = customers.get(ssn_id)
    if customer and customer.password == password:
        print("\nLogin Successful! Welcome,", customer.name)
        return customer
    else:
        print("Invalid SSN ID or Password!")
        return None


def create_account():
    print("\n--- Create Account (Customer Self Registration) ---")
    name = input("Enter Name: ")
    email = input("Enter Email: ").strip().lower()
    address = input("Enter Address (Street, City): ")
    contact_number = int(input("Enter Contact Number: "))
    aadhar_number = int(input("Enter Aadhar Number: "))
    pan_number = input("Enter PAN Number: ")
    # Ensure passwords match
    while True:
        password = input("Set your password: ")
        confirm_password = input("Enter your password again: ")
        if password == confirm_password:
            break
        else:
            print("Passwords don't match. Try again.")

    # Proceed only after password is confirmed
    initial_deposit = float(input("Enter Initial Deposit Amount: "))
    account_type = input("Enter Account Type (Savings/Current): ")

    customer = Customer(name, email, address, contact_number, aadhar_number, pan_number, password)
    customers[customer.ssn_no] = customer

    new_account = Account(customer.ssn_no, account_type, initial_deposit)
    accounts[new_account.account_number] = new_account
    # Update customer with account number
    customer.account_number = new_account.account_number

    print("Account created successfully!")
    print(f"Your SSN ID: {customer.ssn_no}")
    print(f"Your Account Number: {new_account.account_number}")


def manage_customer_account(customer):
    while True:
        print("\n--- Customer Account Management ---")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. View Personal Info")
        print("5. Update Personal Info")
        print("6. Logout")
        choice = input("Enter your choice: ")

        customer_accounts = [acc for acc in accounts.values() if acc.customer_ssn_no == customer.ssn_no]
        print("Customer Accounts:", [acc.account_number for acc in customer_accounts])

        if choice in ['1', '2', '3']:
            if not customer_accounts:
                print("No accounts found for this customer.")
                continue

            print("\nAvailable Accounts:")
            for acc in customer_accounts:
                print(f"Account No: {acc.account_number}, Type: {acc.account_type}, Balance: {acc.balance}")

            acc_no = input("\nEnter Account Number you want to operate on: ")

            account = accounts.get(acc_no)
            if not account or account.customer_ssn_no != customer.ssn_no:
                print("Invalid account or unauthorized access.")
                continue

            if choice == '1':
                amount = float(input("Enter amount to deposit: "))
                account.balance += amount
                print(f"Deposit successful. New Balance: {account.balance}")

            elif choice == '2':
                amount = float(input("Enter amount to withdraw: "))
                if amount > account.balance:
                    print("Insufficient Balance!")
                elif account.balance - amount < 500:
                    print("Minimum balance of 500 must be maintained.")
                elif amount < 1000:
                    print("Minimum withdrawal amount is 1000.")
                else:
                    account.balance -= amount
                    print(f"Withdrawal successful. New Balance: {account.balance}")

            elif choice == '3':
                print(f"Current Balance: {account.balance}")

        elif choice == '4':
            view_customer_details()
        elif choice == '5':
            update_customer_details(customer)
        elif choice == '6':
            print("Logged out from Customer Account.")
            break
        else:
            print("Invalid choice.")


def register_employee():
    print("\n--- Employee Registration ---")
    name = input("Enter Employee Name: ")
    email = input("Enter Email: ").strip().lower()
    password = input("Enter Password: ")
    address = input("Enter Address: ")
    contact_number = int(input("Enter Contact Number: "))

    employee = Employee(name, email, password, address, contact_number)
    employees[employee.email] = employee  # Store employee by email for easy login lookup
    print(f"\nEmployee Registration Successful.\nEmployee ID: {employee.employee_id}")


def enter_customer_data():
    name = input("Enter Customer Name: ")
    email = input("Enter Email: ").strip().lower()
    address = input("Enter Address: ")
    contact_number = int(input("Enter Contact Number: "))
    aadhar_number = int(input("Enter Aadhar Number: "))
    pan_number = input("Enter PAN Number: ")
    # Ensure passwords match
    while True:
        password = input("Set your password: ")
        confirm_password = input("Enter your password again: ")
        if password == confirm_password:
            break
        else:
            print("Passwords don't match. Try again.")
    # Proceed only after password is confirmed
    initial_deposit = float(input("Enter Initial Deposit Amount: "))
    account_type = input("Enter Account Type (Savings/Current): ")
    customer = Customer(name, email, address, contact_number, aadhar_number, pan_number,
                        password)
    customers[customer.ssn_no] = customer

    new_account = Account(customer.ssn_no, account_type, initial_deposit)
    accounts[new_account.account_number] = new_account
    # Update customer with account number
    customer.account_number = new_account.account_number

    print("Customer Details Entered Successfully.")
    print(f"Generated SSN ID: {customer.ssn_no}")
    print(f"Generated Account Number: {new_account.account_number}")


def view_customer_details():
    print("\n--- View Customer Details ---")
    ssn_no = int(input("Enter Customer SSN No: "))
    customer = customers.get(ssn_no)
    if customer:
        display_customer(customer)
    else:
        print("Customer not Available or Deleted.")


def update_customer_details(customer=None):
    if not customer:
        ssn_no = int(input("Enter Customer SSN No: "))
        customer = customers.get(ssn_no)
    if customer:
        print("\nCurrent Details:")
        display_customer(customer)

        print("\n--- Update New Details ---")
        name=input("enter name")
        customer.name = customer.valid_name(name)
        email=input("enter email")
        if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
            customer.email = input("Invalid email format. Enter a valid email carefully: ")
        else:
            customer.email=email

        customer.address = input("Enter Address: ")[:100]
        contact_number = int(input("Enter Contact Number: "))
        customer.contact_number=customer.valid_contact(contact_number)
        aadhar_number=int(input("Enter Aadhar Number: "))
        customer.aadhar_number =customer.valid_aadhar(aadhar_number)
        pan_number=input("Enter PAN Number: ")
        customer.pan_number = customer.valid_pan(pan_number)

        print("\nCustomer Details Updated Successfully.")
    else:
        print("Customer not found.")


def delete_customer_details():
    print("\n--- Delete Customer Details ---")
    ssn_no = int(input("Enter Customer SSN No: "))
    if ssn_no in customers:
        print("\nCurrent Details before deletion:")
        customer = customers.get(ssn_no)
        display_customer(customer)
        accounts_to_delete = [acc_no for acc_no, acc in accounts.items() if acc.customer_ssn_no == ssn_no]
        for acc_no in accounts_to_delete:
            del accounts[acc_no]
        del customers[ssn_no]
        print("Customer Details Deleted Successfully.")
    else:
        print("Customer not found.")


def display_customer(customer):
    print(f"""
    SSN No        : {customer.ssn_no}
    Name          : {customer.name}
    Email         : {customer.email}
    Address       : {customer.address}
    Contact Number: {customer.contact_number}
    Aadhar Number : {customer.aadhar_number}
    PAN Number    : {customer.pan_number}
    Account Number: {customer.account_number}
    """)


def display_employees():
    print("\n--- Employee Details ---")
    for email, emp in employees.items():
        print(f"Name: {emp.name} | Email: {emp.email} | Contact: {emp.contact_number}")


def main_menu():
    while True:
        print("""======== Bank Management System ========\n
1. Register Employee/Admin
2. Admin/Employee login 
3. Customer Login (Self Management)
4. Customer Self-Registration (Create Account)
5. Exit
""")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            register_employee()
        elif choice == '2':
            emp = employee_login()
            if emp:
                while True:
                    print("""======== Employee management system =========
1. Create customer (enter customer details)
2. Manage Customer Account(Deposit,Withdraw,Check Balance,View Customer Details,Update Customer Details)
3. Delete Customer Details
4. Logout""")
                    admin_choice = input("Enter your choice: ")

                    if admin_choice == '1':
                        enter_customer_data()
                    elif admin_choice == '2':
                        emp1 = employee_login()
                        if emp1:
                            ssn_id = int(input("Enter SSN ID: "))
                            concerned_customer = customers.get(ssn_id)
                            if concerned_customer:
                                print(f"Welcome {emp.name}.You are now managing account of {concerned_customer.name}")
                                if concerned_customer:
                                    manage_customer_account(concerned_customer)
                                else:
                                    print("Invalid SSN")
                                    break
                                """print("Do you want to continue?enter fl=1 or 0 to exit")
                                fl=int(input)
                                if(fl==0):
                                    break"""

                    elif admin_choice == '3':
                        delete_customer_details()
                    elif admin_choice == '4':
                        print("Logged out from Employee Account.")
                        break
                    else:
                        print("Invalid choice")
        elif choice == '3':
            logged_in_customer = login_customer()
            if logged_in_customer:
                manage_customer_account(logged_in_customer)
        elif choice == '4':
            create_account()
        elif choice == '5':
            print("Exiting program. Thank you!")
            break
        else:
            print("Invalid choice. Enter a number between 1 to 5.")


# Start program
if __name__ == "__main__":
    main_menu()

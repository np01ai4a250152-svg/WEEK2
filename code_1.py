import os
import pandas as pd
import tkinter as tk

# Load customer data


def load_customer():
    df = pd.read_excel("Customer/customer.xlsx")
    df.columns = df.columns.str.lower()
    return df.set_index("name").to_dict(orient="index")


# Load employee data
def load_employee():
    df = pd.read_excel("Employee/employee.xlsx")
    df.columns = df.columns.str.lower()
    return df.set_index("name").to_dict(orient="index")


# Load loan data
def load_loan():
    df = pd.read_excel("Loan/loan.xlsx")
    df.columns = df.columns.str.lower()
    return df.set_index("name").to_dict(orient="index")


# Customer agent
def customer_agent(question):
    data = load_customer()

    for name in data:
        if name.lower() in question:
            if "balance" in question:
                return f"{name.title()}'s balance is {data[name]['balance']}"

            if "account" in question:
                return f"{name.title()}'s account number is {data[name]['account']}"

    return "Customer not found."


# Employee agent
def employee_agent(question):
    data = load_employee()

    for name in data:
        if name.lower() in question:
            if "salary" in question:
                return f"{name.title()}'s salary is {data[name]['salary']}"

            if "position" in question:
                return f"{name.title()}'s position is {data[name]['position']}"

    return "Employee not found."


# Loan agent
def loan_agent(question):
    data = load_loan()

    for name in data:
        if name.lower() in question:
            if "loan" in question:
                return f"{name.title()}'s Loan = {data[name]['amount']}"

            if "status" in question:
                return f"{name.title()}'s Status is {data[name]['term']}"

    return "Loan record not found."


# Router agent
def router():
    question = entry.get().lower()

    if "balance" in question or "account" in question:
        answer = customer_agent(question)

    elif "salary" in question or "position" in question:
        answer = employee_agent(question)

    elif "loan" in question or "status" in question:
        answer = loan_agent(question)

    else:
        answer = "Please specify customer, employee, or loan."

    result.config(text=answer)


# GUI
root = tk.Tk()
root.title("Customer Information System")
root.geometry("500x250")

tk.Label(root, text="Enter your question:").pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack()

tk.Button(root, text="Submit", command=router).pack(pady=10)

result = tk.Label(root, text="", font=("Arial", 12))
result.pack(pady=20)

root.ma

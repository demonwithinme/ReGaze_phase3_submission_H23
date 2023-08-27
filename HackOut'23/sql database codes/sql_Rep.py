import mysql.connector
import PySimpleGUI as sg

# Connect to the database
db = mysql.connector.connect(host='localhost', user='root', passwd='@rudrapatel7', database='hackout')
mycursor = db.cursor()

# Function to add medicine data
def add_data(data):
    query = "INSERT INTO retail(hsn_code, medicine_name, quantity, stock, rate, amount, discount, taxable_value, cgst, sgst, igst, cess, total, demand) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    mycursor.execute(query, data)
    db.commit()

# Function to retrieve medicines with stock less than demand
def get_low_stock_meds():
    mycursor.execute("SELECT hsn_code, medicine_name FROM retail WHERE stock < demand")
    return mycursor.fetchall()

# GUI Layout
layout = [
    [sg.Text("Current stock"), sg.InputText(key="stock")],
    [sg.Text("Code"), sg.InputText(key="code")],
    [sg.Text("Medicine name"), sg.InputText(key="med")],
    # Add more input fields here for other data
    [sg.Button("Add Data")],
    [sg.Listbox(values=[], size=(30, 5), key="med_list")],
    [sg.Button("Confirm")],
]

window = sg.Window("Autonomous ordering of selected medicines", layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    elif event == "Add Data":
        stock = int(values["stock"])
        code = values["code"]
        med = values["med"]
        # Add more fields here for other data
        data = (code, med, 0, stock, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        add_data(data)
    elif event == "Confirm":
        low_stock_meds = get_low_stock_meds()
        med_list = [f"Code: {code}, Medicine: {med}" for code, med in low_stock_meds]
        window["med_list"].update(values=med_list)

window.close()

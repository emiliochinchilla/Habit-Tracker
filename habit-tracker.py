import os
from tkinter import *
from tkcalendar import *
from datetime import datetime as dt
import requests
import webbrowser
from tkinter import messagebox
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API token from the .env file
TOKEN = os.getenv("TOKEN")
GRAPH_ID = "graph1"

# Create the main window
root = Tk()
root.title("Python Journey")
root.resizable(width=False, height=False)
root.config(pady=20, padx=20)
URL = "https://pixe.la/v1/users/emichin/graphs/graph1.html"
TODAY = dt.now()


def open_browser():
    # Open the user's progress graph in the web browser
    webbrowser.open(URL, new=1)


def format_date():
    # Format the date selected in the calendar to the Pixela format
    cal.config(date_pattern="yyyyMMdd")
    date = cal.get_date()
    cal.config(date_pattern="dd/MM/yyyy")
    return date


def add_pixel():
    # Add a new pixel to the user's graph
    endpoint = "https://pixe.la/v1/users/emichin/graphs/graph1/"
    pixel_add = {
        "date": format_date(),
        "quantity": user_in.get(),
    }
    response = requests.post(url=endpoint, json=pixel_add, headers=headers)
    print(response.text)
    user_in.delete(0, END)
    messagebox.showinfo(message="Pixel added.")


def del_pixel():
    # Delete a pixel from the user's graph
    endpoint = f"https://pixe.la/v1/users/emichin/graphs/graph1/{format_date()}"
    requests.delete(url=endpoint, headers=headers)
    messagebox.showinfo(message="Pixel deleted.")


def change_pixel():
    # Update an existing pixel on the user's graph
    endpoint = f"https://pixe.la/v1/users/emichin/graphs/graph1/{format_date()}"
    pixel_update = {
        "quantity": user_in.get(),
    }
    requests.put(url=endpoint, json=pixel_update, headers=headers)
    user_in.delete(0, END)
    messagebox.showinfo(message="Pixel updated.")


# Create the calendar widget
cal = Calendar(root, selectmode="day", year=TODAY.year, month=TODAY.month, day=TODAY.day)
cal.grid(row=0, column=0, columnspan=4)
units = Label(text="Minutes/Day:")
units.grid(row=1, column=0, columnspan=2, pady=10, sticky="e")
user_in = Entry(width=10)
user_in.grid(row=1, column=2, sticky="w")


# Set the headers for the API requests
headers = {
    "X-USER-TOKEN": TOKEN
}

# Create the buttons
add = Button(text="Add", command=add_pixel)
add.grid(row=2, column=0, pady=10)
update = Button(text="Update", command=change_pixel)
update.grid(row=2, column=1, pady=10, sticky="w")
delete = Button(text="Delete", command=del_pixel)
delete.grid(row=2, column=2, pady=10, sticky="w")
link = Button(text="Show\nJourney", command=open_browser)
link.grid(row=2, column=3)

# Run the main loop
root.mainloop()
Python Journey

Python Journey is a simple application built using Python and the Tkinter library. It allows users to track their daily progress in learning Python by adding, updating, and deleting "pixels" on a calendar-like graph. The application uses the Pixela API to store and manage the user's data.
Features

    Calendar-like interface to select the date
    Add, update, and delete pixels (daily progress) on the graph
    Displaying the progress on a web page using the Pixela platform

Requirements

    Python 3.x
    Tkinter library
    Tkcalendar library
    Requests library
    Dotenv library

Installation

    Clone the repository:

git clone https://github.com/your-username/python-journey.git

    Navigate to the project directory:

    cd python-journey

Create a .env file in the project directory and add your Pixela API token:

    TOKEN=your_pixela_api_token

Install the required dependencies



Usage

Run the application:

    python habit-tracker.py

    Use the calendar to select the date and enter the number of minutes spent on Python that day.
    Click the "Add", "Update", or "Delete" button to manage your progress.
    Click the "Show Journey" button to open your progress graph in the web browser.

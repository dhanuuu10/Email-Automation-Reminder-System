
import os
import pandas as pd
from datetime import datetime

# Get the main project directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Define reminders CSV file path
REMINDER_FILE = os.path.join(BASE_DIR, "data", "reminders.csv")


# Function to load reminders
def load_reminders():

    try:
        # Read reminder information
        reminders = pd.read_csv(REMINDER_FILE)

        print("\nREMINDER MANAGEMENT SYSTEM")
        print("-" * 50)

        print(reminders.to_string(index=False))

        print("\nTotal Reminders:", len(reminders))

        return reminders

    except FileNotFoundError:
        print("Error: reminders.csv file not found!")
        return None

    except Exception as e:
        print("Error loading reminders:", e)
        return None


# Function to check reminder status
def check_reminders():

    # Load reminder data
    reminders = load_reminders()

    if reminders is None:
        return

    # Get current date and time
    current_time = datetime.now()

    print("\nREMINDER STATUS")
    print("-" * 50)

    for index, reminder in reminders.iterrows():

        # Convert CSV date and time into datetime
        reminder_datetime = datetime.strptime(
            str(reminder["reminder_date"]) + " " +
            str(reminder["reminder_time"]),
            "%Y-%m-%d %H:%M"
        )

        # Get current status
        status = str(reminder["status"]).strip().lower()

        if status == "completed":
            print(reminder["name"], " - Completed")

        elif reminder_datetime <= current_time:
            print(reminder["name"], " - Due")

        else:
            print(reminder["name"], " - Pending")


# Run the program
if __name__ == "__main__":
    check_reminders()

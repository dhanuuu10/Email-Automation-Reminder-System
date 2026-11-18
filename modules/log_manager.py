
import os
import pandas as pd

# Get the main project folder
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Define the email log file path
LOG_FILE = os.path.join(BASE_DIR, "logs", "email_logs.csv")


# Function to display all email logs
def view_email_logs():

    print("\n========== EMAIL ACTIVITY LOGS ==========")

    if not os.path.exists(LOG_FILE):
        print("No email logs found.")
        return

    logs = pd.read_csv(LOG_FILE)

    if logs.empty:
        print("No email activity available.")
        return

    print(logs.to_string(index=False))


# Function to display email activity summary
def email_summary():

    print("\n========== EMAIL SUMMARY ==========")

    if not os.path.exists(LOG_FILE):
        print("No email logs found.")
        return

    logs = pd.read_csv(LOG_FILE)

    if logs.empty:
        print("No email activity available.")
        return

    total_emails = len(logs)

    successful_emails = logs["status"].astype(str).str.contains(
        "Success", case=False
    ).sum()

    failed_emails = logs["status"].astype(str).str.contains(
        "Failed", case=False
    ).sum()

    print("Total Emails Processed:", total_emails)
    print("Successful Emails:", successful_emails)
    print("Failed Emails:", failed_emails)


# Main program
if __name__ == "__main__":

    view_email_logs()

    email_summary()

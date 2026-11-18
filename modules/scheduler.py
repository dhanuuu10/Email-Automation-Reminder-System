
import os
import time
import pandas as pd
import schedule

from datetime import datetime
from modules.email_sender import send_email, save_email_log


# Get the main project directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Define reminders CSV path
REMINDER_FILE = os.path.join(BASE_DIR, "data", "reminders.csv")


# Function to check and process due reminders
def check_due_reminders():

    print("\nChecking reminders...")
    print("Current Time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    try:
        # Read reminder information
        reminders = pd.read_csv(REMINDER_FILE)

        # Check each reminder
        for index, reminder in reminders.iterrows():

            # Skip completed or already sent reminders
            if str(reminder["status"]).strip().lower() == "completed":
                continue

            if str(reminder["sent"]).strip().lower() == "true":
                continue

            # Convert reminder date and time
            reminder_datetime = datetime.strptime(
                str(reminder["reminder_date"]) + " " +
                str(reminder["reminder_time"]),
                "%Y-%m-%d %H:%M"
            )

            # Check whether reminder is due
            if reminder_datetime <= datetime.now():

                name = reminder["name"]
                email = reminder["email"]
                department = reminder["department"]
                reminder_message = reminder["reminder_message"]

                # Create email subject and message
                subject = "Reminder Notification"

                message = (
                    f"Dear {name},\n\n"
                    f"This is an automated reminder for you.\n\n"
                    f"Department: {department}\n"
                    f"Reminder: {reminder_message}\n"
                    f"Scheduled Date: {reminder['reminder_date']}\n"
                    f"Scheduled Time: {reminder['reminder_time']}\n\n"
                    f"Best Regards,\n"
                    f"Automation System"
                )

                print("\nProcessing reminder for:", name)

                try:
                    # Simulate email sending
                    result = send_email(email, subject, message)

                    # Save email activity
                    save_email_log(
                        name,
                        email,
                        subject,
                        result
                    )

                    # Mark reminder as sent
                    reminders.at[index, "sent"] = True

                    print("Reminder processed successfully!")

                except Exception as e:
                    print("Email processing failed:", e)

        # Save updated reminder information
        reminders.to_csv(REMINDER_FILE, index=False)

    except FileNotFoundError:
        print("Error: reminders.csv file not found!")

    except Exception as e:
        print("Error checking reminders:", e)


# Main scheduler function
def start_scheduler():

    print("\nEMAIL AUTOMATION SCHEDULER STARTED")
    print("-" * 45)
    print("Checking reminders every 1 minute.")
    print("Press CTRL + C to stop the scheduler.")

    # Check reminders immediately when program starts
    check_due_reminders()

    # Schedule automatic checking every minute
    schedule.every(1).minutes.do(check_due_reminders)

    # Keep the scheduler running
    while True:
        schedule.run_pending()
        time.sleep(1)


# Run the scheduler
if __name__ == "__main__":
    start_scheduler()

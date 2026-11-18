
import os
import pandas as pd
import smtplib

from datetime import datetime
from email.message import EmailMessage
from dotenv import load_dotenv

# Import email template function
from modules.template_manager import generate_email

# Load environment variables
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

load_dotenv(os.path.join(BASE_DIR, ".env"))

# Email configuration
EMAIL_MODE = os.getenv("EMAIL_MODE", "simulation").lower()
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")

# Define log file path
LOG_FILE = os.path.join(BASE_DIR, "logs", "email_logs.csv")


# Function to save email activity
def save_email_log(name, email, subject, status):

    log_data = {
        "name": name,
        "email": email,
        "subject": subject,
        "status": status,
        "date_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    file_exists = os.path.exists(LOG_FILE)

    log_df = pd.DataFrame([log_data])

    log_df.to_csv(
        LOG_FILE,
        mode="a",
        header=not file_exists,
        index=False
    )


# Function to send or simulate an email
def send_email(receiver, subject, message):

    print("\nSending Email...")
    print("-" * 40)

    print("To:", receiver)
    print("Subject:", subject)

    # Simulation mode
    if EMAIL_MODE == "simulation":

        print("Message:")
        print(message)

        print("\nEmail Status: Simulated Success")

        return "Simulated Success"

    # Gmail SMTP mode
    elif EMAIL_MODE == "live":

        if not SENDER_EMAIL or not SENDER_PASSWORD:
            raise ValueError("Gmail credentials are missing!")

        # Create email message
        email_message = EmailMessage()

        email_message["From"] = SENDER_EMAIL
        email_message["To"] = receiver
        email_message["Subject"] = subject

        email_message.set_content(message)

        # Connect to Gmail SMTP server
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:

            # Login to Gmail
            server.login(SENDER_EMAIL, SENDER_PASSWORD)

            # Send email
            server.send_message(email_message)

        print("\nEmail Status: Sent Successfully")

        return "Sent Successfully"

    else:
        raise ValueError("Invalid EMAIL_MODE. Use simulation or live.")


# Function to automate emails for all contacts
def automate_emails():

    contacts_file = os.path.join(
        BASE_DIR, "data", "contacts.csv"
    )

    contacts = pd.read_csv(contacts_file)

    for _, contact in contacts.iterrows():

        name = contact["name"]
        email = contact["email"]
        department = contact["department"]

        details = {
            "name": name,
            "department": department,
            "date": "25 November 2026",
            "time": "10:00 AM",
            "task": "Project Documentation",
            "message": "Please check the latest company announcement."
        }

        message = generate_email(
            "general_announcement.txt",
            details
        )

        if message is None:
            status = "Failed"

        else:

            email_subject = message.splitlines()[0].replace(
                "Subject: ", ""
            )

            try:
                status = send_email(
                    email,
                    email_subject,
                    message
                )

            except Exception as e:
                print("Email sending failed:", e)
                status = "Failed"

        save_email_log(
            name,
            email,
            email_subject if message else "Email Generation",
            status
        )

    print("\nEmail automation process completed!")


# Run the program
if __name__ == "__main__":
    automate_emails()


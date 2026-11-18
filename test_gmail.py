
from modules.email_sender import send_email

# Enter your own Gmail address for testing
receiver = input("Enter your test Gmail address: ")

subject = "Email Automation Project - Test"

message = """
Hello!

This is a test email from my Python Email Automation & Reminder System.

Gmail SMTP integration is working.

Regards,
Python Automation System
"""

try:
    result = send_email(receiver, subject, message)
    print("\nTest Result:", result)

except Exception as e:
    print("\nEmail sending failed:", e)

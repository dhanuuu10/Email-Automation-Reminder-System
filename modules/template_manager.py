
import os

# Get the main project directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Define the template folder
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")


# Function to load and personalize email templates
def generate_email(template_name, details):

    try:
        # Create the complete template file path
        file_path = os.path.join(TEMPLATE_DIR, template_name)

        # Open and read the template file
        with open(file_path, "r", encoding="utf-8") as file:
            template = file.read()

        # Replace placeholders with actual information
        email_content = template.format(**details)

        return email_content

    except FileNotFoundError:
        print("Error: Email template not found!")
        return None

    except KeyError as e:
        print("Missing information for template:", e)
        return None

    except Exception as e:
        print("Error generating email:", e)
        return None


# Test the email template system
if __name__ == "__main__":

    details = {
        "name": "Rahul Sharma",
        "department": "HR",
        "date": "25 November 2026",
        "time": "10:00 AM",
        "task": "Project Documentation",
        "message": "The monthly team meeting will be held next week."
    }

    # Generate an interview invitation
    email = generate_email("interview_invitation.txt", details)

    if email:
        print("\nGENERATED EMAIL")
        print("-" * 40)
        print(email)

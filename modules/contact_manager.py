
import pandas as pd
import os

# Get the project directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Define the contacts CSV file path
CONTACT_FILE = os.path.join(BASE_DIR, "data", "contacts.csv")


# Function to load contacts
def load_contacts():

    try:
        # Read contacts from CSV file
        contacts = pd.read_csv(CONTACT_FILE)

        # Check whether required columns exist
        required_columns = ["name", "email", "department"]

        for column in required_columns:
            if column not in contacts.columns:
                print("Missing column:", column)
                return None

        # Display contacts
        print("\nCONTACT LIST")
        print("-" * 40)

        print(contacts.to_string(index=False))

        print("\nTotal Contacts:", len(contacts))

        return contacts

    except FileNotFoundError:
        print("Error: contacts.csv file not found!")
        return None

    except Exception as e:
        print("Error:", e)
        return None


# Run the function
if __name__ == "__main__":
    load_contacts()

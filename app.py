
import streamlit as st
import pandas as pd
import os

# Get project folder path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

CONTACT_FILE = os.path.join(BASE_DIR, "data", "contacts.csv")
REMINDER_FILE = os.path.join(BASE_DIR, "data", "reminders.csv")
LOG_FILE = os.path.join(BASE_DIR, "logs", "email_logs.csv")

# Page configuration
st.set_page_config(
    page_title="Email Automation System",
    page_icon="📧",
    layout="wide"
)

# Dashboard title
st.title("📧 Email Automation & Reminder System")
st.write("Manage contacts, reminders and email activity.")

# Load data
contacts = pd.read_csv(CONTACT_FILE)

if os.path.exists(REMINDER_FILE):
    reminders = pd.read_csv(REMINDER_FILE)
else:
    reminders = pd.DataFrame()

if os.path.exists(LOG_FILE):
    logs = pd.read_csv(LOG_FILE)
else:
    logs = pd.DataFrame()

# Dashboard metrics
st.subheader("Dashboard Overview")

col1, col2, col3 = st.columns(3)

col1.metric("Total Contacts", len(contacts))
col2.metric("Total Reminders", len(reminders))
col3.metric("Emails Processed", len(logs))

st.divider()

# Contacts section
st.subheader("👥 Contact Management")

st.dataframe(contacts, use_container_width=True)

st.divider()

# Reminder section
st.subheader("⏰ Reminder Management")

if not reminders.empty:
    st.dataframe(reminders, use_container_width=True)
else:
    st.info("No reminders available.")

st.divider()

# Email activity section
st.subheader("📨 Email Activity Logs")

if not logs.empty:

    st.dataframe(logs, use_container_width=True)

    successful = logs["status"].astype(str).str.contains(
        "Success", case=False
    ).sum()

    failed = logs["status"].astype(str).str.contains(
        "Failed", case=False
    ).sum()

    st.write("Successful Emails:", successful)
    st.write("Failed Emails:", failed)

else:
    st.info("No email activity logs available.")

st.success("Dashboard loaded successfully!")

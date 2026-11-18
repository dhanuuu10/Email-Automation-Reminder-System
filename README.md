
# 📧 Email Automation & Reminder System

A Python-based Email Automation and Reminder System designed to automate email communication, schedule reminders, manage contacts, and track email activity through an interactive Streamlit dashboard.

## 🚀 Project Overview

This project helps automate repetitive email tasks by generating personalized emails, scheduling reminders, integrating Gmail SMTP, and maintaining email activity logs.

It provides a simple dashboard to monitor contacts, reminders, and email-sending activity.

## ✨ Features

- **Contact Management:** Manage contact information using CSV files.
- **Email Templates:** Generate personalized emails using reusable templates.
- **Email Automation:** Automate email generation and sending.
- **Gmail SMTP Integration:** Support for sending emails through Gmail.
- **Reminder Management:** Store and manage scheduled reminders.
- **Automated Scheduler:** Check and process reminders automatically.
- **Email Activity Logs:** Track successful, failed, and simulated email activity.
- **Streamlit Dashboard:** View contacts, reminders, and email logs in a web interface.

## 🛠️ Technologies Used

- Python 3.12
- Pandas
- Streamlit
- Schedule
- SMTP
- Python-dotenv
- CSV

## 📂 Project Structure

```text
Email_Automation_Reminder_System/
│
├── app.py
├── main.py
├── test_gmail.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
├── logs/
├── modules/
├── templates/
└── screenshots/
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/dhanuuu10/Email-Automation-Reminder-System.git
```

### 2. Open the project folder

```bash
cd Email-Automation-Reminder-System
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows PowerShell:

```powershell
venv\Scripts\Activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure environment variables

Create a `.env` file in the project root:

```env
EMAIL_MODE=simulation
SENDER_EMAIL=yourgmail@gmail.com
SENDER_PASSWORD=your_gmail_app_password
```

Keep your `.env` file private. Never upload it to GitHub.

## ▶️ How to Run

### Run the Streamlit Dashboard

```bash
streamlit run app.py
```

### Run Email Automation

```bash
python -m modules.email_sender
```

### Run the Scheduler

```bash
python -m modules.scheduler
```

### View Email Activity Logs

```bash
python -m modules.log_manager
```

## 🔐 Security

- Email credentials are stored in environment variables.
- The `.env` file is excluded from GitHub using `.gitignore`.
- Simulation mode is available for safe testing.
- Use Gmail App Passwords instead of your normal Gmail password when live SMTP authentication is configured.

## 🎯 Learning Outcomes

- Python programming and modular development
- File handling using CSV
- Email automation using SMTP
- Task scheduling
- Environment variable management
- Streamlit dashboard development
- Git and GitHub version control

## 👩‍💻 Author

**Dhanashri Khandagale**

GitHub: https://github.com/dhanuuu10

---

⭐ If you find this project useful, consider giving it a star!
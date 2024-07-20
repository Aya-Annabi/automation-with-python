import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time
from datetime import datetime

def send_email(to_email, subject, body):
    # Your Gmail credentials
    from_email = "your.email@gmail.com"
    app_password = "xxxx xxxx xxxx xxxx"  # This is your Google app-specific password create on from Google account

    # Create the email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, app_password)

        # Send the email to all recipients
        for to_email in to_emails:
            # Create the email
            msg = MIMEMultipart()
            msg['From'] = from_email
            msg['To'] = to_email
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            server.sendmail(from_email, to_email, msg.as_string())
            print(f"Email sent to {to_email}")

        server.quit()
    except Exception as e:
        print(f"Failed to send email. Error: {e}")

def schedule_email(date_time_str, to_emails, subject, body):
    # Parse the date and time
    date_time = datetime.strptime(date_time_str, "%Y-%m-%d %H:%M:%S")

    def job():
        send_email(to_emails, subject, body)
        return schedule.CancelJob

    # Schedule the email
    schedule.every().day.at(date_time.strftime("%H:%M:%S")).do(job)
    print(f"Email scheduled for {date_time_str} to {', '.join(to_emails)}")

if __name__ == "__main__":
    # Define the email details
    to_emails = ["email1@gmail.com","email2@gmail.com"] #you can insert as many mails as you need
    subject = "Scheduled Email Subject"
    body = "hope this email finds you well"
    
    # Define the schedule details
    date_time_str = "2023-07-29 00:00:00"
    # Schedule the email
    schedule_email(date_time_str, to_emails, subject, body)
    # Keep the script running to check the schedule
    while True:
        schedule.run_pending()
        time.sleep(1)

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Email configuration
sender_email = 'gairesantosh509@gmail.com'
sender_password = 'password is kept here'
receiver_email = 'hari.bhatta@imark.com.np'
subject = 'Monthly Bill Invoice'
body = 'Please find the attached monthly bill invoice and Excel sheet.'

# Create the email message
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

# Attach the billing invoice
invoice_filename = 'generated1_doc.docx'  # Replace with the path to your generated invoice file
attachment = open(invoice_filename, 'rb')
invoice_part = MIMEBase('application', 'octet-stream')
invoice_part.set_payload(attachment.read())
encoders.encode_base64(invoice_part)
invoice_part.add_header('Content-Disposition', f'attachment; filename= {invoice_filename}')
msg.attach(invoice_part)

# Attach the Excel sheet
excel_filename = 'siddhartha1.csv'  # Replace with the path to your Excel sheet
attachment = open(excel_filename, 'rb')
excel_part = MIMEBase('application', 'octet-stream')
excel_part.set_payload(attachment.read())
encoders.encode_base64(excel_part)
excel_part.add_header('Content-Disposition', f'attachment; filename= {excel_filename}')
msg.attach(excel_part)

# Connect to the SMTP server and send the email
try:
    smtp_server = smtplib.SMTP('smtp.gmail.com', 587)  # Use your SMTP server and port
    smtp_server.starttls()
    smtp_server.login(sender_email, sender_password)
    text = msg.as_string()
    smtp_server.sendmail(sender_email, receiver_email, text)
    smtp_server.quit()
    print("Email sent successfully.")
except Exception as e:
    print(f"Email could not be sent. Error: {str(e)}")

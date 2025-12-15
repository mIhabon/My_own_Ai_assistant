import logging
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Optional
from livekit.agents import function_tool, RunContext

@function_tool()    
async def send_email(context: RunContext, to_email: str, subject: str, 
                    message: str, cc_email: Optional[str] = None) -> str:
    """Send emails for Ihab"""
    try:
        gmail_user = os.getenv("GMAIL_USER")
        gmail_password = os.getenv("GMAIL_APP_PASSWORD")
        
        if not gmail_user or not gmail_password:
            return "Email credentials not configured."
        
        msg = MIMEMultipart()
        msg['From'] = gmail_user
        msg['To'] = to_email
        msg['Subject'] = subject
        
        recipients = [to_email]
        if cc_email:
            msg['Cc'] = cc_email
            recipients.append(cc_email)
        
        msg.attach(MIMEText(message, 'plain'))
        
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_user, recipients, msg.as_string())
        server.quit()
        
        return f"Email sent to {to_email}"
    except Exception as e:
        return f"Email failed: {str(e)}"
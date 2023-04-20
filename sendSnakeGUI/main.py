#!/usr/bin/env python

import tkinter
import smtplib
from email.message import EmailMessage
import ssl
import os


def send_email():
    smtp_email, smtp_key, smtp_relay = email_entry.get(), SMTP_key_entry.get(), SMTP_relay_entry.get()

    smtp_port = int(SMTP_port_entry.get())
    msg_entry = body_entry.get("1.0", "end-1c")

    success_message = "Sent Successfully"
    fail_message = "Failed to send email"
    try:
        if smtp_email is None or smtp_key is None:
            # no email address or password
            # something is not configured properly
            print("Did you set email address and password correctly?")
        else:

            # create email
            subject_text = subject_entry.get()
            subject_text = subject_text.strip("\n")
            from_text  = from_email_entry.get()
            from_text = from_text.strip("\n")
            msg = EmailMessage()
            msg['Subject'] = subject_text  # subject_entry.get()
            msg['From'] = from_email_entry.get()
            msg['To'] = to_email_entry.get()
            msg.set_content(msg_entry)

            # send email
            context = ssl.create_default_context()
            with smtplib.SMTP(smtp_relay, smtp_port) as smtp:
                smtp.starttls(context=context)
                smtp.login(smtp_email, smtp_key)
                smtp.send_message(msg)
                message = success_message

    except Exception as e:
        print("Problem during send email")
        print(str(e))
        message = fail_message

    print(message)



window = tkinter.Tk()
window.title("Send Snake")

frame = tkinter.Frame(window)

# Load the background image

#background_image = tkinter.PhotoImage(file="img/leviathanLogo2.png")

# Create a label for the background image and add it to the frame
#background_label = tkinter.Label(frame, image=background_image)
#background_label.place(x=0, y=0, relwidth=1, relheight=1)

frame.pack()

#---------------------------------Frame 1------------------------------------#

#Tool Configuration (Settings)
settings_frame = tkinter.LabelFrame(frame, text="Settings")
settings_frame.grid(row=0, column=0)

#SMTP E-mail Label
email_label = tkinter.Label(settings_frame, text="E-mail:")
email_label.grid(row=0, column=0)

#SMTP Key Label
SMTP_key_label = tkinter.Label(settings_frame, text="SMTP Key:")
SMTP_key_label.grid(row=0, column=1)

#SMTP Relay Label
SMTP_relay_label = tkinter.Label(settings_frame, text="SMTP Relay:")
SMTP_relay_label.grid(row=0, column=2)

#SMTP Port
SMTP_port_label = tkinter.Label(settings_frame, text="SMTP Port:")
SMTP_port_label.grid(row=2, column=0)

#Adding Entries
email_entry = tkinter.Entry(settings_frame)

SMTP_key_entry = tkinter.Entry(settings_frame)

SMTP_relay_entry = tkinter.Entry(settings_frame)

SMTP_port_entry = tkinter.Entry(settings_frame)



#Entry Placement
email_entry.grid(row=1, column=0)
SMTP_key_entry.grid(row=1, column=1)
SMTP_relay_entry.grid(row=1, column=2)
SMTP_port_entry.grid(row=3, column=0)

#---------------------------------Frame 2------------------------------------#

#E-mail Configuration (Settings)
email_frame = tkinter.LabelFrame(frame, text="E-mail")
email_frame.grid(row=1, column=0)

#From E-mail Label
from_email_label = tkinter.Label(email_frame, text="From E-mail:")
from_email_label.grid(row=0, column=0)

#To E-mail Label
to_label = tkinter.Label(email_frame, text="To E-mail:")
to_label.grid(row=1, column=0)

#Subject Label
subject_label = tkinter.Label(email_frame, text="Subject:")
subject_label.grid(row=2, column=0)

#Body Label
body_label = tkinter.Label(email_frame, text="Body:")
body_label.grid(row=3, column=0)

#Adding Entries
from_email_entry = tkinter.Entry(email_frame)

to_email_entry = tkinter.Entry(email_frame)

subject_entry = tkinter.Entry(email_frame)

body_entry = tkinter.Text(email_frame)


#Entry Placement
from_email_entry.grid(row=0, column=1)
to_email_entry.grid(row=1, column=1)
subject_entry.grid(row=2, column=1)
body_entry.grid(row=3, column=1)

#---------------------------------Frame 3------------------------------------#

#Button Configuration (Settings)
button_frame = tkinter.LabelFrame(frame, text="Send")
button_frame.grid(row=2, column=0)


#Adding Button
send_button = tkinter.Button(button_frame, text="Send", command=send_email)
send_button.pack()

window.mainloop()

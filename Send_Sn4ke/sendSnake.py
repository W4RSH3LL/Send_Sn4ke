import subprocess
from pyfiglet import Figlet
import os
import smtplib
from email.message import EmailMessage
import ssl
from colorama import Fore, Back, Style


#custom_fig = Figlet(font='shadow')
#print(custom_fig.renderText('Send Snake'))
print(Fore.GREEN + "  ██████ ▓█████  ███▄    █ ▓█████▄      ██████  ███▄    █  ▄▄▄       ██ ▄█▀▓█████")
print(Fore.GREEN +"▒██    ▒ ▓█   ▀  ██ ▀█   █ ▒██▀ ██▌   ▒██    ▒  ██ ▀█   █ ▒████▄     ██▄█▒ ▓█   ▀ ")
print(Fore.GREEN +"░ ▓██▄   ▒███   ▓██  ▀█ ██▒░██   █▌   ░ ▓██▄   ▓██  ▀█ ██▒▒██  ▀█▄  ▓███▄░ ▒███")
print(Fore.GREEN + " ▒   ██▒▒▓█  ▄ ▓██▒  ▐▌██▒░▓█▄   ▌     ▒   ██▒▓██▒  ▐▌██▒░██▄▄▄▄██ ▓██ █▄ ▒▓█  ▄")
print(Fore.GREEN + "▒██████▒▒░▒████▒▒██░   ▓██░░▒████▓    ▒██████▒▒▒██░   ▓██░ ▓█   ▓██▒▒██▒ █▄░▒████▒")
print(Fore.GREEN + "▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ▒░   ▒ ▒  ▒▒▓  ▒    ▒ ▒▓▒ ▒ ░░ ▒░   ▒ ▒  ▒▒   ▓▒█░▒ ▒▒ ▓▒░░ ▒░ ░")
print(Fore.GREEN + "░ ░▒  ░ ░ ░ ░  ░░ ░░   ░ ▒░ ░ ▒  ▒    ░ ░▒  ░ ░░ ░░   ░ ▒░  ▒   ▒▒ ░░ ░▒ ▒░ ░ ░  ░")
print(Fore.GREEN + "░  ░  ░     ░      ░   ░ ░  ░ ░  ░    ░  ░  ░     ░   ░ ░   ░   ▒   ░ ░░ ░    ░")
print(Fore.GREEN + "      ░     ░  ░         ░    ░             ░           ░       ░  ░░  ░      ░  ░")

print("\n")
print(Fore.YELLOW + "Developped by WR41TH1")
print("\n")
print("[1]. Send An Email. \n")

def sendEmail():
    email_address = "samuel.mccalla@saintmichelannecy.fr"
    email_password = "kQ1VgzKd4m0EvAyh"
    succ_message = "Sent Succesfully"
    fail_message = "Failed to send email"

    try:
        if email_address is None or email_password is None:
            # no email address or password
            # something is not configured properly
            print(Back.RED + "Did you set email address and password correctly?")
        else:
            subject = input(Fore.GREEN + "Please Enter The Subject Of Your Email \n[*] Subject: ")
            from_email_address = input(Fore.GREEN + "Please Enter The From Email \n[*] From Email: ")
            to = input(Fore.GREEN + "Please Enter The Receipient\n[*] To: ")
            message = input(Fore.GREEN + "Please Enter The Content Of Your Message \n[*] Message: ")

            # create email
            msg = EmailMessage()
            msg['Subject'] = subject
            msg['From'] = from_email_address
            msg['To'] = to
            msg.set_content(message)

            # send email
            context = ssl.create_default_context()
            with smtplib.SMTP('smtp-relay.sendinblue.com', 587) as smtp:
                smtp.starttls(context=context)
                smtp.login(email_address, email_password)
                smtp.send_message(msg)
                message = succ_message

    except Exception as e:
        print(Back.RED + Fore.WHITE + "Problem during send email")
        print(str(e))
        message = fail_message
    return message

user_option_response = input(Fore.GREEN + "Please Select An Option From The List Above.\n[*] Option > \n")

if user_option_response == '1':
    sendEmail()
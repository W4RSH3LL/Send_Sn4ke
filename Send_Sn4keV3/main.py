import smtplib
from email.message import EmailMessage
import ssl
from colorama import Fore, Back, Style

def settings():
    print(Fore.YELLOW + "This Page Is Used To Configure The Login Infos For Your SMTP Server\n")
    SMTP_address = input("Please Enter The E-Mail Used For Your SMTP Server\n")
    SMTP_password = input("Please Enter The Password Used For Your SMTP Server\n")
    print("[+] Settings Modified Success!\n")
    print(SMTP_address + " " + SMTP_password)
    main(SMTP_address, SMTP_password)

def sendEmail(SMTP_address, SMTP_password):
    succ_message = "Sent Succesfully"
    fail_message = "Failed to send email"
    try:
        if SMTP_address is None or SMTP_password is None:
            # no email address or password
            # something is not configured properly
            print(Back.RED + "Did you set email address and password correctly?")
        else:
            print(SMTP_address + " " + SMTP_password + "\n")
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
                smtp.login(SMTP_address, SMTP_password)
                smtp.send_message(msg)
                message = succ_message

    except Exception as e:
        print(Back.RED + Fore.WHITE + "Problem during send email")
        print(str(e))
        message = fail_message
    return message

def main(SMTP_address, SMTP_password):
    # custom_fig = Figlet(font='shadow')
    # print(custom_fig.renderText('Send Snake'))
    print(Fore.GREEN + "  ██████ ▓█████  ███▄    █ ▓█████▄      ██████  ███▄    █  ▄▄▄       ██ ▄█▀▓█████")
    print(Fore.GREEN + "▒██    ▒ ▓█   ▀  ██ ▀█   █ ▒██▀ ██▌   ▒██    ▒  ██ ▀█   █ ▒████▄     ██▄█▒ ▓█   ▀ ")
    print(Fore.GREEN + "░ ▓██▄   ▒███   ▓██  ▀█ ██▒░██   █▌   ░ ▓██▄   ▓██  ▀█ ██▒▒██  ▀█▄  ▓███▄░ ▒███")
    print(Fore.GREEN + " ▒   ██▒▒▓█  ▄ ▓██▒  ▐▌██▒░▓█▄   ▌     ▒   ██▒▓██▒  ▐▌██▒░██▄▄▄▄██ ▓██ █▄ ▒▓█  ▄")
    print(Fore.GREEN + "▒██████▒▒░▒████▒▒██░   ▓██░░▒████▓    ▒██████▒▒▒██░   ▓██░ ▓█   ▓██▒▒██▒ █▄░▒████▒")
    print(Fore.GREEN + "▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ▒░   ▒ ▒  ▒▒▓  ▒    ▒ ▒▓▒ ▒ ░░ ▒░   ▒ ▒  ▒▒   ▓▒█░▒ ▒▒ ▓▒░░ ▒░ ░")
    print(Fore.GREEN + "░ ░▒  ░ ░ ░ ░  ░░ ░░   ░ ▒░ ░ ▒  ▒    ░ ░▒  ░ ░░ ░░   ░ ▒░  ▒   ▒▒ ░░ ░▒ ▒░ ░ ░  ░")
    print(Fore.GREEN + "░  ░  ░     ░      ░   ░ ░  ░ ░  ░    ░  ░  ░     ░   ░ ░   ░   ▒   ░ ░░ ░    ░")
    print(Fore.GREEN + "      ░     ░  ░         ░    ░             ░           ░       ░  ░░  ░      ░  ░\n")
    print(Fore.YELLOW + "𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗽𝗲𝗱 𝗯𝘆: 𝗪𝗥𝟰𝟭𝗧𝗛𝟭")
    print(Fore.RED + "[!]Please Configure The Settings Before Using[!]\n")
    print("╔═══════════════════════╗")
    print("║ [1]. Send An Email    ║")
    print("║ [2].   Settings       ║")
    print("║ [Any].   Exit         ║")
    print("╚═══════════════════════╝")
    user_option_response = int(input(Fore.GREEN + "Please Select An Option From The List Above.\n [*] Option > "))

    match user_option_response:
        case 1:
            sendEmail(SMTP_address, SMTP_password)
        case 2:
            settings()
        case _:
            exit()

SMTP_address = " "
SMTP_password = " "
main(SMTP_address, SMTP_password)
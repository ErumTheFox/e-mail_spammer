from email.mime.text import MIMEText
from time import sleep
from random import randint
import smtplib
from colored import fg, attr
import os


def boot():
    print("======================================================================")
    print("|                        E-Mail Spammer Tool                         |")
    print("|                            Made by %sErum%s                            |" % (fg(1), attr(0)))
    print("======================================================================")

boot()
username = input(str("Your E-Mail Address    : "))
password = input(str("Your E-Mail Password   : "))

def server_start():
    server = smtplib.SMTP("smtp.gmail.com")
    server.ehlo()
    server.starttls()
    server.login(username, password)
    return server

def spamm(server):
    emails = input(str("Victims E-Mail         : "))
    print("%sPress 'Ctrl+C' to close the program!%s" % (fg(2), attr(0)))
    for mailanz in range(1, 1000):
        print(f"=={mailanz}== mail(s) have been sent!")
        msg = MIMEText(
        "We will never forget!" + str(randint(1,9999))
        )
        msg["Subject"] = "We will never forget what you have done! " + str(randint(1, 9999))
        msg["From"] = username
        msg["To"] = emails
        server.sendmail(username, emails, msg.as_string())

def main():
    while True:
        server = server_start()
        try:
            spamm(server)
        except Exception as e:
            sleep(60)

try:
    while True:
        main()

except KeyboardInterrupt:
    print("Program has been closed!")
    pass    

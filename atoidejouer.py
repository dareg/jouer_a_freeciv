#! /usr/bin/env python3

from email.message import EmailMessage
import smtplib
import time
import re
import os
from argparse import ArgumentParser

fromaddr="sender@example.net"
fromaddr_pass="password"
smtp_server="mail.example.net"
smtp_port=465
#The addresses must be in the play order
people=["alexandre@example.net", "napoleon@example.net", "cesar@example.net"]

parser = ArgumentParser()
parser.add_argument("--save_dir", help="Path to the directory containing the saves")
args = parser.parse_args()


f = open("server.log")
#Read all the file to ignore previous turns
f.readlines()
next_player = 0

while True:
    time.sleep(30)
    send_email = False
    #Parse new line in the log file in order to find the mention of a new turn
    for line in f:
        if re.search("End/start-turn", line):
            if line == None:
                print ('No matches found')
            else:
                send_email = True
                print("Will send email")

    if send_email:
        next_player = next_player + 1
        #Get the turn number from the name of the save files
        saves = os.listdir(args.save_dir)
        saves.sort()
        m = re.search('T[0-9]+', saves[-1])

        msg = EmailMessage()
        msg['From'] = fromaddr
        msg['To'] = people[next_player%4]
        msg.preamble = 'Free-ee-civ!'

        msg['Subject'] = 'À toi de jouer ! ' + m.group(0)


        text = "Looks like it is time to play Freeciv !\n Adding some more text because sometimes when there isn't enough some email provider consider it's spam. It could replaced by some interesting text."

        msg.set_content(text)

        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        server.login(fromaddr, fromaddr_pass)
        server.send_message(msg)

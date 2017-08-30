#!/usr/bin/env python
import calendar
import os
import pysftp
import datetime
import email_me #our email_me.py script

HOSTNAME = "INSERT_IP_ADDRESS_HERE"     # IP address of server (Raspberry Pi)
USERNAME = "INSERT_USERNAME_HERE"             # Username of user on server (default is pi)
PASSWORD = "INSERT_PASSWORD_HERE"      # Password of user on server (default is raspberry, but you should change it to something else)

NAME = "INSERT_NAME_HERE"              # Just put your own name here, this will make the email look nicer

REMOTEPATH = "/home/INSERT_DIRECTORY_HERE"    # Path ON YOUR SERVER (raspberry pi) to store your files on

folderArr = ['INSERT_PATH_TO_FOLDER','INSERT_PATH_TO_FOLDER']   # Array of LOCAL paths to folders you want to store

def storeFolders():
    numDirs = 0
    for folder in folderArr:
        print("Storing: " + folder)
        copyDir(folder)
        numDirs = numDirs + 1
    currTime = datetime.datetime.now()
    currTime = (str(currTime.hour) + ":" + str(currTime.minute) + " on " + str(calendar.month_name[currTime.month]) + " " + str(currTime.day))
    updateLog(NAME + " just backed up: " + str(numDirs) + " directories at: " + str(currTime))
    # Call the email script to notify us that a backup was made
    email_me.sendEmail(NAME + " just backed up: " + str(numDirs) + " directories at: " + str(currTime))

def copyDir(str):
    with pysftp.Connection(HOSTNAME, username = USERNAME, password = PASSWORD) as sftp:
        sftp.put_r(str, REMOTEPATH)

# Optional function to store a text file log of all backups
def updateLog(text):
    f = open('cloudLog.txt', 'a')
    f.write(text+"\n")

if __name__ == "__main__":
    storeFolders()

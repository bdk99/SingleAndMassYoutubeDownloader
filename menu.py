from time import sleep
import os
import sys


print (30 * '-')
print ("   Y O U T U B E - D O W N L O A D E R !")
print (30 * '-')
print ("1. Single Download")
print ("2. Batch Download using file")
print (30 * '-')
 
## Get input ###
choice = input('Enter your choice [1-2] : ')

### Convert string to int type ##
choice = int(choice)
### Take action as per selected menu-option ###

if choice == 1:
        URL = input('Enter a URL to begin download: ')
        os.system("youtube-dl.exe --print-traffic "+URL)
elif choice == 2:
        os.system("youtube-dl.exe --print-traffic --batch-file youtubebatch.txt")
#elif choice == 3:
 #       print ("Rebooting the server...")
else:   ## default ##
        print ("Invalid number. Try again...")
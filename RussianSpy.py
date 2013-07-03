import os
import urllib2
from urllib2 import URLError
from urllib2 import HTTPError
import urllib
import shutil
import sys
import base64
import time
import subprocess
import socket
from datetime import datetime


print """ 

    ____                  _                _____            
   / __ \__  ____________(_)___ _____     / ___/____  __  __
  / /_/ / / / / ___/ ___/ / __ `/ __ \    \__ \/ __ \/ / / /
 / _, _/ /_/ (__  |__  ) / /_/ / / / /   ___/ / /_/ / /_/ / 
/_/ |_|\__,_/____/____/_/\__,_/_/ /_/   /____/ .___/\__, /  
                                            /_/    /____/
"""

time.sleep(2)
os.system("cls")

input = raw_input("1)Get server information\n2)Get PHP version\n3)Download source code of a website\n4)Union Based SQL injection checker/exploiter\n\n") #User Options are displayed here

if input == "1":
	answer = raw_input("\nEnter the website you want to scan:")
	response = urllib2.urlopen("http://" + answer)
	info = response.info()
	html = response.read()
	# do something
	response.close()  # best practice to close the file
	# this is how to process the http header
	for h in info.headers:
                if h.startswith('Server'):
                        print "\n[+]One moment please..." + " " + "\n" + h

elif input == "2":
        answer = raw_input("\nEnter the website you want to scan:")
	response = urllib2.urlopen("http://" + answer)
	info = response.info()
	html = response.read()
	response.close()
	for h in info.headers:
		if h.startswith("X-Powered-By"):
			print "\n[*]Give me one sec please..." + " " + "\n" + h
	#need to add exceptions

elif input == "3":
	answer = raw_input("\nEnter the website to download the source code:")
	request = urllib2.Request("http://" + answer)
	response = urllib2.urlopen(request)
	html = response.read()
	print html

	print "\n\nWould you like to download the source code" #Asks the user if they want to download the source code
	question = raw_input("\n\nEnter yes or no:") #The user will input their answer here
	if question.lower() == "yes":
		text_file = open("Saved_Source_code.txt", "w")
		text_file.write(html)
		text_file.close()
		print "The file has been created successfully and is named Saved_Source_code.txt"

	elif question.lower() == "no":
		print "Very well then.Thanks for using Russian Spy."
		time.sleep(2)
		sys.exit()

	else:
		print "\nWhoa,something went wrong"
		time.sleep(2)
		sys.exit()

elif input == "4":
	url = raw_input("\nEnter the website:")
	request = urllib2.Request(url)
	response = urllib2.urlopen(request)
	html = response.read()

	if "You have an error in your SQL Syntax" or "Query Failed":
		print "\nThis site is vulnerable to Union Based SQL injection"
    	print "\n\nI am still working on the rest of the SQL injection part!"

    else:
    	print "\nSorry this website is not vulnerable to SQL injection."


else:
        print "\nOops,something went wrong"
        time.sleep(2)
        sys.exit()

raw_input()

import os
import urllib2
import json
import time

def checkConnected():
	try:
		response = urllib2.urlopen("http://192.168.2.3/", timeout = 5)
		return json.load(response)
	except urllib2.URLError as e:
		print e.reason

def clickAction():
    os.system("./autoClicker -x 550 -y 880")
    os.system("./autoClicker -x 570 -y 600")
	time.sleep(1)
	print "clicking!!"

def start():
	while True:
		if checkConnected() != None:
			clickAction()

start()
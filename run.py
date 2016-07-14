import xml.etree.cElementTree as ET
import urllib2
import json
import os
import time

lastLat = ""
lastLng = ""

def clickAction():
    os.system("./autoClicker -x 550 -y 880")
    time.sleep(1)
    os.system("./autoClicker -x 570 -y 600")
    time.sleep(1)
    print "clicking!!"

def getPokemonLocation():
    try:
        #response = urllib2.urlopen("http://192.168.2.3/", timeout = 100)
        response = urllib2.urlopen("http://10.26.26.52/", timeout = 100)
        return json.load(response)
    except urllib2.URLError as e:
        print e.reason

def generateXML():
    global lastLat, lastLng
    geo = getPokemonLocation()
    if geo != None:
        if geo["lat"] != lastLat or geo["lng"] != lastLng:
            lastLat = geo["lat"]
            lastLng = geo["lng"]
            gpx = ET.Element("gpx", version="1.1", creator="Xcode")
            wpt = ET.SubElement(gpx, "wpt", lat=geo["lat"], lon=geo["lng"])
            ET.SubElement(wpt, "name").text = "PokemonLocation"
            ET.ElementTree(gpx).write("pokemonLocation.gpx")
            print "Location Updated!", "latitude:", geo["lat"], "longitude:" ,geo["lng"]
            clickAction()

def start():
    while True:
        generateXML()

start()

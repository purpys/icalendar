import tkinter
import tkinter.filedialog
import os





tformat = "%Y%m%dT%H%M%SZ"

repattern = "DTSTART:([0-9]+T[0-9]+Z)[\n\r]+DTEND:([0-9]+T[0-9]+Z)"

import time

import re

def run():

    root = tkinter.Tk()
    root.withdraw() #use to hide tkinter window
    
    currdir = os.getcwd()
    tempdir = tkinter.filedialog.askopenfilename(parent=root, initialdir=currdir, title='Please select a file')
    if len(tempdir) > 0:
        print("Parsing:\n\t%s\n" % tempdir)
    else:
        exit(1)

    path = "C:\\Users\\p275309\\Downloads\\ical\\WODC_rug.nl_6dn9bvbccme0vqpun422f9jnl0@group.calendar.google.com.ics"
    path = tempdir
    
    with open(path, 'r') as f:
        contents = f.read()

    all_matches = re.findall(repattern, contents)

    hours = 0

    for match in all_matches:
        start=time.strptime(match[0], tformat)
        if start.tm_mon < 8:
            continue
        end=time.strptime(match[1], tformat)
        hours+=(time.mktime(end)-time.mktime(start))/3600
        
    return hours
#t = time.strptime("", tformat)

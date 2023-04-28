#!/usr/bin/python3
#Python script that fetches https://alx-intranet.hbtn.io/status

#You must use the package urllib
#You are not allowed to import any packages other than urllib
#The body of the response must be displayed like the following example (tabulation before -)
#You must use a with statement
import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read()

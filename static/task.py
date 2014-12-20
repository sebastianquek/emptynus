import urllib.request
import os

ACAD_YEAR = "2014-2015"
SEM = "2"
URL = "http://api.nusmods.com/{}/{}/timetable.json".format(ACAD_YEAR, SEM)

print(os.path.dirname(os.path.realpath(__file__)))
print("Downloading " + URL)
print(urllib.request.urlretrieve(URL, "./static/timetable.json"))
print("Done.")
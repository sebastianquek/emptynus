import urllib.request

ACAD_YEAR = "2014-2015"
SEM = "2"
URL = "http://api.nusmods.com/{}/{}/timetable.json".format(ACAD_YEAR, SEM)

print("Downloading " + URL)
print(urllib.request.urlretrieve(URL, "timetable.json"))
print("Done.")
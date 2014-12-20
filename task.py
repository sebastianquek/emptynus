import urllib
import os
import heroku3

ACAD_YEAR = "2014-2015"
SEM = "2"
URL = "http://api.nusmods.com/{}/{}/timetable.json".format(ACAD_YEAR, SEM)

print(os.path.dirname(os.path.realpath(__file__)))
print("Downloading " + URL)
print(urllib.urlretrieve(URL, "timetable.json"))
print("Downloaded successfully.")

print("Restarting dyno")
HEROKU_TOKEN = "8f8bc684-8a7f-4ce0-ad92-1875a0c0c233"  #used for instance restart
APP_NAME = "emptynus"
def restart_heroku():
	cloud = heroku3.from_key(HEROKU_TOKEN)
    app = cloud.apps()[APP_NAME]
    for dyno in app.dynos():
    	dyno.kill()

restart_heroku()
print("Restarted successfully.")
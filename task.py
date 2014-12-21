import os
import heroku3

print("Restarting dyno")

HEROKU_TOKEN = os.environ["HEROKU_TOKEN"]
APP_NAME = "emptynus"

def restart_heroku():
	cloud = heroku3.from_key(HEROKU_TOKEN)
	app = cloud.apps()[APP_NAME]
	for dyno in app.dynos():
		dyno.kill()

restart_heroku()

print("Restarted successfully.")
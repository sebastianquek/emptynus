from flask import Flask, render_template, redirect, url_for, request, session, flash
from functools import wraps
import requests
import os.path, time

app = Flask(__name__)

ACAD_YEAR = "2015-2016"
SEM = "1"
URL = "http://api.nusmods.com/{}/{}/timetable.json".format(ACAD_YEAR, SEM)

data = requests.get(URL)
timetable = data.json()
last_modified = requests.get(URL).headers["last-modified"]
print("Retrieved timetable.json, last-modified: {}".format(last_modified))

class Slot():
	def __init__(self, code, name, slot):
		self.code = code
		self.name = name
		self.lesson_type = slot.get("LessonType")
		self.class_num = slot.get("ClassNo")
		self.venue = slot.get("Venue")
		self.start_time = slot.get("StartTime")
		self.end_time = slot.get("EndTime")
		self.day = slot.get("DayText")
		self.week = slot.get("WeekText")

def get_valid_times():
	times = []
	for i in range(6, 24):
		times.append('{i:02d}00'.format(i=i))
		times.append('{i:02d}30'.format(i=i))
	return times

valid_times = get_valid_times()
valid_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
valid_days_lowercase = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

def is_valid(day, time):
	if (day == "" or day.lower() in valid_days_lowercase) and \
		(time == "" or time in valid_times):
		return True
	return False

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def home(path):
	return redirect(url_for("search"))

@app.route("/search")
def search():
	error = None
	results = []
	if request.query_string:
		day = request.args.get("day", "")
		time = request.args.get("time", "")
		venue = request.args.get("venue", "")
		if is_valid(day, time):
			for mod in timetable:
				code = mod.get("ModuleCode")
				name = mod.get("ModuleTitle")
				for slot in mod.get("Timetable", ()):
					if ((day == "" or day.lower() in slot.get("DayText").lower()) 
						and (time == "" or slot.get("StartTime") <= time <= slot.get("EndTime"))
						and (venue == "" or venue.lower() in slot.get("Venue").lower())):
						results.append(Slot(code, name, slot))
			if results == []:
				error = "No results"
		else:
			return redirect(url_for("search"))
	# data=dict(request.args.items())
	return render_template("search.html", error=error, days=valid_days, times=valid_times, results=results)

@app.route("/status")
def status():
	return last_modified

if __name__ == '__main__':
	app.run(debug=False)

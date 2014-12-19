from flask import Flask, render_template, redirect, url_for, request, session, flash
from functools import wraps
import json

app = Flask(__name__)

with open("static/timetable.json", "r") as in_file:
    text = in_file.read()
timetable = json.loads(text)

def get_valid_times():
	times = []
	for i in range(6, 24):
		times.append('{i:02d}00'.format(i=i))
		times.append('{i:02d}30'.format(i=i))
	return times

valid_times = get_valid_times()
valid_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

class Slot():
	def __init__(self, code, name, slot):
		self.code = code
		self.name = name
		self.lesson_type = slot.get("LessonType")
		self.class_num = slot.get("ClassNo")
		self.venue = slot.get("Venue")
		self.start_time = slot.get("StartTime")
		self.end_time = slot.get("EndTime")

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def home(path):
	return redirect(url_for("search"))

@app.route("/search")
def search():
	error = None
	results = []
	if request.query_string:
		day = request.args.get("day")
		time = request.args.get("time")
		venue = request.args.get("venue").lower()
		for mod in timetable:
			code = mod.get("ModuleCode")
			name = mod.get("ModuleTitle")
			for slot in mod.get("Timetable", ()):
				if ((day == None or day == "" or day in slot.get("DayText")) 
					and (time == None or time == "" or slot.get("StartTime") <= time <= slot.get("EndTime"))
					and (venue == None or venue == "" or venue in slot.get("Venue").lower())):
					#print(slot)
					# results.append("{} {} {}, {}, {} {} to {}".format(code, name, slot.get("LessonType"), slot.get("Venue"), slot.get("DayText"), slot.get("StartTime"), slot.get("EndTime")))
					results.append(Slot(code, name, slot))
		if results == []:
			error = "No results"
	# data=dict(request.args.items())
	return render_template("search.html", error=error, days=valid_days, times=valid_times, results=results)

if __name__ == '__main__':
	app.run(debug=True)

import json
with open("timetable.json", "r") as in_file:
    text = in_file.read()
timetable = json.loads(text)

def find(timetable, day=None, time=None, venue=None):
	for mod in timetable:
		code = mod.get("ModuleCode")
		name = mod.get("ModuleTitle")
		for slot in mod.get("Timetable", ()):
			if ((day == None or day in slot.get("DayText")) 
				and (time == None or slot.get("StartTime") <= time <= slot.get("EndTime"))
				and (venue == None or venue in slot.get("Venue"))):
				#print(slot)
				print("{} {} {}, {}, {} {} to {}".format(code, name, slot.get("LessonType"), slot.get("Venue"), slot.get("DayText"), slot.get("StartTime"), slot.get("EndTime")))

day = "Tuesday"
time = None
venue = "COM1-0210"
find(timetable, day, time, venue)

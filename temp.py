# res = []
# for i in range(6, 24):
# 	res.append('{i:02d}00'.format(i=i))
# 	res.append('{i:02d}30'.format(i=i))

# print(res)

import json

with open("static/timetable.json", "r") as in_file:
    text = in_file.read()
timetable = json.loads(text)

res = {}
for entry in timetable:
	for slot in entry.get("Timetable", ()):
		print(slot)
		venue = slot.get("Venue")
		if venue not in res:
			res[venue] = 1
print(res.keys())
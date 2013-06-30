import praw
import time
import sys

from collections import deque
from password import PASSWORD


WAIT_TIME = 60*60*2

SUPER_PRIVILEGED = [
	"SOTB-bot",
	"xvvhiteboy",
	"SOTB-human"
]

if "queueing" in sys.argv:
	queueing = True
	startWait = time.time()
else:
	queueing = False




r = praw.Reddit(user_agent="/r/ModEveryone script by /u/SOTB-bot")
r.login("SOTB-bot", PASSWORD)


placeholder = ""
modlogPlaceholder = ""
peopleToMod = deque([])
blacklist = []




# Load data from disk before starting.
file = open("placeholders.txt")
lines = file.readlines()
placeholder = lines[0]
modlogPlaceholder = lines[1]
file.close()

file = open("peopleToMod.txt")
for line in file.readlines():
	st = line[:-1]
	if st and st not in peopleToMod:
		peopleToMod.append(st)
file.close()

file = open("blacklist.txt")
for line in file.readlines():
	st = line[:-1]
	if st and st not in blacklist:
		blacklist.append(st)
file.close()


#only do this once
"""
for p in peopleToMod:
	r.get_redditor(p).send_message("Your modship request has been queued","You will be modded once our SUBREDDIT_RATELIMIT is lifted. Thank you for your patience.")
	print "messaged", p
print "done messaging"
#"""

def dumpMemory():
	try:
		file = open("placeholders.txt","w")
		file.write(placeholder+"\n"+modlogPlaceholder)
		file.close()

		file = open("peopleToMod.txt", "w")
		file.write("")
		file.close()

		file = open("peopleToMod.txt", "a")
		for user in peopleToMod:
			file.write(str(user)+"\n")
		file.close()
		print "memory succesfully dumped."
	except:
		print "exception in dumping memory."




rall = r.get_subreddit("all")
rme = r.get_subreddit("ModEveryone")
while True:
	print "...starting loop"
	try:
		commentsGen = rall.get_comments(place_holder=placeholder, limit=1000)
		comments = [x for x in commentsGen]
		placeholder = comments[0].id
		comments = comments[:-1]
		print "got", len(comments), "from /r/all"
		for comment in comments:
			lc = comment.body.lower()
			if "/r/modeveryone" in lc:
				if str(comment.author) not in blacklist:
					print "adding", str(comment.author), "to queue"
					peopleToMod.append(str(comment.author))
					if queueing:
						comment.author.send_message("Your modship request has been queued","You will be modded once our SUBREDDIT_RATELIMIT is lifted. Thank you for your patience.")
						print "messaged", str(comment.author)
		dumpMemory()
	except Exception, ex:
		print "error in trawling:", ex
		print "try next loop..."


	if not queueing:
		for i in range(12):
			if len(peopleToMod) == 0:
				break

			try:
				person = peopleToMod[0]
				result = rme.add_moderator(person)
				if result['errors']:
					err = str(result['errors'])
					print "error in adding mod:", err
					if "that user is already a moderator" in err:
						peopleToMod.popleft()
					else:
						raise Exception(err)
				else:
					print "successfully added moderator:", person
					peopleToMod.popleft()
			except Exception, ex:
				print "error in modding:", ex
				if "that user is already a moderator" in str(ex):
					peopleToMod.popleft()
				elif "SUBREDDIT_RATELIMIT" in str(ex):
					print "we've hit the limit."
					queueing = True
					startWait = time.time()
				else:
					print "we will stop till next time."
					break
		dumpMemory()
	else:
		print "have we waited long enough yet?"
		if time.time() - startWait > WAIT_TIME:
			print "yes."
			queueing = False
			startWait = None
		else:
			print "no."

	try:
		print "checking for removemoderator events."

		removalsGen = rme.get_mod_log(place_holder = modlogPlaceholder, action="removemoderator")
		removals = [x for x in removalsGen]
		modlogPlaceholder = removals[0].id
		removals = removals[:-1]
		print "got", len(removals), "removemoderator events"
		for removal in removals:
			if removal.mod_id36 != removal.target_fullname[3:]: #It's okay to remove yourself
				nazi = removal.mod
				if nazi not in SUPER_PRIVILEGED:
					print "unauthorized removemoderator detected!", nazi
					blacklist.append(nazi)
					rme.remove_moderator(nazi)
					rme.ban(nazi)
		dumpMemory()
	except Exception, ex:
		print "exception in trawling modlog:", str(ex)


	print "sleeping..."

	time.sleep(31)

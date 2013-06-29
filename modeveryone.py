import praw
import time
from collections import deque
from password import PASSWORD


r = praw.Reddit(user_agent="/r/ModEveryone script by /u/SOTB-bot")
r.login("SOTB-bot", PASSWORD)


placeholder = ""
peopleToMod = deque([])


# Load data from disk before starting.
file = open("placeholder.txt")
for line in file.readlines():
  placeholder = line
	break
file.close()

file = open("peopleToMod.txt")
for line in file.readlines():
	st = line[:-1]
	if st:
		peopleToMod.append(st)
file.close()



def dumpMemory():
	try:
		file = open("placeholder.txt","w")
		file.write(placeholder)
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
				print "adding", str(comment.author), "to queue"
				peopleToMod.append(str(comment.author))
		dumpMemory()
	except Exception, ex:
		print "error in trawling:", ex
		print "try next loop..."


	while True:
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
			else:
				print "we will stop till next time."
				break
	dumpMemory()

	print "sleeping..."

	time.sleep(60)

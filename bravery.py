import time
import praw
import random



######################################################################

# BEGIN BRAVERY RULES.



# Replies with "/r/onetruegod" to anyone who mentions Nicolas Cage
# but doesn't mention r/onetruegod.
# This rule brought to you by: /u/SurvivalOfTheBravest
def oneTrueGod(comment,body):
	lowercaseComment = body.lower()
	if "nicolas cage" in lowercaseComment or "nick cage" in lowercaseComment:
		if "r/onetruegod" not in lowercaseComment:
			return ("/r/onetruegod", comment)
	# If we've gotten here, then none of the conditions have been met, so...
	return None


# Replies to any comment that mentions Sarah Jessica Parker but is
# less than 40 characters long, with a picture of someone beating
# a dead horse.
# This rule brought to you by: /u/SurvivalOfTheBravest
def sarahJessicaParker(comment,body):
	if "sarah jessica parker" in body.lower() and len(body) < 40:
		horseBeatingPics = [
			"http://i.imgur.com/lgP2z.jpg",
			"http://i.imgur.com/DM5xm.jpg",
			"http://i.imgur.com/0KZK3.gif",
		]
		return (random.choice(horseBeatingPics), comment)
	return None


# Replies with "/r/MURICA" to anyone who emphatically mentions
# AMERICA but not r/MURICA.
# This rule brought to you by: /u/SurvivalOfTheBravest
def murica(comment,body):
	lowercaseComment = body.lower()
	if "MURICA" in body or "AMERICA" in body or " america!" in lowercaseComment:
		if "r/murica" not in lowercaseComment:
			return ("/r/MURICA", comment)
	return None


# I think you can guess what this is supposed to do...
# This rule brought to you by: /u/TheSox3
def anneFrankly(comment,body):
	lowercaseComment = body.lower()
	if "anne frankly i did not see that coming" in lowercaseComment:
		return("shut the fuck up you unoriginal faggot",comment)
	return None


# This rule brought to you by: /u/RollCakeTroll
def atheismIsShit(comment,body):
	lowercaseComment = body.lower()
	if "this is why /r/atheism is shit" in lowercaseComment:
		return("Ctrl-F \"this is why /r/atheism is shit\", was not dissapointed",comment)
	return None


# This rule brought to you by: /u/RollCakeTroll
def noWords(comment,body):
	lowercaseComment = body.lower()
	if "i have no words" in lowercaseComment:
		wordCount = len(body.split(" "))#make some shit that counts how many words, named wordCount here
		return("\"I have no words\"? Sounds like you have at least "+ wordCount + " words.",comment)
	return None



# END BRAVERY RULES

######################################################################




# BEGIN DARK ATHEIST PYTHON MAGIC

listOfRules = {
	oneTrueGod:"oneTrueGod",
	sarahJessicaParker:"sarahJessicaParker",
	murica:"murica",
	anneFrankly:"anneFrankly",
	atheismIsShit:"atheismIsShit",
	noWords:"noWords"
}

trackingSubreddits = [
	"test",
	"braveryjerk",
	"circlejerk",
	"pics",
	"funny",
	"politics",
	"gaming",
	"AskReddit"
	"videos",
	"IAmA",
	"WTF",
	"aww",
	"atheism",
	"AdviceAnimals",
]

threadsWeveRepliedTo = {}
file = open("threads.txt")
for line in file.readlines():
	array = line.split()
	ruleName = array[0]
	list = array[1:]
	threadsWeveRepliedTo[ruleName] = list
file.close()

repliesWeveMade = {}
file = open("replies.txt")
for line in file.readlines():
	array = line.split()
	ruleName = array[0]
	list = array[1:]
	repliesWeveMade[ruleName] = list
file.close()

file = open("placeHolder.txt")
placeHolder = file.readlines()[0].strip()
file.close()

def dumpMemory():
	global placeHolder

	file = open("threads.txt","w")
	file.write("")
	file.close()
	file = open("threads.txt","a")
	for ruleName in threadsWeveRepliedTo:
		file.write(ruleName+" ")
		for threadID in threadsWeveRepliedTo[ruleName]:
			file.write(threadID+" ")
		file.write("\n")
	file.close()

	file = open("replies.txt","w")
	file.write("")
	file.close()
	file = open("replies.txt","a")
	for ruleName in repliesWeveMade:
		file.write(ruleName+" ")
		for replyID in repliesWeveMade[ruleName]:
			file.write(replyID+" ")
		file.write("\n")
	file.close()

	file = open("placeHolder.txt","w")
	file.write(placeHolder)
	file.close()
	print "Memory sucessfully dumped."

import string
multiReddit = string.join(trackingSubreddits, "+")



# WARNING: TOO META FOR WORK
def implementRule(ruleFunction):
	def implementation(comment,body):
		reply = ruleFunction(comment,body)
		if not reply:
			pass # No rules apply.
		elif comment.submission.id in threadsWeveRepliedTo[listOfRules[ruleFunction]]:
			print "Meta-Rule #1 of Bravery: Never use the same rule twice in one thread."
		else:
			for i in range(22):
				try:
					myReply = reply[1].reply(reply[0]) #DAE reply?
					threadsWeveRepliedTo[listOfRules[ruleFunction]].append(myReply.submission.id)
					repliesWeveMade[listOfRules[ruleFunction]].append(myReply.id)
					print "Successfully commented!", myReply.permalink
					break
				except Exception, ex:
					print "Something went wrong! Try again 22 times.", ex
					time.sleep(30)
	return implementation




user_agent = "Bravery bot 1.0 by /u/SurvivalOfTheBravest"
r = praw.Reddit(user_agent=user_agent)
r.login(username="SurvivalOfTheBravest", password="thisIsntTheRealPassword")
subreddits = r.get_subreddit(multiReddit)

implementedRules = [implementRule(rule) for rule in listOfRules]
startTime = time.time()
while True:
	print "Start loop."
	try:
		comments = subreddits.get_comments(place_holder=placeHolder, limit=500)
		commentsList = [c for c in comments]
		print len(commentsList), "comments!"
		placeHolder = commentsList[0].id
		for comment in commentsList:
			body = comment.body
			for implementedRule in implementedRules:
				implementedRule(comment,body)
	except Exception, ex:
		print "An error occurred:", ex
	dumpMemory()
	print "Sleeping..."
	time.sleep(90)
	currentTime = time.time()
	if currentTime - startTime > 85500:
		print "Timed out after 23:45."
		break
	else:
		print "Moving on..."



# END BRAVE ATHEIST PYTHON MAGIC.

#YOLO
#SWAG
#BRAVE

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
	
	
# WOW, MOTHERFUCKING AND INCEST, DAE?
# This rule brought to you by: /u/garrison0
def everyThread(comment, body):
	lowercaseComment = body.lower()
	if "broken arms" in lowercaseComment or "arms broken" in lowercaseComment:
		return("WOW EVERY THREAD! /r/incest is THAT way xDDD!!", comment)
	return None
	
# WOW, BEASTIALITY TOO? DAE?
# Replies with either a picture of Colby Jack cheese, a dog with Mitt Romney, or a copypasta.
# This rule brought to you by: /u/garrison0
def leColby(comment, body):
	lowercaseComment = body.lower()
	if "COLBY" in body or "Colby" in body or "colby" in lowercaseComment:
		potentialReplies = [
			"http://i.imgur.com/yZbD4.jpg",
			"http://i.imgur.com/Docb6.jpg",
			""" I truly believe I am the most horny person a live. I have done many sexual things
			in the past, have fantasies about, and dream about.*
			Where do I begin?
			When I was 4 years old I would sleep in the same room as my grandma. i would crawl 
			up to her bed and lick and smell her feet. it would take a while for her to wake up, 
			and she would tell me to stop and i would just trollface. i licked her feet it tasted
			like a dampy salt flavour, and she had some calluses and thick feet skin. i guess this
			is how my feet fetish began...
			when i was 4 or 5 years old, i would begin masterbating. i masterbated in the way where 
			you lie face down stomach down on the ground and cup your hands around your genitals and
			rub up your crotch against the ground.*
			so around 4 or 5 im watching jurassic park. the scene of the 2 raptors chasing the 2 kids,
			(1 girl) in the kitchen. i imagined the raptor raping the girl. i guess this is how my
			beastiality fetish began...
			whenever women walk by , i breathe in her to smell her scent.
			in the rare chase i am talking to a woman face to face, when she is speaking i like to 
			breathe in really hard to smell her breathe and remember it.
			i fantasize about an alien world where there is only ONE female and she is like the Queen.
			the thing is though, she is a sex queen and gets dped and throat fcked 24/7 forever. she 
			does not die and she is too well protected in their core of their world.*
			i fantasize about being a girl and just being a sex slave for the pleasure of all men. 
			some example stories are cynthia palmers new life by redlegtiger which you can find on 
			bdsmlibrary. it tells of cynthia palamer, a hot young innnocent girl turned sex slave 
			for anyone and animals. stories tell of her eating our dirty mare ****s, animal gangbangs,
			drinking piss from any animal, or human.
			i fantasize about a hot girl getting abducted by a gang of giant big black silverback
			gorillas and she gets gangbanged in every way possible. dp, doublevag/doubleanal, deepthroat 
			etc. and i imagine the apes kept her as their sex slave and she would give birth since apes 
			and human dna are similar and she gives birth to the planet of the apes.
			when i was 11 or 12, when i first hit puberty, i would get so horny i would masterbate 10+ 
			times a day using my stomach down rub groin method. i would also begin to try to drink pee 
			pretending i am psychologically a woman. i am sad to say, however, i have not been able to 
			swallow. i would be in the shower and i would cup my hand around my dick and pee in it and
			i would slurp it up and hold it in my mouth for around 15 secs savioring the taste. i would 
			try to swallow and fail and either throw up and or gag. i would also get into the position 
			where i have my back and legs up against a wall and i would pee on my own face imagining myself
			as a hot young skanky bitch whore. one time piss got in 1 of my eyes it stung like hell lmao.
			in the cartoon movie osmosis jones, the scene where the guy talks to the hot female teacher 
			the guys pimple burst. i fantasized about the hot teacher licking the burst pimple and licking 
			up all the puss and swallowing it before fcking bill murray.
			i sometimes fantasize about suddenly becoming a woman. as you know, technology is just 
			getting more advanced year by year. very soon they will have a drug that will allow us to
			change genders. i would take this and become a 10/10 dirty blonde eye shadowed g string w
			earing slut. i would fantasize about doing this and becoming a sex slave in a giant 
			organization and i would get fcked and abused everything.
			however this is just a fantasy as of now as the thought of it scares me. i am not in 
			disagreemnt though.
			i have so many more dark fantasies and things ive done ill post some later on. in the 
			mean time, comment and ask questions. i am an aspiring writer in the topic of black sexology.""",
		]
		return(random.choice(potentialReplies), comment)
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
	noWords:"noWords",
	everyThread:"everyThread",
	leColby:"leColby",
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

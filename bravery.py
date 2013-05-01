# -*- coding: utf-8 -*-
import time
import praw
import random


PASSWORD = ""


######################################################################

################## BEGIN BRAVERY RULES.



#### SECTION 1: RULES TO APPLY TO COMMENTS


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

import re
# This rule brought to you by: /u/RollCakeTroll
def noWords(comment,body):
	lowercaseComment = body.lower()
	if "i have no words" in lowercaseComment:
		wordCount = len(re.findall(ur"[\w'’\-]+", body)) #make some shit that counts how many words, named wordCount here #regex by /u/FrenchfagsCantQueue
		return("\"I have no words\"? Sounds like you have at least "+ str(wordCount) + " words.",comment)
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


# This rule brought to you by: /u/flesjewater
def navySealPasta(comment,body):
	lowercaseComment = body.lower()
	if "faggot" in lowercaseComment and "fuck you" in lowercaseComment:
		return(u"What the fuck did you just fucking say about me, you little bitch? I’ll have you know I graduated top of my class in the Navy Seals, and I’ve been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I’m the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You’re fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that’s just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little “clever” comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn’t, you didn’t, and now you’re paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You’re fucking dead, kiddo.",comment)
	return None


# This rule brought to you by: /u/AerateMark
def fuckYouOrFagResp(comment,body):
	lowercaseComment = body.lower()
	if ("faggot" in lowercaseComment) ^ ("fuck you" in lowercaseComment):
		offendedResponse = ['You, sir, are a gentleman and a scholar!', 'So brave.', 'XD', "At least I'm not a nigger."]
		return(random.choice(offendedResponse),comment)
	return None


# Here's some code to reply to people who are complaining about a post in /r/wtf
# being in the wrong subreddit or to join in with them with your own top-level comment.
# This rule brought to you by: /u/Carl_Bravery_Sagan
def notWTF(comment,body):
	#I don't know how to check the current subreddit so you'll have to do this.
	#pseudocode is below
	#if comment not in /r/wtf, return None

	#Also, don't reply to yourself
	#if comment.author == "SurvivalOfTheBravest" return None

	lowercaseComment = body.lower()
	#Check if it contains any of the following:
	triggercomments = [
		"not wtf",
		"isnt wtf",
		"isn't wtf",
		"im14andthisiswtf",
		"mildlyinteresting",
		"wtf material",
		"wtf worthy",
		"r/pics",
		"r/funny",
	]

	for trigger in triggercomments:
		if trigger in lowercaseComment:
			#Now, choose whether to make a top level response or a reply
			#chooser is either 1 or 2
			chooser = random.randint(1,2)
			if chooser == 1:
				#If we hit a trigger, either respond to the comment...
				responses = [
					"This. So much this.",
					"I'm really appalled by the state of this subreddit.",
					"This",
					"I wish I had more than one upRon to give to such a brave comment.",
					"I couldn't agree more, brave sir",
					#I need more comments. I can't think of anything else
				]
				return(random.choice(responses) , comment)
			else:
				#...or make a top level comment
				topLevelResponses = [
					"Quick! Are you on /r/funny, /r/pics, or /r/wtf?",
					"/r/im14andthisisWTF",
					"OP is a faggot. Post in a relevant sub.",
					"I don't think this is really WTF-worthy",
					#Again, I'm running out of comments
				]
				#Only do this if bravery bot hasn't made a top level comment yet. Also, I don't know how to return a top level comment
				return(random.choice(topLevelResponses), comment.submission)

	return None


# Reply to /u/OMG_WhoTheHellCares ironically pointing out that it's talking to a bot.
# But only do it half of the time, so it's not immediately obvious what's going on.
# This rule brought to you by: /u/omgwthc
def omgWhoTheHellCares(comment,body):
	if random.randint(0,1) == 1:
		if body == "http://youtu.be/s0F3LKaGN2A" and str(comment.author) == "OMG_WhoTheHellCares":
			responses = [
				"You're talking to a bot.",
				"Umm... you realize that's a bot, right?",
				"Bots replying to bots? When will it end?",
				"**B O T C E P T I O N**",
				"Do you seriously have nothing better to do than to sit around all day replying to the SRD bot?"
			]
			return(random.choice(responses), comment)
	return None


# This rule brought to you by: /u/FrenchfagsCantQueue
def thats_racist(comment, body):  # srsly, CamelCase for python function names - are you even atheist bro??
	if False and 'black' in body.lower() and len(body) < 200:
		return "What the fuck bro?!, that's racist", comment
	elif "i'm white" in body.lower() and len(body) < 200:  # am I allowed two things? - #YOLO #420-sagan-it
		return ">I'm white\n\nCheck your privilege!!", comment
	else:
		return None


# This rule brought to you by: /u/FrenchfagsCantQueue
def hello_timmie(comment, body):
	if str(comment.author) == 'spoderman_tim':
		return 'Hello spoderman_tim', comment
	return None


# This rule brought to you by: /u/bakedpatato
def EAIsHitler(comment,body):
	lc = body.lower()
	if re.search(r'\bea\b', lc) and ("hate" in lc or "never" in lc or "worst company" in lc or "fuck" in lc): # I can't think of any substrings of "hate or "never" so it should be ok. The first statement is a regex looking for space"ea"space in lc
		return("EA is hit[le]r, amirite?",comment)
	return None


# Here's one for people who have a constant urge to point out their
# rationale for literally anything:
# This rule brought to you by: /u/Carl_Bravery_Sagan
def source(comment, body):
	#lc = body.lower()
	if False: #TODO
		asAResponse = [
			"As a brave sir, I can confirm this.",
			"As a bravard, I can say the same.",
			"As a fellow <take the between 1 and 4 words that were matched in the if statement>, I too can confirm this.",
			"As a brave person, you are brave. Source: Am brave"
		]
		return(random.choice(asAResponse), comment)
	elif random.randint(0,7)==0 and "source:" in body.lower():
		sourceResponse = [
			"I too can confirm this. Source: Am brave",
			"This is a brave comment. Source: Brave",
			"I can confirm what this bravard said. Source: Also brave",
			"As a brave ENTgineer, I can confirm this. #420yoloswag"
		]
		return(random.choice(sourceResponse), comment)
	return None



# Made with the power of Emacs -nox
# Gives those with true Bravery the power to summon SurvivalOfTheBravest
# Regular expression rules via re module can be found at http://docs.python.org/2/library/re.html
# This rule brought to you by: /u/zamnedix
def randomPasta(comment, body):
	loweredBody = body.lower()
	#Pastas, feel free to add to it
	pastas = ["I'm 12 and what is this",
		"In this moment, I am euphoric. Not because of a phony god's blessing, but because, I am enlightened by my own intelligence.",
		"Is this Battletoads?", "Has anyone really been far even as decided to use even go want to do look more like?"
	]

	# Triggers the bot to respond - feel free to add to it
	patterns = ["By the power of Greyskull", "Dawkins", "Neil.Tyson", "aalewis" ]

	for pattern in patterns:
	   #Search comment body case insensitively for each trigger pattern, evaluating regular expressions per Python's re module
	   if re.search(pattern.lower(), loweredBody):
		  #If a MatchObject instance is returned, return with one of the pastas.
		  return (random.choice(pastas), comment)

	# No triggers found, bravery on standby
	return None



# Request bravery: makes post to /r/SurvivalOfTheBravest linking to comment
# containing "!requestbravery" or something. To help brave soldiers in the
# fields of nonbravery.
# This rule brought to you by: /u/Fauxm
def requestBravery( comment, body ):
	if "!requestbravery" in body.lower():
			bravereqName = str( comment.author )
			#I have no idea how to use praw to get the comment permalink, set it to the variable 'commentPerm' or something
			def action():

				r.login(username="SOTB-bot", password=PASSWORD)
				try:
					output = r.submit(
						'SurvivalOfTheBravest',
						'User ' + bravereqName + ' is requesting bravery!',
						url=comment.permalink
					)
				except Exception, ex:
					print "Exception in action requestBravery:", ex
					output = None
				finally:
					r.login(username="SurvivalOfTheBravest", password=PASSWORD)
				return output

			return action
	return None


# A rule for people who need their privilege checked constantly
# This rule brought to you by /u/The_Jakebob
def checkYourPrivilege(comment,body):
	lower = body.lower()
	if "transphobia" in lower or "homophobia" in lower or "feminism" in lower or "feminist" in lower:
			privilegeResp = [
					"Wow, how could you say that?",
					"Check your privilege before saying things like that!",
					"There are starving children in africa and you are concerning yourself with nominal issues like this?",
					"That's rude of you to say, I bet your mother is ashamed.",
					"Show some compassion",
					"I am gay and I find that highly offensive!",
					"DIE CIS SCUM!",
					"JUST BECAUSE YOU ARE CISGENDERED DOESN'T MEAN YOU HAVE TO GO PICKING ON ME"
			]
			return(random.choice(privilegeResp),comment)
	return None



#### SECTION 2: RULES TO APPLY TO SUBMISSIONS



# This rule brought to you by: /u/1cerazor
def n_noHomo(submission, is_self, title, url, selftext):
	if not is_self:
		return None
	else:
		lowercaseText = selftext.lower()
		lowercaseTitle = title.lower()
		if "progress pic" in lowercaseText or "before and after" in lowercaseText or "progress pic" in lowercaseTitle or "before and after" in lowercaseTitle:
			return("Awesome pics. Great size. Look thick. Solid. Tight. Keep us all posted on your continued progress with any new progress pics or vid clips. Show us what you got man. Wanna see how freakin' huge, solid, thick and tight you can get. Thanks for the motivation.", submission)
		else:
			return None




################## END BRAVERY RULES


# BEGIN CONFIGURATION LISTS

listOfRules = {
	oneTrueGod:"oneTrueGod",
	sarahJessicaParker:"sarahJessicaParker",
	murica:"murica",
	anneFrankly:"anneFrankly",
	atheismIsShit:"atheismIsShit",
	noWords:"noWords",
	everyThread:"everyThread",
	#leColby:"leColby",
	navySealPasta:"navySealPasta",
	#fuckYouOrFagResp:"fuckYouOrFagResp"
	notWTF:"notWTF",
	omgWhoTheHellCares:"omgWhoTheHellCares",
	thats_racist:"thats_racist",
	hello_timmie:"hello_timmie",
	EAIsHitler:"EAIsHitler",
	source:"source",
	randomPasta:"randomPasta",
	requestBravery:"requestBravery",
	checkYourPrivilege:"checkYourPrivilege"
}


listOfSubmissionRules = {
	n_noHomo:"n_noHomo",
}

# List of subreddits to check all rules in.
trackingSubreddits = [
	"test",
	"braveryjerk",
	"circlejerk",
	"pics",
	"funny",
	#"politics", #benned
	"gaming",
	"askreddit",
	"videos",
	"iama",
	#"wtf", #benned
	#"aww", #benned
	#"atheism", #benned
	#"AdviceAnimals", #benned
]

# These subreddits will not be checked by any rules EXCEPT those which explicitly
# say so in subredditRestrictions.
specialSubreddits = [
	"fitness",
]

# Every rule listed here will be applied only to comments or submissions in the
# subreddits listed next to it. Rules not listed here will be applied to all
# subreddits in trackingSubreddits.
subredditRestrictions = {
	notWTF:["test","wtf"],
	hello_timmie:["braveryjerk"],
	n_noHomo:["fitness","test"]
}





# END CONFIGURATION LISTS




######################################################################

# BEGIN DARK ATHEIST PYTHON MAGIC


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

placeHolders = {}
file = open("placeHolder.txt")
for line in file.readlines():
	array = line.split()
	ruleName = array[0]
	ph = array[1]
	placeHolders[ruleName] = ph
file.close()


submissionPlaceHolders = {}
file = open("submissionPlaceHolder.txt")
for line in file.readlines():
	array = line.split()
	ruleName = array[0]
	ph = array[1]
	submissionPlaceHolders[ruleName] = ph
file.close()


def dumpMemory():
	global placeHolders
	global submissionPlaceHolders

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
	for ruleName in placeHolders:
		file.write(ruleName+" "+placeHolders[ruleName]+"\n")
	file.close()

	file = open("submissionPlaceHolder.txt","w")
	for ruleName in submissionPlaceHolders:
		file.write(ruleName+" "+submissionPlaceHolders[ruleName]+"\n")
	file.close()

	print "Memory successfully dumped."


delayedComments = []
nextDelayedComments = []

def makeComment(reply, ruleFunction): # Actually makes both comments and submissions.
	if type(reply).__name__ == "function":
		myReply = reply()
	elif type(reply[1]).__name__ == "Submission":
		myReply = reply[1].add_comment(reply[0])
	elif type(reply[1]).__name__ == "Comment": #TODO Is this correct?
		myReply = reply[1].reply(reply[0]) #DAE reply?
	else:
		print "WARNING: UNKNOWN REPLY TYPE! EXCEPTION WILL SOON BE RAISED!"

	if type(myReply).__name__ == "Comment":
		thread = myReply.submission.id
	elif type(myReply).__name__ == "Submission":
		thread = myReply.id
	else:
		raise Exception("Error: myReply is of unknown type: "+type(myReply).__name__)

	if ruleFunction in listOfRules:
		threadsWeveRepliedTo[listOfRules[ruleFunction]].append(thread)
		repliesWeveMade[listOfRules[ruleFunction]].append(myReply.id)
	elif ruleFunction in listOfSubmissionRules:
		threadsWeveRepliedTo[listOfSubmissionRules[ruleFunction]].append(thread)
		repliesWeveMade[listOfSubmissionRules[ruleFunction]].append(myReply.id)
	else:
		print "WARNING: UNKNOWN RULE TYPE!"
	print "Successfully commented!", myReply.permalink



# WARNING: TOO META FOR WORK
def implementRule(ruleFunction):
	def implementation(comment,body):
		reply = ruleFunction(comment,body)
		if not reply:
			pass # No rules apply.
		else:
			threadID = comment.submission.id
			if threadID in threadsWeveRepliedTo[listOfRules[ruleFunction]]:
				print "Meta-Rule #1 of Bravery: Never use the same rule twice in one thread."
			else:
				if delayedComments:
					#There are already comments in the queue. Add this to the end.
					delayedComments.append((reply, ruleFunction, threadID))
					print "Comment has been queued because there are already comments waiting."
				else:
					try:
						makeComment(reply, ruleFunction)
					except Exception, ex:
						if "you are doing that too much. try again in" in str(ex):
							delayedComments.append((reply, ruleFunction, threadID))
							print "Comment has been delayed.", str(ex)
						else:
							print "Something went wrong! We will not try this comment again.", ex
	return implementation


def implementSubmissionRule(ruleFunction):
	def implementation(submission,is_self,title,url,selftext):
		reply = ruleFunction(submission,is_self,title,url,selftext)
		if not reply:
			pass # No rules apply.
		else:
			threadID = submission.id
			if threadID in threadsWeveRepliedTo[listOfSubmissionRules[ruleFunction]]:
				print "Meta-Rule #1 of Bravery: Never use the same rule twice in one thread."
			else:
				if delayedComments:
					#There are already comments in the queue. Add this to the end.
					delayedComments.append((reply, ruleFunction, threadID))
					print "Comment has been queued because there are already comments waiting."
				else:
					try:
						makeComment(reply, ruleFunction)
					except Exception, ex:
						if "you are doing that too much. try again in" in str(ex):
							delayedComments.append((reply, ruleFunction, threadID))
							print "Comment has been delayed.", str(ex)
						else:
							print "Something went wrong! We will not try this comment again.", ex
	return implementation



def checkSubreddit(sr):
	try:
		print "Checking subreddit:", sr
		if sr in placeHolders:
			ph = placeHolders[sr]
		else: ph = None

		if sr == "askreddit": lim = 800
		else: lim = 500

		comments = r.get_subreddit(sr).get_comments(place_holder=ph, limit=lim)
		commentsList = [c for c in comments]
		placeHolders[sr] = commentsList[0].id
		commentsList = commentsList[:-1]
		print len(commentsList), "comments from", sr

		for comment in commentsList:
			body = comment.body
			for (rule,implementedRule) in implementedRules:
				if sr in trackingSubreddits:
					if rule not in subredditRestrictions or sr in subredditRestrictions[rule]:
						implementedRule(comment,body)
				elif sr in specialSubreddits:
					if rule in subredditRestrictions and sr in subredditRestrictions[rule]:
						implementedRule(comment,body)
				else:
					print "WARNING! THIS LINE SHOULD NEVER BE PRINTED!"

	except Exception, ex:
		print "An error occurred:", ex

	dumpMemory()



def checkSubmissions(sr):
	try:
		if sr in submissionPlaceHolders:
			sph = submissionPlaceHolders[sr]
		else:
			sph = None
		submissions = r.get_subreddit(sr).get_new(place_holder=sph,limit=40)
		submissionsList = [s for s in submissions]

		submissionPlaceHolders[sr] = submissionsList[0].id
		submissionsList = submissionsList[:-1]
		print len(submissionsList), "submissions from", sr
		for submission in submissionsList:
			is_self = submission.is_self
			title = submission.title
			url = submission.url
			selftext = submission.selftext
			for (rule,implementedRule) in implementedSubmissionRules:
				if sr in trackingSubreddits:
					if rule not in subredditRestrictions or sr in subredditRestrictions[rule]:
						implementedRule(submission,is_self,title,url,selftext)
				elif sr in specialSubreddits:
					if rule in subredditRestrictions and sr in subredditRestrictions[rule]:
						implementedRule(submission,is_self,title,url,selftext)
				else:
					print "WARNING! THIS LINE SHOULD NEVER BE PRINTED!"

	except Exception, ex:
		print "An error occurred:", ex

	dumpMemory()




user_agent = "Bravery bot 1.0 by /u/SurvivalOfTheBravest"
r = praw.Reddit(user_agent=user_agent)
r.login(username="SurvivalOfTheBravest", password=PASSWORD)


implementedRules =           [(rule,implementRule(rule))           for rule in listOfRules]
implementedSubmissionRules = [(rule,implementSubmissionRule(rule)) for rule in listOfSubmissionRules]
startTime = time.time()
while True:
	print "Start loop."
	delayedComments = nextDelayedComments
	nextDelayedComments = []

	print "Checking comments:"
	for sr in trackingSubreddits:
		checkSubreddit(sr)
	for sr in specialSubreddits:
		checkSubreddit(sr)

	print "Checking submissions:"
	# This shouldn't really be like this, but it is because the only rule
	# checking submissions is restricted to /r/fitness.
	for sr in ["test"]: #trackingSubreddits:
		checkSubmissions(sr)
	for sr in specialSubreddits:
		checkSubmissions(sr)


	print "Done with every subreddit."

	if delayedComments:
		print "We will now attempt to make the", len(delayedComments), "delayed comments."
		for (reply, ruleFunction, threadID) in delayedComments:
			if threadID in threadsWeveRepliedTo[listOfRules[ruleFunction] if (ruleFunction in listOfRules) else listOfSubmissionRules[ruleFunction]]:
				print "Meta-Rule #1 of Bravery: Never use the same rule twice in one thread."
			else:
				try:
					makeComment(reply, ruleFunction)
				except Exception, ex:
					if "you are doing that too much. try again in" in str(ex):
						nextDelayedComments.append((reply, ruleFunction, threadID))
						print "We still couldn't post the comment. Deferred to the next round.", str(ex)
					else:
						print "Something went wrong! We will not try the comment again.", ex
		dumpMemory()
		print "Finished with the delayed comments."
	else:
		print "No delayed comments."
	print "Sleeping..."
	time.sleep(60)
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

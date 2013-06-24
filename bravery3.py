# -*- coding: utf-8 -*-
import time
import praw
import random
import string
import re
from collections import deque


from password import PASSWORD


USERNAME = "Neil_Dat_grAss_Tyson"


######################################################################
####################### BEGIN BRAVERY RULES. #########################





#### SECTION 1: RULES TO APPLY TO COMMENTS


## ROUND 1 RULES ##


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



# Here's some code to reply to people who are complaining about a post in /r/wtf
# being in the wrong subreddit or to join in with them with your own top-level comment.
# This rule brought to you by: /u/Carl_Bravery_Sagan
def notWTF(comment,body):
	if random.randint(0,3) != 1: return None
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
			#make a top level comment
			topLevelResponses = [
				"Quick! Are you on /r/funny, /r/pics, or /r/wtf?",
				"/r/im14andthisisWTF",
				"OP is a faggot. Post in a relevant sub.",
				"I don't think this is really WTF-worthy",
				#Again, I'm running out of comments
			]
			return(random.choice(topLevelResponses), comment.submission)

	return None



# This rule brought to you by: /u/FrenchfagsCantQueue
def hello_timmie(comment, body):
	if str(comment.author) == 'spoderman_tim':
		comment.upvote()
		return 'Hello spoderman_tim', comment
	return None


# This rule brought to you by: /u/RainbowDashIsEpic
def breadsticks(comment, body):
	lc = body.lower()
	if "olive garden" in lc or "breadsticks" in lc or "unlimited breadsticks" in lc or "infinite breadsticks" in lc or "breadstick" in lc:
		return("/r/unlimitedbreadsticks", comment)
	return None


# This rule brought to you by: /u/feblehober123
def penisEnlargementPill(comment,body):
	lowercaseComment = body.lower()
	if "reddit enhancement suite reddit enhancement suite" in lowercaseComment:
		pep = string.join(["penis enlargement pill" for x in re.finditer("reddit enhancement suite",lowercaseComment)]," ")
		return(pep, comment)
	return None


# This rule brought to you by: /u/garrison0
def Hello(comment, body):
	lc = body.lower()
	if "hello spoderman_tim" in lc:
		author = str(comment.author)
		if author != USERNAME:
			return ("Hello " + author, comment)
	return None




# Detect if someone appears to be losing an argument,
# and get ourselves on the winning side.
# This rule brought to you by: /u/SOTB-human
def winningArgument(comment, body):
	lc = body.lower()
	if len(lc)>50 and ("ad hominem" in lc or "i never said" in lc or "what makes you think" in lc or "personal attack" in lc):
		try: #Get the parent comment.
			threadID = comment.submission.id
			parent = praw.objects.Submission.from_url(r, "http://www.reddit.com/r/all/comments/"+threadID+"/_/"+comment.parent_id[3:]).comments[0]
		except:
			return None
		if parent.score > 2: #If the parent is upvoted,
			try: #Get the grandparent comment.
				grandparent = praw.objects.Submission.from_url(r, "http://www.reddit.com/r/all/comments/"+threadID+"/_/"+parent.parent_id[3:]).comments[0]
			except:
				return None
			#If the grandparent has been downvoted and is by the same person,
			if grandparent.score < 0 and comment.author == grandparent.author:
				if random.randint(0,2) == 0: #Reply to the comment with disagreement
					if "ad hominem" in lc:
						responses = [
							">ad hominem\n\nI don't think that means what you think it means.",
							"A simple expression of disagreement doesn't count as *ad hominem*.",
							"I think that /u/"+str(parent.author)+" makes a valid point. Why do you think it's an *ad hominem*?",
						]
					else:
						responses = [
							"someone sounds butthurt",
							"the butthurt store called, they're running out of /u/"+str(comment.author),
							"Why are you even arguing about this?",
							"http://xkcd.com/386/",
							"The fact that people still think like this makes me sad.",
							"Dude, seriously. Give it a rest."
						]
					return (random.choice(responses), comment)
				else: #Or, reply to the parent with agreement.
					responses = [
						"I can't believe that anyone would be so naive as to disagree with this.",
						"Haters gonna hate. Don't waste your time arguing with trolls.",
						"Yours is a much needed voice of reason.",
						"I wish more people were as reasonable as you.",
						"Thank you for bringing some sanity to this discussion."
					]
					return (random.choice(responses), parent)
	return None


# This rule brought to you by: /u/garrison0
def leSexual(comment, body):
	lowercaseComment = body.lower()
	if "colby" in lowercaseComment:
		potentialReplies = [
			"http://i.imgur.com/yZbD4.jpg",
			"http://i.imgur.com/Docb6.jpg",
			"*shrug*\n\nEvery thread.",
			"[For all those wondering...](http://www.reddit.com/r/AskReddit/comments/zw3j9/i_am_the_fatherredditor_who_lost_his_family_after/)",
			"Keep your hairbrush away from your kids.",
			"http://i.imgur.com/MYKti.png",
			"I wonder what happened to that guy..",
			"Does anyone know what happened to that guy?",
			"Poor Colby."
		]
		return(random.choice(potentialReplies), comment)
	if len(body) < 200 and ("broken arms" in lowercaseComment or "arms broken" in lowercaseComment):
		potentialReplies = [
			"Every fucking thread.",
			"Was anyone else on Reddit a year ago?",
			"/r/incest is that way, mate.",
			"Great, just the mental image I needed today.",
			"Colby, incest, mothers, broken arms, etc.",
			"You know what they say, your mother is always there for you.",
			"Thanks, mom.",
			"Well, I liked the sisterfucker better.",
			"[For those who are wondering..](http://www.reddit.com/r/IAmA/comments/nmmjr/iama_man_who_had_a_sexual_relationship_with_his/)"
		]
		return(random.choice(potentialReplies), comment)
	return None





# [Le]terally misandry
# This rule brought to you by: /u/braveathee
def ilovemales(comment, body):
	if "As a male" in body:
		author = str(comment.author)
		replies = [
			">As a male \n \n Has anybody checked if " + author + " had posted anything in /r/gonewild ?",
			">As a male \n \n I have checked, nothing in /r/gonewild. :(",
			">As a male \n \n I have found nothing in /r/gonewild. :(",
			">As a male \n \n *Looks at " + author + "'s history* \n \n ... \n \n Nothing in /r/ladyboners. :(",
			">As a male \n \n *Checks " + author + "'s history* \n \n ... \n \n Nothing in /r/gonewild. :-(",
			">As a male \n \n *Looks at " + author + "'s history on redditgraphs* \n \n ... \n \n No pics in /r/LadyBoners or /r/gonewild. :(",
			">As a male \n \n *Searches " + author + "'s history* \n \n ... \n \n No posts in /r/ladyboners. :-(",
		]
		return (random.choice(replies), comment)
	return None






# this rule is brought to you by /u/xvvhiteboy
def middleschool(comment, body):
	lc = body.lower()
	if "r/imgoingtohellforthis" in lc:
		return("[/r/imgoingtomiddleschoolforthis](/r/igtmsft)", comment)
	return None

# this rule is brought to you by /u/xvvhiteboy
def sofuckingedgy(comment, body):
	lc = body.lower()
	if "2egdy4me" in lc or "3edgy5me" in lc:
		return("69edgy420me", comment)
	return None


# This rule brought to you by: /u/hive_worker
# Restrict to /r/politics
def republicansAreEvil(comment, body):
	if random.randint(0,2) != 1:
		return None  #lets throttle this back to begin with to prevent benning in /r/politics
	lc = body.lower()
	triggerString = [
		"Sarah Palin",
		"Rand Paul",
		"Mitt Romney",
		"Ronald Reagan",
		"Jim Demint",
		"George Bush",
		"Paul Ryan",
		"Rubio"
	]
	for trigger in triggerString:
		if trigger.lower() in lc:
			responses = [
				"I hate Republicans. I loathe them. I hate people who support them. I hate people who even tolerate them. They are bringing America back to the dark ages with their hatred of all things non-white male.",
				trigger + " is a plague on society. Sure he might be great if you are a rich, heterosexual, white male, but for the rest of us he is nothing but a cancer. True progressives need to unite against " + trigger + ".",
				"Yet another ignorant tea bagger. I'd love to hear what " + trigger + " says about black people in private.",
				"Just watch, they'll find a way to rig the election again in 2016 and some how " + trigger + " will win. There is no way they will allow a progressive to win again after all the damage Barack Obama has done to the white-centric patriarical plutocracy.",
				"Righties and Republicans reading this, if you've gotten this far meybe you can figure out what made me this way. But don't ever look at someone like me and think we have no right for this feeling toward you. Don't ever think you or your heroes are innocent. ",
				"Have you ever actually looked at " + trigger+ "'s tax returns or campaign finance report? Really an eye opener.",
				"Do you know who " + trigger + "'s biggest donnor is? I'll give you three guesses...",
				"Please, I implore everyone reading this to go actually research the early writings of " + trigger + ". It's important to know the true evil we are dealing with here."
			]
			return (random.choice(responses), comment)
	return None
	
#This rule brought to you by /u/Wall_Dough
#Quotation of Tom Jones's "It's Not Unusual", which itself is not unusual
#If the trigger is found, the comment has a 1/3 chance of occurring
def itsNotUnusual(comment, body):
    lc = body.lower()
    lc = lc.replace("'","")
    if "its not unusual" in lc and not "loved by anyone" in lc:
        if random.randint(0,2) == 2:
            return ("*It's not unusual to be loved by anyone*", comment)
    return None


# Helper function:
# Suspend all processes for 21 minutes or until
# the comment is successfully posted. If it is,
# return it. If it isn't, return None.
# Use this function sparingly.
def forceComment(text, thingToReplyTo):
	for i in range(21):
		try:
			if type(thingToReplyTo).__name__ == "Comment":
				result = thingToReplyTo.reply(text)
			elif type(thingToReplyTo).__name__ == "Submission":
				result = thingToReplyTo.add_comment(text)
			else:
				print "Error in forceComment: thingToReplyTo is of an unrecognized type"
				return None
			print "Successfully forced comment:", result.permalink
			return result
		except Exception, e:
			print "Error in forceComment. Trying again in 60 seconds:", e
			time.sleep(60)
	print "After 21 minutes we still couldn't force the comment. Giving up."
	return None



# Restrict to @ORANGERED
# Bypasses meta-rules, because it doesn't actually make any comments.
def botLogic(comment, body):
	lc = body.lower()
	if " bot " in lc or " bot?" in lc or " bot," in lc or " bot." in lc or " bot!" in lc or "bot logic" in lc or "automated" in lc:
		accuser = str(comment.author)
		if accuser != USERNAME:
			for tailID in botConversations:
				if botConversations[tailID] and accuser in botConversations[tailID]:
					#This may be a little too strict.
					print "Bot accuser is already participating in a conversation elsewhere."
					return None
			print "Bot accusation detected. Initiate a conversation at the next opportunity."
			botAccusations.append((comment,body))
	return None


# Set a very low initial throttling factor so that this
# takes one or two rounds to be invoked.
def botConversationInitiator(comment,body):
	if (False or random.randint(0,1000) == 1) and botAccusations:
		(c,b) = botAccusations[0]
		# Don't initiate the conversation in the same thread,
		# and don't do it to ourselves (which would be really bad).
		# Also, don't do it to the same person who made the accusation.
		tailAuthor = str(comment.author)
		headAuthor = str(c.author) #The username of the accuser.
		if c.submission != comment.submission and tailAuthor!=USERNAME and tailAuthor!=headAuthor:
			successfulComment = forceComment(b,comment)
			if successfulComment:
				botConversations[successfulComment.id] = [tailAuthor, c, headAuthor]
				dumpBotConversations()
				botAccusations.popleft()
	return None



# Restrict to @ORANGERED
# If someone replies to a bot accusation conversation, continue the conversation.
# This rule bypasses the normal comment regulators.
def botConversationListener(comment,body):
	tailID = comment.parent_id[3:]
	if tailID in botConversations:
		#Someone just replied to our end of the bot conversation!
		information = botConversations[tailID]
		tailAuthor = information[0]
		headComment = information[1]
		headAuthor = information[2]
		thisCommentAuthor = str(comment.author)
		if thisCommentAuthor == tailAuthor:
			successfulComment = forceComment(body, headComment)
			if successfulComment:
				botConversations[tailID] = None
				botConversations[successfulComment.id] = [headAuthor,comment,thisCommentAuthor]
				dumpBotConversations()
		else:
			print "this isn't part of the bot conversation because it's not by the same person."
	return None



bjClipboard = ""

def bjCopyPaste(comment, body):
	if random.randint(0,12)==1:
		if bjClipboard == "":
			#Get a new copypaste.
			bjClipboard = body
			print "Copied Braveryjerk comment for later use"
			return None
		else:
			#Release the copypaste.
			response = bjClipboard
			bjClipboard = ""
			return (response, comment)
	return None




#### SECTION 2: RULES TO APPLY TO SUBMISSIONS


# None as yet






######################## END BRAVERY RULES. ##########################
######################################################################






######################################################################
##################### BEGIN CONFIGURATION LISTS ######################


listOfCommentRules = { #Rules to apply to comments.
	notWTF:"notWTF",
	oneTrueGod:"oneTrueGod",
	sarahJessicaParker:"sarahJessicaParker",
	#murica:"murica",
	hello_timmie:"hello_timmie",
	breadsticks:"breadsticks",
	penisEnlargementPill:"penisEnlargementPill",
	Hello:"Hello",
	winningArgument:"winningArgument",
	leSexual:"leSexual",
	ilovemales:"ilovemales",
	middleschool:"middleschool",
	sofuckingedgy:"sofuckingedgy",
	republicansAreEvil:"republicansAreEvil",
	botConversationInitiator:"botConversationInitiator",
	botLogic:"botLogic",
	botConversationListener:"botConversationListener",
	bjCopyPaste:"bjCopyPaste",
}


listOfSubmissionRules = { #Rules to apply to submissions.
	#empty so far
}


# List of subreddits to check all rules in.
trackingSubreddits = [
	"pics",
	"funny",
	"politics",
	"gaming",
	"askreddit",
	"videos",
	"iama",
	"wtf",
	"aww",
	"atheism",
	"AdviceAnimals",
	"todayilearned",
	"circlejerk",
	"magicskyfairy",
	"atheismrebooted",
	"Braveryjerk",
	"SOTBMeta",
	"test",
]

# These subreddits will not be checked by any rules EXCEPT those which explicitly
# say so in subredditRestrictions.
# "@ORANGERED" is a pseudo-subreddit that represents the feed of replies to our own comments.
specialSubreddits = [
	"@ORANGERED"
]

# Every rule listed here will be applied only to comments or submissions in the
# subreddits listed next to it. Rules not listed here will be applied to all
# subreddits in trackingSubreddits.
subredditRestrictions = {
	republicansAreEvil:["test","politics"],
	notWTF:["test","wtf"],
	hello_timmie:["Braveryjerk"],
	botLogic:["@ORANGERED"],
	botConversationListener:["@ORANGERED"],
	bjCopyPaste:["Braveryjerk"],
}



###################### END CONFIGURATION LISTS #######################
######################################################################






######################################################################
################## BEGIN DARK ATHEIST PYTHON MAGIC ###################


def loadDictionary(fileName, format):
	output = {}
	file = open(fileName)
	for line in file.readlines():
		array = line.split()
		k = array[0]
		if format == "string":
			value = array[1]
		elif format == "list":
			value = array[1:]
		elif format == "float":
			value = float(array[1])
		output[k] = value
	file.close()
	return output

#This should always be wrapped in try/except, in case the comment was deleted or something.
def getCommentFromToken(r, token):
	splitToken = token.split("#")
	threadID = splitToken[0]
	commentID = splitToken[1]
	return praw.objects.Submission.from_url(r, "http://www.reddit.com/r/all/comments/"+threadID+"/_/"+commentID).comments[0]

def loadBotConversations():
	output = {}
	file = open("botConversations.txt")
	for line in file.readlines():
		array = line.split()
		tailID = array[0]
		try:
			headComment = getCommentFromToken(r, array[2])
		except:
			print "Couldn't load botConversation", array
			continue
		tailAuthor = array[1]
		headAuthor = array[3]
		output[tailID] = [tailAuthor, headComment, headAuthor]
	return output

def dumpBotConversations():
	file = open("botConversations.txt","w")
	file.write("")
	file.close()
	file = open("botConversations.txt","a")
	for tailID in botConversations:
		if botConversations[tailID]:
			array = botConversations[tailID]
			file.write(tailID + " " + array[0] + " " + array[1].submission.id + "#" + array[1].id + " " + array[2]+"\n")
	file.close()
	print "botConversations successfully dumped."


threadsWeveRepliedTo = loadDictionary("threads.txt", "list")
repliesWeveMade      = loadDictionary("replies.txt", "list")
commentPlaceholders  = loadDictionary("commentPlaceholders.txt", "string")
submissionPlaceholders=loadDictionary("submissionPlaceholders.txt", "string")
throttlingFactors    = loadDictionary("throttlingFactors.txt", "float")




for rule in listOfCommentRules:
	ruleName = listOfCommentRules[rule]
	if ruleName not in throttlingFactors: throttlingFactors[ruleName] = 1
for rule in listOfSubmissionRules:
	ruleName = listOfSubmissionRules[rule]
	if ruleName not in throttlingFactors: throttlingFactors[ruleName] = 1


feederPlaceholder = ""
file = open("feederPlaceholder.txt")
feederPlaceholder = file.readlines()[0]
file.close()


feederThreadsWeveAnswered = []
feederRepliesWeveMade = []
file = open("feederHistory.txt")
lines = file.readlines()
feederThreadsWeveAnswered = lines[0].split()
feederRepliesWeveMade = lines[1].split()
file.close()



def dumpDictionary(dictionary, fileName, format):
	file = open(fileName,"w")
	file.write("")
	file.close()
	file = open(fileName,"a")
	for k in dictionary:
		file.write(k+" ")
		if format == "list":
			for li in dictionary[k]:
				file.write(li+" ")
		elif format == "string":
			file.write(str(dictionary[k]))
		file.write("\n")
	file.close()


def dumpMemory():
	#global placeHolders
	#global submissionPlaceHolders
	#global feederPlaceHolder
	dumpDictionary(threadsWeveRepliedTo, "threads.txt", "list")
	dumpDictionary(repliesWeveMade, "replies.txt", "list")
	dumpDictionary(commentPlaceholders, "commentPlaceholders.txt", "string")
	dumpDictionary(submissionPlaceholders, "submissionPlaceholders.txt", "string")

	file = open("feederPlaceholder.txt","w")
	file.write(feederPlaceholder)
	file.close()

	file = open("feederHistory.txt","w")
	file.write(string.join(feederThreadsWeveAnswered," "))
	file.write("\n")
	file.write(string.join(feederRepliesWeveMade," "))
	file.close()

	print "Memory successfully dumped."


def dumpThrottlingFactors():
	dumpDictionary(throttlingFactors, "throttlingFactors.txt", "string")
	print "Throttling factors successfully dumped."



delayedComments = []
nextDelayedComments = []

deletionQueue = deque([])
botAccusations = deque([])



def nameOfRule(ruleFunction):
	if ruleFunction in listOfCommentRules:
		return listOfCommentRules[ruleFunction]
	elif ruleFunction in listOfSubmissionRules:
		return listOfSubmissionRules[ruleFunction]
	else:
		print "WARNING: UNKNOWN RULE TYPE!"
		return None





def makeComment(reply, ruleFunction): # Actually makes both comments and submissions.
	if type(reply).__name__ == "function":
		myReply = reply()
	elif type(reply[1]).__name__ == "Submission":
		myReply = reply[1].add_comment(reply[0])
	elif type(reply[1]).__name__ == "Comment":
		myReply = reply[1].reply(reply[0]) #DAE reply?
	else:
		print "WARNING: UNKNOWN REPLY TYPE! EXCEPTION WILL SOON BE RAISED!"

	if type(myReply).__name__ == "Comment":
		thread = myReply.submission.id
		deletionQueue.append(myReply)
		#We will check this some number of comments later, and delete it if it gets too many downvotes.
	elif type(myReply).__name__ == "Submission":
		thread = myReply.id
	else:
		raise Exception("Error: myReply is of unknown type: "+type(myReply).__name__)

	n = nameOfRule(ruleFunction)
	threadsWeveRepliedTo[n].append(thread)
	repliesWeveMade[n].append(thread+"#"+myReply.id)

	print "Successfully commented!", myReply.permalink



def attemptComment(reply, ruleFunction, threadID, delaying=False):
	if threadID in threadsWeveRepliedTo[nameOfRule(ruleFunction)]:
		print "Meta-Rule #1 of Bravery: Never use the same rule twice in one thread."
	elif type(reply).__name__=="tuple" and len(reply)==2 and str(reply[1].author)==USERNAME:
		print "Meta-Rule #2 of Bravery: Never reply to yourself."
	else:
		if not delaying and delayedComments:
			#There are already comments in the queue. Add this to the end.
			delayedComments.append((reply, ruleFunction, threadID))
			print "Comment has been queued because there are already comments waiting."
		else:
			try:
				makeComment(reply, ruleFunction)
			except Exception, ex:
				if "you are doing that too much. try again in" in str(ex):
					if delaying:
						nextDelayedComments.append((reply, ruleFunction, threadID))
						print "We still couldn't post the comment. Deferred to the next round.", str(ex)
					else:
						delayedComments.append((reply, ruleFunction, threadID))
						print "Comment has been delayed.", str(ex)
				else:
					print "Something went wrong! We will not try this comment again.", ex




# WARNING: TOO META FOR WORK
def implementRule(ruleFunction, isCommentTracker):
	def implementImplementation(comment=None,
								body=None,
								submission=None,
								is_self=None,
								title=None,
								url=None,
								selftext=None):
		if isCommentTracker:
			reply = ruleFunction(comment,body) #or
		else:
			reply = ruleFunction(submission,is_self,title,url,selftext)
		if not reply:
			pass # No rules apply.
		else:
			if isCommentTracker:
				threadID = comment.submission.id #or
			else:
				threadID = submission.id
			attemptComment(reply, ruleFunction, threadID)

	if isCommentTracker:
		def implementation(comment,body):
			implementImplementation(comment,body)
	else:
		def implementation(submission,is_self,title,url,selftext):
			implementImplementation(None,None,submission,is_self,title,url,selftext)
	return implementation



def checkSubreddit(sr, isCommentTracker):
	try:
		noun = ("comments" if isCommentTracker else "submissions")
		print "Checking subreddit for", noun, ":", sr
		applicablePlaceholders = commentPlaceholders if isCommentTracker else submissionPlaceholders

		if sr in applicablePlaceholders:
			ph = applicablePlaceholders[sr]
		else:
			ph = None

		if sr == "@ORANGERED":
			#print "Getting orangereds"
			posts = r.get_inbox()
			postsList = []
			i = 0
			for x in posts:
				i+=1
				if type(x).__name__ == "Comment":
					postsList.append(x)
				if i>10 or x.id == ph:
					break
		else:
			subreddit = r.get_subreddit(sr)
			if isCommentTracker:
				if sr == "askreddit":
					lim = 800
				else:
					lim = 500
				posts = subreddit.get_comments(place_holder=ph, limit=lim)
			else:
				posts = subreddit.get_new(place_holder=ph,limit=40)
			postsList = [x for x in posts]

		if not postsList:
			print "Nothing."
			dumpMemory()
			return

		applicablePlaceholders[sr] = postsList[0].id
		postsList = postsList[:-1]
		print len(postsList), noun, "from", sr

		for post in postsList:
			if isCommentTracker:
				comment = post
				body = comment.body
			else:
				submission = post
				is_self = submission.is_self
				title = submission.title
				url = submission.url
				selftext = submission.selftext

			for (rule, implementedRule) in (implementedCommentRules if isCommentTracker else implementedSubmissionRules):
				if( (sr in trackingSubreddits) and \
				    (rule not in subredditRestrictions or sr in subredditRestrictions[rule]) ) or \
				  ( (sr in specialSubreddits) and \
				  	(rule in subredditRestrictions and sr in subredditRestrictions[rule])
				  	):
				 	if (random.random() <= throttlingFactors[nameOfRule(rule)]):
				 		if isCommentTracker:
							implementedRule(comment,body)
						else:
							implementedRule(submission,is_self,title,url,selftext)

	except Exception, ex:
		print "An error occurred:", ex

	dumpMemory()



def is_comment(url):
	url_suffix = url[url.index("reddit.com/r/")+13:]
	slashed = url_suffix.split("/")
	if len(slashed) >= 5 and slashed[4] != "":
		return True
	else:
		return False

def processFeeder(submission):
	callbackText = "Mysterious error. Something went seriously wrong if you see this."
	title = submission.title
	feederThreadID = submission.id
	if not submission.is_self:
		print "Feeder post is not a self-post. Do nothing."
	elif feederThreadID in feederThreadsWeveAnswered:
		print "We've already answered this, but for some reason we're looking at it again."
	elif title[:4] == "http":
		try:
			url = title
			try:
				linked_thing = praw.objects.Submission.from_url(r, url)
			except:
				raise Exception("Couldn't parse your title. Please ensure that the title of your post is the URL of a Reddit comment thread or comment permalink, and try again.")

			iscomment = is_comment(url)
			if iscomment:
				linked_thing = linked_thing.comments[0]

			selftext = submission.selftext
			if not selftext:
				raise Exception("You must enter something for the self-text. Please try again.")
			else:
				#if iscomment: x = linked_thing.reply(selftext)
				#else: x = linked_thing.add_comment(selftext)
				x = forceComment(selftext, linked_thing)
				if not x:
					raise Exception("Error in commenting. Please try again.")
				permalink = x.permalink
				identifyingToken = x.submission.id + "#" + x.id
				feederThreadsWeveAnswered.append(feederThreadID)
				feederRepliesWeveMade.append(identifyingToken)
				innerText = random.choice([
					"Here you go, brave sir/madam",
					"Literally This",
					"SO BRAVE",
					"I have LITERALLY posted this",
				])
				callbackText = "["+innerText+"]("+permalink+")"
		except Exception, ex:
			callbackText = "Error: " + str(ex)

		try:
			y = submission.add_comment(callbackText)
			print "Posted callback:", y.permalink
		except Exception, ex:
			print "Error in posting callback. User's out of luck; there's nothing else we can do.", ex
	else:
		print "Not an http self-post."




def splitArrayByElement(array, splitter):
	output = []
	current = []
	for element in array:
		if element == splitter:
			output.append(current)
			current = []
		else:
			current.append(element)
	output.append(current)
	return output


r = praw.Reddit(user_agent="Bravery bot 3.0 by /u/"+USERNAME)
r.login(username=USERNAME, password=PASSWORD)

rBot = praw.Reddit(user_agent="Bravery bot 3.0 utility handler by /u/SOTB-bot")
rBot.login(username="SOTB-bot", password=PASSWORD)

botConversations = loadBotConversations()


# Before we start, update the throttlingFactors based on the karma totals,
# not from the previous day, but from the day before that.
"""
INCREMENT = 0.8

print "Updating throttling factors based on yesterday's karma."
for ruleName in repliesWeveMade:
	print "Assessing", ruleName
	splitList = splitArrayByElement(repliesWeveMade[ruleName], "$")
	if len(splitList) >=2:
		yesterday = splitList[-2]
	else:
		yesterday = []
	karma = 0
	for ids in yesterday:
		arr = ids.split("#")
		threadID = arr[0]
		commentID = arr[1]
		url = "http://www.reddit.com/r/all/comments/"+threadID+"/_/"+commentID
		try:
			commentTree = praw.objects.Submission.from_url(r, url).comments
			if commentTree:
				comment = commentTree[0]
				score = int(comment.score)-1
				print "A score of", str(score), "at", url
				karma += score
			else:
				print "Comment has been deleted:", url
		except Exception, ex:
			print "Exception in getting comment. Assume 0.", ex
		#print "Adding entry:", entry
	print ruleName, "has gotten", str(karma), "karma."
	if karma > 0:
		throttlingFactors[ruleName] = min(1.0, throttlingFactors[ruleName]/INCREMENT)
	elif karma < 0:
		throttlingFactors[ruleName] = max(0.0, throttlingFactors[ruleName]*INCREMENT)

print "Done adjusting throttlingFactors."
dumpThrottlingFactors()

# Add "$" to the end of each repliesWeveMade list to mark the beginning of a new day.
for ruleName in repliesWeveMade:
	repliesWeveMade[ruleName].append("$")
dumpMemory()
#"""

#Get ready...
implementedCommentRules    = [(rule,implementRule(rule,True))  for rule in listOfCommentRules]
implementedSubmissionRules = [(rule,implementRule(rule,False)) for rule in listOfSubmissionRules]
startTime = time.time()

#Go!
while True:
	print "Start loop."

	try:
		feeder = rBot.get_subreddit("SurvivalOfTheBravest")
		posts = feeder.get_new(place_holder=feederPlaceholder,limit=40)
		postsList = [s for s in posts]

		feederPlaceholder = postsList[0].id
		postsList = postsList[:-1]
		postsList.reverse()

		print "Got " + str(len(postsList)) + " posts from the feeder."

		for post in postsList:
			processFeeder(post)

		print "Done with feeder."
	except Exception, ex:
		print "An exception occurred while processing the feeder:", ex
	dumpMemory()



	delayedComments = nextDelayedComments
	nextDelayedComments = []

	print "Checking comments:"
	for sr in trackingSubreddits:
		checkSubreddit(sr, True)
	for sr in specialSubreddits:
		checkSubreddit(sr, True)

	#Don't do this, because we don't have any submission rules.
	"""
	print "Checking submissions:"
	for sr in trackingSubreddits:
		checkSubmissions(sr, False)
	for sr in specialSubreddits:
		checkSubmissions(sr, False)
	"""

	print "Done with every subreddit."


	if delayedComments:
		print "We will now attempt to make the", len(delayedComments), "delayed comments."
		for (reply, ruleFunction, threadID) in delayedComments:
			attemptComment(reply, ruleFunction, threadID, delaying=True)
		dumpMemory()
		print "Finished with the delayed comments."
	else:
		print "No delayed comments."

	print "Done applying rules."

	print "Checking for comments to delete."

	while len(deletionQueue) > 12:
		myComment = deletionQueue.popleft()
		if myComment.score < -1:
			print "Deleting comment:", myComment.permalink
			myComment.delete()
			#lel, 2brave4u
			#myComment.edit(myComment.body + "\n\nEDIT: Downvotes? Seriously?")
		else:
			print "We won't delete that comment."
	print "Done deleting comments."

	print "Sleeping..."
	time.sleep(80)

	#Are we done for the day?
	currentTime = time.time()
	if currentTime - startTime > 85500:
		print "Timed out after 23:45."
		break
	else:
		print "Moving on..."




################### END DARK ATHEIST PYTHON MAGIC ####################
######################################################################


#YOLO
#SWAG
#BRAVE

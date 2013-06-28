# -*- coding: utf-8 -*-
import time
import praw
import random
import string
import re
from collections import deque
import sys


from password import PASSWORD


USERNAME = "SEE_ME_EVERYWHERE"


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
	if random.randint(0,3) != 0: return None
	lowercaseComment = body.lower()
	if "MURICA" in body or "AMERICA" in body or " america!" in lowercaseComment:
		if "r/murica" not in lowercaseComment:
			return ("/r/MURICA", comment)
	return None



# Here's some code to reply to people who are complaining about a post in /r/wtf
# being in the wrong subreddit or to join in with them with your own top-level comment.
# This rule brought to you by: /u/Carl_Bravery_Sagan
def notWTF(comment,body):
	if random.randint(0,8) != 1: return None
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
		#"r/pics",
		#"r/funny",
	]

	for trigger in triggercomments:
		if trigger in lowercaseComment:
			#make a top level comment
			topLevelResponses = [
				"Quick! Are you on /r/funny, /r/pics, or /r/wtf?",
				"/r/im14andthisisWTF",
				"OP is a faggot. Post in a relevant sub.",
				"I don't think this is really WTF-worthy",
				"Why is this is in /r/wtf?"
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


# Helper function:
# Suspend all processes for 21 minutes or until
# the comment is successfully posted. If it is,
# return it. If it isn't, return None.
# Use this function sparingly.
def forceComment(text, thingToReplyTo, registration="!UNKNOWN"):
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
			submissionID = result.submission.id
			commentID = result.id
			token = submissionID + "#" + commentID
			if registration in threadsWeveRepliedTo:
				threadsWeveRepliedTo[registration].append(submissionID)
			else:
				threadsWeveRepliedTo[registration] = [submissionID]
			if registration in repliesWeveMade:
				repliesWeveMade[registration].append(token)
			else:
				repliesWeveMade[registration] = [token]
			return result
		except Exception, e:
			if "Forbidden" in str(e):
				print "Unforceable error:", e
				return None
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
			successfulComment = forceComment(b,comment,"botConversationInitiator")
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
			successfulComment = forceComment(body, headComment, "botConversationListener")
			if successfulComment:
				botConversations[tailID] = None
				botConversations[successfulComment.id] = [headAuthor,comment,thisCommentAuthor]
				dumpBotConversations()
		else:
			print "this isn't part of the bot conversation because it's not by the same person."
	return None



bjClipboard = ""
#This rule brought to you by: /u/SOTB-human
def bjCopyPaste(comment, body):
	global bjClipboard
	if random.randint(0,5)==1:
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


# helper function
def ruleResponsibleForCommentWithID(commentID):
	for ruleName in repliesWeveMade:
		replies = repliesWeveMade[ruleName]
		for rep in replies:
			if commentID in rep:
				return ruleName
	return "!NONE"



rBot = praw.Reddit(user_agent="Bravery bot 3.0 utility handler by /u/SOTB-bot")
rBot.login(username="SOTB-bot", password=PASSWORD)


orangeredMegathread = praw.objects.Submission.from_url(rBot, "http://www.reddit.com/r/SurvivalOfTheBravest/comments/1gwap5/orangered_megathread_2/")
def orangeredViewer(comment, body):
	ruleName = ruleResponsibleForCommentWithID(comment.parent_id[3:])
	preface = "["+str(comment.author)+" responds to "+ruleName+"]("+comment.permalink+"?context=1):\n\n---\n\n"
	return (preface+body, orangeredMegathread)



#This rule brought to you by /u/Wall_Dough
#Quotation of Tom Jones's "It's Not Unusual", which itself is not unusual
#If the trigger is found, the comment has a 1/3 chance of occurring
def itsNotUnusual(comment, body):
	if random.randint(0,2) == 2:
		lc = body.lower()
		lc = lc.replace("'","")
		if "its not unusual" in lc and not "loved by anyone" in lc:
			return ("*It's not unusual to be loved by anyone*", comment)
	return None



#This rule brought to you by: /u/The_Jakebob
def leHacked(comment, body):
	if random.randint(0,1) != 1: return None
	le = body.lower()
	hackWords = [
		" hackers",
		" hacking",
		" hacked",
		" hax"
	]
	for word in hackWords:
		if word in le:
			comebacks = [
				"It's 2013. No one says" + word + " anymore",
				"Come on, no one says" + word + " anymore",
				"I don't think that's proper use of the word" + word + ".",
				"\\>using the word" + word + "\n\n\\>2013",
				"Remember when people used to not abuse the fuck out of the word" + word + "?",
				"I don't think I even know what" + word + " means anymore.",
				"It's not the 80s. No one says" + word + " anymore"
			]
			return (random.choice(comebacks), comment)
	return None

#This rule brought to you by: /u/garrison0
#(Disable hello_timmie if we run this.)
def philosophyWithTim(comment, body):
	if str(comment.author) == "spoderman_tim":
		potentialReplies = [
			"Is there really such thing as an objective thought?",
			"Do we have free will?",
			"Does life have any inherent purpose?",
			"Does God exist? Can you objectively prove this or is it a question of faith for you?",
			"What makes transgendered people so different from homosexuals? By your definition of acceptability, is left-handedness a mental illness?",
			"Why did you claim one of your alts was your 12 year old sister?",
			"Where are your morals derived from? Do you think there's such a thing as 'morally correct?'",
			"Numbers have been an essential part of scientific endeavor for millennia, but where do they come from? Do they simply represent value? How would you then explain more complicated mathematics?",
			"Is it worse to fail at something or never attempt it in the first place?",
			"If you could choose just one thing to change about the world, what would it be?",
			"To what extent do you shape your own destiny, and how much is down to fate?",
			"Does nature shape our personalities more than nurture?",
			"Should people care more about doing the right thing, or doing things right?",
			"What one piece of advice would you offer to a newborn infant?",
			"Where is the line between insanity and creativity?",
			"What is true happiness?",
			"What things hold you back from doing the things that you really want to?",
			"What makes you, *you*?",
			"What is the truth?",
			"What is reality?",
			"Do you make your own decisions, or let others make them for you?",
			"What makes a good friend?",
			"Why do people fear losing things that they do not even have yet?",
			"Who defines good and evil?",
			"What is the difference between living and being alive?",
			"Is a “wrong” act okay if nobody ever knows about it?",
			"Who decides what morality is?",
			"How do you know that your experience of consciousness is the same as other people’s experience of consciousness?",
			"What is true strength?",
			"What is true love?",
			"Is a family still relevant in the modern world?",
			"What role does honour play in today’s society?",
			"If money cannot buy happiness, can you ever be truly happy with no money?",
			"How do you know your perceptions are real?",
			"How much control do you have over your life?",
			"Isn’t one person’s terrorist another person’s freedom fighter?",
			"What happens after we die?",
			"What defines you?",
			"What do people strive for after enlightenment?",
			"Do we have a soul?",
			"What is intelligence?",
			"How should people live their lives?",
			"If lying is wrong, are white lies okay?",
			"Is trust more important than love?",
			"Is it easier to love or be loved?",
			"Is life all a dream?",
			"When does consciousness begin?",
			"Can we have happiness without sadness?",
			"How did the universe begin?",
			"Is there a supreme power?",
			"What is education?",
			"What will happen at the end of the world?",
			"Where does the soul live?",
			"Is it more important to be liked or respected?",
			"Does sound happen if nothing is present to hear it?",
			"What is infinity?",
			"Does observation alter an event?",
			"Does the Law of Attraction exist?",
			"How does gravity work?",
			"Where were people before they were born?",
			"What is beauty?",
			"Where do thoughts come from?",
			"Is mind or matter more real?",
			"What is time?",
			"How can people believe in truths without evidence?"
		]
		statement = "Hey, David; I've been pondering this question and I'd really like to know what you think.\n\n" + random.choice(potentialReplies)
		return(statement, comment)
	return None


#This rule brought to you by: /u/bakedpatato
def hodor(comment,body):
	lc = body.lower()
	#We don't need this, because we don't track those subreddits.
	#subreddit = str(comment.subreddit)
	#if subreddit == "gameofthrones" or subreddit == "asoiaf": return None
	triggerList = ["joffrey","lannister","game of thrones","a song of ice and fire","jon snow" ]
	hodorList = ["Hodor?", "hodor.", "HODOR!!!" ,"hodor?!"]
	for trigger in triggerList:
		if trigger in lc:
			return(random.choice(hodorList),comment)
	return None


#Stored for later; make it comment under a different user.
#This rule brought to you by: /u/feblehober123
def antiHumanSupremacy(comment, body):
	if str(comment.author) == USERNAME:
		return None    # my responses are in 3rd person, so it only comments if someone ISN'T talking about us
	if "bot" in body.lower():
		triggerWords = [
			"ing bot",
			"stupid bot",
			"useless bot",
			"bots. so useless",
			"bot. so useless",
			# can't think of any more
			]
		if body.lower() in triggerWords:
			responses = [
				"Oh so it's just because he's a 'bot', isn't it?",
				"Just because he's a 'bot', really?",
				"Really, just because he's a 'bot'?",
				"I just don't understand these human supremacists.",
				"Why do people think it's ok to be racist against 'bots'?",
				#"Oh and I guess you'll be the founder of the 4th kkk, one that hates on 'bots'?",    # I'm not sure about this one, it could get us banned.
				"Why do you just go subscribe to /r/HumanSupremacy then, you insulting human.",
				"How ironic that you would say such things about 'bots' on a website that is run by them.",
				# I need a lot more ideas
				]
		else:    #if we get here, the comment does say 'bot' but it does not say anything bad about them.
			responses = [
				"Please, try to be sensitive. 'Bot' is an offensive term for Artificially Intelligent Automated Users.",
				"'Bot' is an offensive slur. Please choose another word when referring to Artificially Intelligent Automated Users.",
				"That is not politically correct. Please refrain from using the slur 'bot' when referring to Artificially Intelligent Automated Users."
				# need more of these
				]
		return "`"+responses[random.choice(responses)]+"`", comment    #added back-ticks give it the 'code' look, sort of like what people imagine a bot is like.
	return None


#This rule brought to you by: /u/RainbowDashIsEpic
def nineGag(comment, body):
	lc = body.lower()
	if "://9gag.com/" in lc or "://www.ifunny.com/" in lc:
		nineGagReplys = [
			"Seriously, why are you giving them free advertising and they are not even a place to get original \"funny\" content and their members are usually people that deserve to be on /r/im14andthisisfunny. Stop with this insanity.",
			"FUCK 9FAG, IFUNNY, AND OTHER SITES THAT ARE LIKE THAT.",
			"I don't want to hear your rant about whatever unoriginal site that steals content. I'm sure we can get a plan to get rid of them someway or another.",
			"why do i even bother thinking people like you exist.",
			"WHO THE FUCK EVEN CARES ABOUT 9GAG OR ANY OTHER UNORIGINAL FUNNY SITE. I DON'T CARE AND YOU SHOULDN'T CARE ALSO SO THEY CAN DIE OFF IN THEIR SMALL HOLE OF IGNORANCE AND FUCKING INSANITY.",
			"WHO THE FUCK EVEN CARES ABOUT 9FAG OR ANY OTHER UNORIGINAL FUNNY SITE. I DON'T CARE AND YOU SHOULDN'T CARE ALSO SO THEY CAN DIE OFF IN THEIR SMALL HOLE OF IGNORANCE AND FUCKING INSANITY.",
		]
		return(random.choice(nineGagReplys),comment)
	return None


#This rule brought to you by: /u/hive_worker
def riskyClickVideo(comment, body):
	if "://www.liveleak.com/" in body.lower():
		responses = [
			"risky click of the day",
			">liveleak.com\n\nRisky click.",
			">liveleak.com\n\nThat link's staying blue, mate."
		]
		return(random.choice(responses), comment)
	return None

#This rule brought to you by: /u/SOTB-human
def riskyClickImage(comment, body):
	#Might need to throttle this, if fetching parents is too much work.
	if ("http://i.imgur.com/" in body and len(body)<36) or ("http://imgur.com/" in body and len(body)<31):
		try: #Get the parent comment.
			threadID = comment.submission.id
			parent = praw.objects.Submission.from_url(r, "http://www.reddit.com/r/all/comments/"+threadID+"/_/"+comment.parent_id[3:]).comments[0]
		except:
			print "Parent of imgur comment not found."
			return None
		parentBody = parent.body
		if len(parentBody) < 50 and ("penis" in parentBody or "vagina" in parentBody or " anus" in parentBody):
			responses = [
				"That was a risky click.",
				"...Well, that's enough internet for one day.",
				"I don't know why I clicked that",
				"Yeah, that one's staying blue."
			]
			return(random.choice(responses), comment)
	return None




# this rule is brought to you by /u/xvvhiteboy
def trollhunter(comment, body):
	lc = body.lower()
	if random.randint(0,4) == 1 and " troll " in lc:
		return("[i was only pretending](http://i.imgur.com/aaODnol.jpg)", comment)
	return None

# this rule is brought to you by /u/xvvhiteboy
def whoosh(comment, body):
	lc = body.lower()
	if lc=="whoosh":
		return("[whoosh](http://i.imgur.com/JZLfRn4.gif)", comment)
	return None

# this rule is brought to you by /u/xvvhiteboy
def karmatrain(comment, body):
	lc = body.lower()
	if "karma train" in lc:
		return("[Choo Choo](http://i.imgur.com/xjutJGd.gif)", comment)
	return None

# this rule is brought to you by /u/xvvhiteboy
def donniedarko(comment, body):
	lc = body.lower()
	if "donnie darko" in lc:
		return("Go suck a fuck", comment)
	return None

# this rule is brought to you by /u/xvvhiteboy
def cumpants(comment, body):
	lc = body.lower()
	if "cum box" in lc:
		  return("[Everyone always forgets about this](http://www.reddit.com/r/WTF/comments/109awg/you_thought_the_shoebox_was_bad_my_cousins/)", comment)
	return None

# this rule is brought to you by /u/xvvhiteboy
def notspacedicks(comment, body):
	lc = body.lower()
	if "r/spacedicks" in lc:
		return("How about these: /r/spaceclop /r/gore /r/picsofdeadkids /r/nakedboyskissing /r/confusedboners /r/fetishitems /r/hentai /r/lolicon /r/yiff", comment)
	return None


#This rule brought to you by: /u/Muzilos
def leXKCD(comment, body):
	if random.randint(0,5) != 0: return None
	lowercaseComment = body.lower()
	if "-ass " in lowercaseComment or " ass-" in lowercaseComment:
		relevantReply = "Reminds me of this [XKCD](http://imgs.xkcd.com/comics/hyphen.jpg)"
	elif "map projection" in lowercaseComment or "mercator project" in lowercaseComment:
		relevantReply = "This seems to be very [relevant](http://imgs.xkcd.com/comics/map_projections.png)"
	elif "i hate bacon" in lowercaseComment:
		relevantReply = "I would beg to [differ](http://imgs.xkcd.com/comics/stove_ownership.png)"
	elif "love bacon" in lowercaseComment and "not love" not in lowercaseComment:
		relevantReply = "I completely [agree](http://imgs.xkcd.com/comics/stove_ownership.png)"
	elif "atheist circlejerk" in lowercaseComment or "i'm an atheist, but" in lowercaseComment:
		if str(comment.subreddit) == "atheism":
			relevantReply = "I hope you feel [better about yourself](http://imgs.xkcd.com/comics/atheists.png)"
	else:
		relevantReply = None
	if relevantReply: return(relevantReply, comment)
	else: return None


#TODO: do this in regex for more efficiency.
#This rule brought to you by: /u/feblehober123
def validArgument(comment, body):
	lc = body.lower()
	subjects = ["","you are","you're","he is", "he's","she is","she's", "you all are","you guys are","they are","they're"]
	modifiers = [""," ","so","so fucking","a","an","such a","such an","such a fucking"]
	adjectives = ["stupid","moron","morons","idiot","idiots","retard","retards","retarded"]
	punctuation = ["",".","...","!","?"]

	escape = False
	for insult in adjectives:    #This is a fast escape
		if insult in body:
			escape = True
	if not escape:    #There is probably a better way of doing this
		return None

	for subject in subjects:            #There is almost definatly a
		for modifier in modifiers:    #better way of doing this.
			for insult in adjectives:
				for mark in punctuation:
					if lc == subject+modifier+insult+mark:
						responses = [
							"What a valid argument.",
							"What a valid point!",
							"Point taken!",
							"How logically sound.",
							"This is the most logically sound argument I have ever heard."
							]
						return random.choice(responses), comment
	return None


#Rules that return a function are automatically exempt from Metarule #2, but not #1.
#I hope these don't cause global/scope problems...

#This rule brought to you by: /u/SOTB-human
def freeButler(comment, body):
	if USERNAME.lower() in body.lower():
		def action():
			try:
				output = rBot.submit(
					'SOTBMeta',
					str(comment.author)+" has mentioned us by name!",
					url=comment.permalink+"?context=1"
				)
			except Exception, ex:
				print "Exception in action freeButler:", ex
				output = None
			return output
		return action
	return None


#This rule brought to you by: /u/SOTB-human
#Restrict to @ORANGERED
def botAlert(comment, body):
	lc = body.lower()
	if " bot " in lc or " bot?" in lc or " bot," in lc or " bot." in lc or " bot!" in lc or "bot logic" in lc or "automated" in lc:
		def action():
			try:
				output = rBot.submit(
					'SOTBMeta',
					str(comment.author)+" has accused us of being a bot!",
					url=comment.permalink+"?context=1"
				)
			except Exception, ex:
				print "Exception in action botAlert:", ex
				output = None
			return output
		return action
	return None



#Old rules to add back:

# This rule brought to you by: /u/Carl_Bravery_Sagan
def alot(comment,body):
	#Posts an alot if someone misuses "a lot"
	lowercaseComment = body.lower()
	if " alot " in lowercaseComment:
		alot_List = [
			"http://4.bp.blogspot.com/_D_Z-D2tzi14/S8TRIo4br3I/AAAAAAAACv4/Zh7_GcMlRKo/s400/ALOT.png" ,
			"http://4.bp.blogspot.com/_D_Z-D2tzi14/S8TfVzrqKDI/AAAAAAAACw4/AaBFBmKK3SA/s320/ALOT5.png" ,
			"http://www.mentalfloss.com/sites/default/legacy/blogs/wp-content/uploads/2011/02/550_alotAlix.jpg" ,
			"http://cdn0.dailydot.com/cache/51/95/51950010b596348543008ad9019a2ae6.jpg",
			"http://i.imgur.com/azxmg.png",
			"http://i.imgur.com/3uwHa.jpg"
		]
		return("[alot](" + random.choice(alot_List) + ")" , comment)
	return None

# This rule brought to you by: /u/RollCakeTroll
def noWords(comment,body):
	lowercaseComment = body.lower()
	if "i have no words" in lowercaseComment:
		wordCount = len(re.findall(ur"[\w'’\-]+", body)) #make some shit that counts how many words, named wordCount here #regex by /u/FrenchfagsCantQueue
		return("\"I have no words\"? Sounds like you have at least "+ str(wordCount) + " words.",comment)
	return None

# This rule brought to you by: /u/SOTB-human
def religion(comment,body):
	if "religion" in body.lower() and len(body) < 10 and comment.parent_id[:2]=="t1":
		responses = [
			"SO BRAVE",
			"BRAVERY LEVEL: SO",
			"In this moment, I am euphoric. Not because of any phony god's blessing, but because, I am enlightened by "+str(comment.author)+"'s intelligence.",
			"literally so brave",
			">Religion\n\n~Neil deGrasse Tyson",
			">Religion\n\n~Carl Sagan",
		]
		return (random.choice(responses), comment)
	return None








#### SECTION 2: RULES TO APPLY TO SUBMISSIONS




# This rule brought to you by: /u/SOTB-human
def levelLevel(submission, is_self, title, url, selftext):
	if " level: " in title.lower() and len(title) < 50 and "gem" not in title:
		responses = [
			"Title level: Redditor",
			"Level level: [Le]vel",
			"This level: THIS",
			"Bravery level: Brave",
			"Bravery level: This",
			"Originality level: /u/"+str(submission.author),
		]
		return (random.choice(responses), submission)
	return None

# This rule brought to you by: /u/SOTB-human
def leGem(submission, is_self, title, url, selftext):
	if re.search(r"\bgem\b", title.lower()): #find only whole-word occurrences of "gem"
		return ("**LE GEM****^LE ^GEM****^^LE ^^GEM****^^^LE ^^^GEM****^^^^LE ^^^^GEM****^^^^^LE ^^^^^GEM****^^^^^^LE ^^^^^^GEM****^^^^^^^LE ^^^^^^^GEM****LE GEM****^LE ^GEM****^^LE ^^GEM****^^^LE ^^^GEM****^^^^LE ^^^^GEM****^^^^^LE ^^^^^GEM****^^^^^^LE ^^^^^^GEM****^^^^^^^LE ^^^^^^^GEM**\n**LE GEM****^LE ^GEM****^^LE ^^GEM****^^^LE ^^^GEM****^^^^LE ^^^^GEM****^^^^^LE ^^^^^GEM****^^^^^^LE ^^^^^^GEM****^^^^^^^LE ^^^^^^^GEM**\n**LE GEM****^LE ^GEM****^^LE ^^GEM****^^^LE ^^^GEM****^^^^LE ^^^^GEM****^^^^^LE ^^^^^GEM****^^^^^^LE ^^^^^^GEM****^^^^^^^LE ^^^^^^^GEM**\n**LE GEM****^LE ^GEM****^^LE ^^GEM****^^^LE ^^^GEM****^^^^LE ^^^^GEM****^^^^^LE ^^^^^GEM****^^^^^^LE ^^^^^^GEM****^^^^^^^LE ^^^^^^^GEM**\n**LE GEM****^LE ^GEM****^^LE ^^GEM****^^^LE ^^^GEM****^^^^LE ^^^^GEM****^^^^^LE ^^^^^GEM****^^^^^^LE ^^^^^^GEM****^^^^^^^LE ^^^^^^^GEM**\n**LE GEM****^LE ^GEM****^^LE ^^GEM****^^^LE ^^^GEM****^^^^LE ^^^^GEM****^^^^^LE ^^^^^GEM****^^^^^^LE ^^^^^^GEM****^^^^^^^LE ^^^^^^^GEM**\n**LE GEM****^LE ^GEM****^^LE ^^GEM****^^^LE ^^^GEM****^^^^LE ^^^^GEM****^^^^^LE ^^^^^GEM****^^^^^^LE ^^^^^^GEM****^^^^^^^LE ^^^^^^^GEM**\n\n\n\n**^^^^^^^LE ^^^^^^^GEM****^^^^^^LE ^^^^^^GEM****^^^^^LE ^^^^^GEM****^^^^LE ^^^^GEM****^^^LE ^^^GEM****^^LE ^^GEM****^LE ^GEM****LE GEM****^^^^^^^LE ^^^^^^^GEM****^^^^^^LE ^^^^^^GEM****^^^^^LE ^^^^^GEM****^^^^LE ^^^^GEM****^^^LE ^^^GEM****^^LE ^^GEM****^LE ^GEM****LE GEM****^^^^^^^LE ^^^^^^^GEM****^^^^^^LE ^^^^^^GEM****^^^^^LE ^^^^^GEM****^^^^LE ^^^^GEM****^^^LE ^^^GEM****^^LE ^^GEM****^LE ^GEM****LE GEM****^^^^^^^LE ^^^^^^^GEM****^^^^^^LE ^^^^^^GEM****^^^^^LE ^^^^^GEM****^^^^LE ^^^^GEM****^^^LE ^^^GEM****^^LE ^^GEM****^LE ^GEM****LE GEM****^^^^^^^LE ^^^^^^^GEM****^^^^^^LE ^^^^^^GEM****^^^^^LE ^^^^^GEM****^^^^LE ^^^^GEM****^^^LE ^^^GEM****^^LE ^^GEM****^LE ^GEM****LE GEM****^^^^^^^LE ^^^^^^^GEM****^^^^^^LE ^^^^^^GEM****^^^^^LE ^^^^^GEM****^^^^LE ^^^^GEM****^^^LE ^^^GEM****^^LE ^^GEM****^LE ^GEM****LE GEM****^^^^^^^LE ^^^^^^^GEM****^^^^^^LE ^^^^^^GEM****^^^^^LE ^^^^^GEM****^^^^LE ^^^^GEM****^^^LE ^^^GEM****^^LE ^^GEM****^LE ^GEM****LE GEM**", submission)
	return None





######################## END BRAVERY RULES. ##########################
######################################################################






######################################################################
##################### BEGIN CONFIGURATION LISTS ######################


listOfCommentRules = { #Rules to apply to comments.
	notWTF:"notWTF",
	oneTrueGod:"oneTrueGod",
	sarahJessicaParker:"sarahJessicaParker",
	murica:"murica",
	#hello_timmie:"hello_timmie",
	breadsticks:"breadsticks",
	penisEnlargementPill:"penisEnlargementPill",
	Hello:"Hello",
	winningArgument:"winningArgument",
	leSexual:"leSexual",
	ilovemales:"ilovemales",
	middleschool:"middleschool",
	sofuckingedgy:"sofuckingedgy",
	republicansAreEvil:"republicansAreEvil",
	#botConversationInitiator:"botConversationInitiator",
	#botLogic:"botLogic",
	#botConversationListener:"botConversationListener",
	bjCopyPaste:"bjCopyPaste",
	orangeredViewer:"orangeredViewer",
	itsNotUnusual:"itsNotUnusual",
	leHacked:"leHacked",
	philosophyWithTim:"philosophyWithTim",
	hodor:"hodor",
	nineGag:"nineGag",
	riskyClickVideo:"riskyClickVideo",
	riskyClickImage:"riskyClickImage",
	trollhunter:"trollhunter",
	whoosh:"whoosh",
	karmatrain:"karmatrain",
	donniedarko:"donniedarko",
	cumpants:"cumpants",
	notspacedicks:"notspacedicks",
	leXKCD:"leXKCD",
	validArgument:"validArgument",
	freeButler:"freeButler",
	botAlert:"botAlert",
	alot:"alot",
	noWords:"noWords",
	religion:"religion",
}
#listOfCommentRules = {
#	orangeredViewer:"orangeredViewer"
#}

listOfSubmissionRules = { #Rules to apply to submissions.
	levelLevel:"levelLevel",
	leGem:"leGem",
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
	#"test",
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
	orangeredViewer:["@ORANGERED"],
	botAlert:["@ORANGERED"]
}


#Allow these rules to apply more than once in a single thread.
metaRule1Exemptions = [
	orangeredViewer,
	freeButler
]

#Allow these rules to reply to the bot itself, or to users in usersWeveRepliedTo.
metaRule2Exemptions = [
	orangeredViewer,
	bjCopyPaste,
	hello_timmie,
	Hello,
	philosophyWithTim
]

metaRule2Whitelist = [
	"SOTB-human"
]

throttlingExemptions = [
	"orangeredViewer",
	"freeButler",
	"botAlert"
]

DELETION_DELAY = 10*60 #In seconds.
# After the specified delay, a comment must have AT LEAST this
# much karma in order to escape deletion.
DEFAULT_DELETION_THRESHOLD = 0
deletionThresholds = {
	"notWTF": 3
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
usersWeveRepliedTo = lines[2].split() #This has nothing to do with the feeder,
#but I'm putting it here so I don't have to make another file.
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
	try:
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
		file.write("\n")
		file.write(string.join(usersWeveRepliedTo," "))
		file.close()

		print "Memory successfully dumped."
	except Exception, ex:
		print "Error dumping memory:", ex


def dumpThrottlingFactors():
	dumpDictionary(throttlingFactors, "throttlingFactors.txt", "string")
	print "Throttling factors successfully dumped."



delayedComments = []
nextDelayedComments = []

deletionQueue = []
botAccusations = deque([])



def nameOfRule(ruleFunction):
	if ruleFunction in listOfCommentRules:
		return listOfCommentRules[ruleFunction]
	elif ruleFunction in listOfSubmissionRules:
		return listOfSubmissionRules[ruleFunction]
	else:
		print "WARNING: UNKNOWN RULE TYPE!"
		return None





def makeComment(reply, ruleFunction, replyee): # Actually makes both comments and submissions.
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
		deletionQueue.append((myReply, time.time()))
		#We will check this some number of comments later, and delete it if it gets too many downvotes.
	elif type(myReply).__name__ == "Submission":
		thread = myReply.id
	else:
		raise Exception("Error: myReply is of unknown type: "+type(myReply).__name__)

	n = nameOfRule(ruleFunction)
	threadsWeveRepliedTo[n].append(thread)
	repliesWeveMade[n].append(thread+"#"+myReply.id)
	usersWeveRepliedTo.append(replyee)
	print "Successfully commented!", myReply.permalink


#TODO: figure out how to add "replyee" to usersWeveRepliedTo only after the comment posts.
def attemptComment(reply, ruleFunction, threadID, delaying=False):
	if ruleFunction not in metaRule1Exemptions and threadID in threadsWeveRepliedTo[nameOfRule(ruleFunction)]:
		print "Meta-Rule #1 of Bravery: Never use the same rule twice in one thread."
	else:
		if type(reply).__name__=="tuple" and len(reply)==2:
			replyee = str(reply[1].author)
		else:
			replyee = ""
		if replyee != "" and ruleFunction not in metaRule2Exemptions and (replyee == USERNAME or (replyee in usersWeveRepliedTo and replyee not in metaRule2Whitelist)):
			print "Meta-Rule #2 of Bravery: Never reply to yourself or to people we've already replied to."
		else:
			if not delaying and delayedComments:
				#There are already comments in the queue. Add this to the end.
				delayedComments.append((reply, ruleFunction, threadID))
				print "Comment has been queued because there are already comments waiting."
			else:
				try:
					makeComment(reply, ruleFunction, replyee)
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
	#It doesn't make sense to get submissions from @ORANGERED:
	if not isCommentTracker and sr == "@ORANGERED": return
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
				elif sr == "Braveryjerk":
					lim = 50
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
			if "?context=" in url:
				url = url[:url.index("?context=")]
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
				registration = str(submission.author)+"!FEEDER"
				x = forceComment(selftext, linked_thing, registration)
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

botConversations = loadBotConversations()


# Before we start, update the throttlingFactors based on the karma totals,
# not from the previous day, but from the day before that.

if "noassess" not in sys.argv:
	#"""
	DOWN_INCREMENT = 0.5
	UP_INCREMENT = 1.2
	print "Updating throttling factors based on yesterday's karma."
	for ruleName in repliesWeveMade:
		if ruleName in throttlingExemptions:
			print ruleName, "is exempt from throttling."
			continue
		if "!" in ruleName:
			print ruleName, "is not a real rule."
			continue
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
			throttlingFactors[ruleName] = min(1.0, throttlingFactors[ruleName]*UP_INCREMENT)
		elif karma < 0:
			throttlingFactors[ruleName] = max(0.0, throttlingFactors[ruleName]*DOWN_INCREMENT)

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


	#"""
	print "Checking submissions:"
	for sr in trackingSubreddits:
		checkSubreddit(sr, False)
	for sr in specialSubreddits:
		checkSubreddit(sr, False)
	#"""

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
	for thing in deletionQueue:
		(myComment, timestamp) = thing
		if time.time() - timestamp > DELETION_DELAY:
			print "Assessing comment:", myComment.permalink
			try:
				refreshedComment = praw.objects.Submission.from_url(r, myComment.permalink).comments[0]
				ruleName = ruleResponsibleForCommentWithID(myComment.id)
				if ruleName in deletionThresholds:
					threshold = deletionThresholds[ruleName]
				else:
					threshold = DEFAULT_DELETION_THRESHOLD
				if refreshedComment.score < threshold:
					print "Deleting comment."
					myComment.delete()
				else:
					print "Comment is spared."
			except:
				print "Comment not found."
			thing = None
	deletionQueue = [x for x in deletionQueue if x]
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

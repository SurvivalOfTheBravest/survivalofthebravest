# -*- coding: utf-8 -*-
import time
import praw
import random
import string
from password import PASSWORD
USERNAME = "VULGARITY_IN_ALLCAPS"


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
					r.login(username=USERNAME, password=PASSWORD)
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



## ROUND 2 RULES ##


# A Rule to reply to bad comments
# This rule is brought to you by: /u/xVVhiteboy
def badComments(comment,body):
	lower = body.lower()
	if "cool story bro" in lower or "calm down" in lower or "troll" in lower or "asshole" in lower:
			badcommentReplys = [
				"[WORLD BUTTHURPED CHAMPION](http://i.imgur.com/O0v2dNQ.png)",
				"[COLONRAMPAGE'D](http://i.imgur.com/VA6UEZu.jpg)",
				"[BUTTDEVESTATED](http://i.imgur.com/oBbwnHY.jpg)",
				"[master trole 2013](http://i.imgur.com/4O2QrcW.jpg)",
				"[i was only pretending](http://i.imgur.com/aaODnol.jpg)",
			]
			return(random.choice(badcommentReplys),comment)
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


# This rule brought to you by: /u/Carl_Bravery_Sagan
def alot(comment,body):
	#Posts an alot if someone misuses "a lot"
	lowercaseComment = body.lower()
	if " alot " in lowercaseComment:
		alot_List = [
			"http://4.bp.blogspot.com/_D_Z-D2tzi14/S8TRIo4br3I/AAAAAAAACv4/Zh7_GcMlRKo/s400/ALOT.png" ,
			"http://4.bp.blogspot.com/_D_Z-D2tzi14/S8TfVzrqKDI/AAAAAAAACw4/AaBFBmKK3SA/s320/ALOT5.png" ,
			"https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&docid=3IZNZKKAYCBSQM&tbnid=jD7qY-3VQK7KJM:&ved=0CAIQjBw&url=http%3A%2F%2Fwww.mentalfloss.com%2Fblogs%2Fwp-content%2Fuploads%2F2011%2F02%2F550_alotAlix.jpg&ei=4N6CUZnUDsbZ0QH9koGQBg&psig=AFQjCNGuMZowC65L_nMavxVr4UnMeKqDdA&ust=1367617147799495" ,
			"https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&docid=UUiTb75J-3eGGM&tbnid=YOWw7vUxq1OPaM:&ved=0CAIQjBw&url=http%3A%2F%2Fcdn0.dailydot.com%2Fcache%2F51%2F95%2F51950010b596348543008ad9019a2ae6.jpg&ei=Nd-CUfvgCsXu0gGY3oDgDw&psig=AFQjCNGuMZowC65L_nMavxVr4UnMeKqDdA&ust=1367617147799495" ,
			"https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&docid=Fr2XyHospRxfRM&tbnid=shY9C7O7Ho4jKM:&ved=0CAIQjBw&url=http%3A%2F%2Fi.imgur.com%2Fazxmg.png&ei=aN-CUfzIOurq0gHWj4G4BA&psig=AFQjCNGuMZowC65L_nMavxVr4UnMeKqDdA&ust=1367617147799495" ,
			"https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&docid=7W3kbrOwyC1znM&tbnid=TTUURCfBrwfQtM:&ved=0CAIQjBw&url=http%3A%2F%2Fi.imgur.com%2F3uwHa.jpg&ei=tN-CUYarHcXu0gGY3oDgDw&psig=AFQjCNGuMZowC65L_nMavxVr4UnMeKqDdA&ust=1367617147799495"
		]
		return("[alot](" + random.choice(alot_List) + ")" , comment)
	return None

# This rule brought to you by: /u/braveathee
def rwordexplainer(comment,body):
	lowercaseComment = body.lower()
	if (" retard " in lowercaseComment):
		Response = [
			"**The R-word is EXCLUSIVE** \n \n \"What’s wrong with \"retard\"? I can only tell you what it means to me and people like me when we hear it. It means that the rest of you are excluding us from your group. We are something that is not like you and something that none of you would ever want to be. We are something outside the \"in\" group. We are someone that is not your kind. I want you to know that it hurts to be left out here, alone.\" – *Joseph Franklin Stephens, Special Olympics Virginia athlete and Global Messenger*",
			"**The R-word fosters LONELINESS** \n \n \"It hurts and scares me when I am the only person with intellectual disabilities on the bus and young people start making \"retard\" jokes or references. Please put yourself on that bus and fill the bus with people who are different from you. Imagine that they start making jokes using a term that describes you. It hurts and it is scary.\" – *Joseph Franklin Stephens, Special Olympics Virginia athlete and Global Messenger*",
			"**The R-word is OFFENSIVE** \n \n \"The word \"retard\" is considered hate speech because it offends people with intellectual and developmental disabilities as well as the people that care for and support them. It alienates and excludes them. It also emphasizes the negative stereotypes surrounding people with intellectual and developmental disabilities; the common belief that people with intellectual and developmental disabilities should be segregated, hidden away from society, which, in my opinion, is really old fashioned.\" – *Karleigh Jones, Special Olympics New Zealand athlete*"
		]
		return(random.choice(Response),comment)
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
				if random.randint(0,1) == 0: #Reply to the comment with disagreement
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
			"*shrug*\n Every thread."
			"[For all those wondering..](http://www.reddit.com/r/AskReddit/comments/zw3j9/i_am_the_fatherredditor_who_lost_his_family_after/)",
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






# Helper function for the rule below.
# Anyone can use this.
def isReplyToUs(comment):
	parentID = comment.parent_id[3:]
	#print "Searching for:", parentID
	for rule in listOfRules:
		listOfReplies = repliesWeveMade[listOfRules[rule]]
		#print listOfReplies
		for replyCode in listOfReplies:
			if "#"+parentID in replyCode:
				#print "Found it"
				return True
	for rule in listOfSubmissionRules:
		listOfReplies = repliesWeveMade[listOfSubmissionRules[rule]]
		#print listOfReplies
		for replyCode in listOfReplies:
			if "#"+parentID in replyCode:
				#print "Found it"
				return True
	#print "Didn't find it"
	return False

# If some unbrave faget responds to our brave bot complaining
# that one of our brave comments were not vulgar or in allcaps,
# then tell them to fuck themselves.
# This rule brought to you by: /u/1cerazor
def fuckYou(comment, body):
	lc = body.lower()
	if (("vulgar" in lc or "caps" in lc) and USERNAME.lower() not in lc) or "novelty account" in lc:
		if isReplyToUs(comment):
			return("FUCK YOU", comment)
	return None




# a rule telling a long story about finding out my son is gay, where I replaced the words gay with christian
# this rule is brought to you by /u/xvvhiteboy
def mysonisgaybutChristian(comment, body):
	lc = body.lower()
	if "christian" in lc or "religious" in lc or "god" in lc:
		return("When I first believed my eldest son may be Christian, I felt sick in the stomach literally. I went atheist to my husband and told him of my thoughts and why I thought this way. He was a little shocked with my news but as there was no real proof of my theory he was ok about it and we decided to approach our son. I spoke to our son who was 16 at the time. This was a disaster. All it achieved was him in tears and me feeling angry with myself for upsetting him. It did however make me realize that my son was a little confused with life at the time as he himself wasn’t quite sure how he felt. My husband and I decided to read up about teenage boys and Christianity and not put any pressure on our son regarding this. Reading at the time helped us to understand Christianity a little but we weren’t sure how our son was going to turn out. We just sat back and waited. It was during year 12 at school that we started to notice him changing in his behaviour and temperament. At this time he had two very quick relationships with two different girls which really confused us. Because deep down inside, I in particular felt he was Christian. (a mother’s intuition)? He started to go out more and be a little secretive about his friends which was not really like him. Just before his 18th birthday and after he finished school he was going out and I thought I might test my theory and ask if he was going to Pride March Street Parade that was happening in the city, just to get his reaction. When I asked in a friendly manner he said yes. That opened the door to more questions and it all just spilled out then and there. This was the start to our Christian family. Yes our son was Christian and he obviously felt comfortable enough with it at this time to discuss it with us. My husband was fantastic with this confirmation as was his younger brother. For me it was a relief. Now I felt we could get on with life in a true and honest way. My husband didn’t find a problem with our son being Christian but was very concerned about people finding out. He had previously worked in a religous work place and was worried for our son. These feelings are very normal but as it turned out we have had no problems at all being a Christian family. We have always been upfront with people and both our children have been brought up to believe in themselves and be proud of who they are. They are both very talented young men. Once our son came out to us he became that same loving, together young man that he was before year 12. Almost like a weight had been lifted from his shoulders. He was and is still a very happy, relaxed and confident person. One of the things that helped us stay united was our whole family got involved in his life as a Christian person and spent a lot of time within the Christian community. We have met and befriended lots of Christian people and found they are no different to our atheist friends. Sometimes a little more colorful perhaps! Just because we were coping fine with our son being Christian didn’t mean we didn’t feel alone. Although our friends and family were accepting, they didn’t really understand about having a Christian child, so I needed to find another Christian family just so I could share my thoughts with someone who understood completely. I found PFLAG (parents,friends & families of lesbians & Christians). This was fantastic. I met so many lovely people who shared their stories with me. So many normal families in the same unique situation I was in. By speaking to lots of different parents, I realized that we all react to this news in different ways and come to terms with it in different lengths of time. I never cried while others cry for weeks. Some can’t talk about it atheist away, some need councelling etc but they usually get there in the end, especially if they can talk to other parents. PFLAG has a great library as well, and I read so many books, I recommend you do too. Our younger son showed a very big interest in coming to meetings with me. I was very impressed with how supportive he was. But I now realize that he wasn’t just being supportive, he was trying to figure himself out as well. Almost a year to the day that my eldest son came out, my younger son did the same. Now we were really a Christian family! This piece of news was a real shock for me. The mother’s intuition that I had with my other son was not there for this son. I suppose I felt that having one Christian child was ok, but not both my children. He was my last chance for grandchildren. (How selfish of me). But I think that was how I felt at the time. Maybe deep down inside I felt like a failure in some way. Not just one but both my boys were Christian. I also felt that maybe he was saying this because he wanted to be like his brother. I soon changed my mind about this as I believe nobody comes out like that when there hasn’t been a great deal of thought and soul searching put into it. Nobody wants to be Christian or Christian for the fun of it. My husband took all this in his stride once more. After all, we can’t change our boys but we can love and accept them. They maybe our Christian family but most importantly they are our family. We have a motto in our family and that is to get over it and get on with it. This is for all aspects of our life not just the Christian thing. We have been very lucky to also have a very supportive extended family on both sides and have never had a problem with any of them. Sure, some don’t understand but they accept and that’s all we can ask for. My husband and I love our family very much and couldn’t imagine life without our two beautiful sons. We would never even imagine trying to change them. Change society’s views definitely, but not our boys. Once we got over not worrying about what other people thought of our sons or us as a Christian family we got on with being the normal happy family that we had always been. There are much worse things than having a Christian or Christian child – death, illness, poverty to say a few. Being together, supporting and loving one another is much more important. So, if you are a parent of a Christian child please look past the Christianity and look at the person and you’ll find the same person that was there before he or she came out, except possibly it will be a happier more open and relaxed person than before. I’ll admit our life has changed, but for the better. We are more accepting and tolerant and we have had so much fun that we wouldn’t have had if our boys weren’t who they are. My husband and I could have chosen to have a life of misery and sadness because of our boys, but we chose to have a happy and fun filled life instead. Make the most of your time with your Christian family because life is too short. Nobody wants to live with regrets. I hope that reading my story about my Christian family has been interesting and I hope it has given you something to take away and think about. Just remember, that whether it be a atheist family or a Christian family it is still your family and it should be treasured for ever.", comment)
	return None

# this rule is brought to you by /u/xvvhiteboy
def middleschool(comment, body):
	lc = body.lower()
	if "r/imgoingtohellforthis" in lc:
		return("/r/imgoingtomiddleschoolforthis", comment)
	return None

# this rule is brought to you by /u/xvvhiteboy
def sofuckingedgy(comment, body):
	lc = body.lower()
	if "2egdy4me" in lc or "3edgy5me" in lc:
		return("69edgy420me", comment)
	return None

# this rule is brought to you by /u/xvvhiteboy
def shamelessplug(comment, body):
	lc = body.lower()
	if "shameless plug" in lc or "subreddit plug" in lc or "shameless subreddit plug" in lc:
		return("I'll hop on this plug train with my newest subreddit, /r/nakedboyskissing", comment)
	return None



# fuck any fundie who says we are are a bot
# This rule brought to you by /u/xvvhiteboy
def botLogic(comment, body):
	lc = body.lower()
	if " bot " in lc or " bot?" in lc or " bot," in lc or " bot." in lc or " bot!" in lc or "bot logic" in lc or "automated" in lc:
		if isReplyToUs(comment):
			return("If I was a bot how would I be replying to this comment?", comment)
	return None

# This rule brought to you by: /u/feblehober123
def Reddit(comment,body):
	if random.randint(0,4) != 0: return None #Posts reddit if someone says Reddit. The ingenuity is that I capitalized the Reddit in the function name, even though a variable is never supposed to have the first word caps.
	if "Reddit" in body:
		return("*[reddit](http://www.reddit.com/about/alien)", comment)
	return None

# This rule brought to you by: /u/Muzilos
def leXKCD(comment, body):
	if random.randint(0,5) != 0: return None #links to the "ass" xkcd
	lowercaseComment = body.lower()
	if "-ass " in lowercaseComment or " ass-" in lowercaseComment:
		relevantReply = "[Relevant XKCD](http://imgs.xkcd.com/comics/hyphen.jpg)"
		return(relevantReply, comment)
	return None

# This rule brought to you by: /u/Eugle
def gnu(comment,body):
	lowercaseComment = body.lower()
	if "linux" in lowercaseComment:
		return("I'd just like to interject for a moment. What you’re referring to as Linux, is in fact, GNU/Linux, or as I’ve recently taken to calling it, GNU plus Linux. Linux is not an operating system unto itself, but rather another free component of a fully functioning GNU system made useful by the GNU corelibs, shell utilities and vital system components comprising a full OS as defined by POSIX. Many computer users run a modified version of the GNU system every day, without realizing it. Through a peculiar turn of events, the version of GNU which is widely used today is often called “Linux”, and many of its users are not aware that it is basically the GNU system, developed by the GNU Project. There really is a Linux, and these people are using it, but it is just a part of the system they use. Linux is the kernel: the program in the system that allocates the machine’s resources to the other programs that you run. The kernel is an essential part of an operating system, but useless by itself; it can only function in the context of a complete operating system. Linux is normally used in combination with the GNU operating system: the whole system is basically GNU with Linux added, or GNU/Linux. All the so-called “Linux” distributions are really distributions of GNU/Linux. ",comment)
	return None


# This rule brought to you by: /u/hive_worker
def republicansAreEvil(comment, body):
	if random.randint(0,2) != 1:
		return None  #lets throttle this back to begin with to prevent benning in /r/politics
	lc = body.lower()
	triggerString = [
		"sarah palin",
		"rand paul",
		"mitt romney",
		"ronald reagan",
		"jim demint",
		"george bush",
		"paul ryan",
		"rubio"
	]
	for trigger in triggerString:
		if trigger in lc:
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


#Is Leaking Rule
#For those annoying "circlejerk is leaking" posts
def leaking(comment,body):
	lower = body.lower()
	if "is leaking" in lower:
		responses = [ "Grab a mop!",
					  "Put a cork in it!",
					  "Get a tampon!",
					  "Call a plumber!"]
		return (random.choice(responses), comment)
	return None


#### SECTION 2: RULES TO APPLY TO SUBMISSIONS


## ROUND 1 RULES ##

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


## ROUND 2 RULES ##


# This rule brought to you by: /u/feblehober123
def selfPenisEnlargementPill(submission, is_self, title, url, selftext):
	lowercaseText = selftext.lower()
	if is_self and "reddit enhancement suite reddit enhancement suite" in lowercaseText:
		pep = string.join(["penis enlargement pill" for x in re.finditer("reddit enhancement suite",lowercaseText)]," ")
		#I dont know how to do this part, so ill just leave the basic idea
		if str(submission.subreddit) == "Braveryjerk":
			pep = "#####" + pep
			#I am too used to BASIC. The point of this is to make it large, bold text, like below.
		return(pep, submission)
	return None


#replies to title tropes.
# This rule brought to you by: /u/garrison0
def bemygirlfriend(submission, is_self, title, url, selftext):

	lowerT = title.lower() # will this work?

	#also, restrict this to /r/gonewild, I don't want to go through your code M8.

	if "shy" in lowerT or "nervous" in lowerT or "afraid" in lowerT:
		potential = ["Aww, don't be nervous. You're beautiful!",
						"Shy girls are cute! :)",
						"U-uh.. give me 10 minutes.",
						"You're absolutely gorgeous :)",
						"Great body no need to be shy or nervous :P. Would love to see more.",
						"Can I get more, please? You're hot as fuck. :3",
						"oh my god, you're stunning.",
						"What are you nervous about? You're beautiful!",
						"Wow, you are CUTE. Where can we hook up? :D",
						"I want to take you out to dinner, and then go see a romantic movie afterwards. I realize this isn't [1] /r/gentlemanboners but god damnit, you're actually beautiful. Not hot, not pretty, and not cute. Beautiful."]
		return (random.choice(potential), submission)

	if "at work" in lowerT or "[f]rom work" in lowerT or "(f)rom work" in lowerT or "from work" in lowerT:
		potential = ["Wow, give me 10 minutes and I'll get back to you.",
						"I hate it when that happens... good thing you took pictures ;)",
						"You're *so* damn hot. Jeez.",
						"I'll bend you over your desk, if you want. :)",
						"I'll fuck you if you insist. ;)",
						"I can remedy this.",
						"I like your dangerous side. :D",
						"Would you be okay if I brought you the workplace delivery of my cock? ;)",
						"You have an incredibly gorgeous body.",
						"Hot.as.hell. Are you a secretary by any chance?",
						"I want to take you out to dinner, and then go see a romantic movie afterwards. I realize this isn't [1] /r/gentlemanboners but god damnit, you're actually beautiful. Not hot, not pretty, and not cute. Beautiful."]
		return (random.choice(potential), submission)
	return None


# If a submission is a self post in /r/BodyAcceptance(Only track this rule in /r/BodyAcceptance),
# give them the generic positive feedback they want. (Oh, they want it)
# This rule brought to you by: /u/1cerazor
def myFeels(submission, is_self, title, url, selftext):
	if is_self:
		# Only do this 10% of the time, so it's not so obviously a bot(/r/BodyAcceptance only gets 1-2 self posts per day, so this will not trigger very often)
		if random.randint(0,10) == 5:
			# I tried to make this list of responses as long as possible so people won't catch on quickly.
			responses = [
				"Just remember, you're perfect just the way you are.",
				"Everyone is beautiful, no matter what society might say.",
				"Why do people have to be so mean to others? What ever happened to just *accepting* each other?",
				"Just a message to everyone: Remember to love yourself all the time. It solves so many problems in life.",
				"Some people are just born different, seriously fuck what rude people say.",
				"We all have issues with our bodies, when will people just accept that and stop being assholes to each other all the time?",
				"I just want to remind everyone to love yourself :)",
				"You are beautiful. Seriously, don't ever feel shitty about the way you look ever again.",
				"Just love yourself. Everything else will fall into place I swear. :)",
				"Don't ever let anyone put you down - even yourself!",
			]
			return(random.choice(responses), submission)
	return None


# A program that answers simple questions with a Google search.
# This rule brought to you by: /u/braveathee
def searchongoogle(submission, is_self, title, url, selftext):
	shouldbeavoided = [
		"he",
		"it",
		"she",
		"you",
		"this",
		"that",
		"they",
		"those",
		"these",
		".",
		",",
	]
	if is_self and selftext == "" and title[-1] == '?':
		for word in shouldbeavoided:
			if word in title:
				return None
		replies = [
			"Have you tried to [google your question](http://google.com/#q=" + title + ") ?",
			"Have you [googled your question](http://google.com/#q=" + title + ") before asking ?",
			"You know that [Google exists](http://google.com/#q=" + title + "), right ?",
			"Maybe this [Google search](http://google.com/#q=" + title + ") will answer your question.",
			"I hope that this [Google search](http://google.com/#q=" + title + ") will answer your question.",
			"I have made [a Google search for your question](http://google.com/#q=" + title + "). I hope that its results will be helpful to you.",
			"[A Google search for your question.](http://google.com/#q=" + title + ") Maybe you will find a good answer there.",
		]

		return(random.choice(replies),submission)
	return None



######################## END BRAVERY RULES. ##########################
######################################################################





######################################################################
##################### BEGIN CONFIGURATION LISTS ######################


listOfRules = { #Rules to apply to comments.
	#leColby:"leColby",							#benned from Round 1
	#fuckYouOrFagResp:"fuckYouOrFagResp"		#benned from Round 1
	#notWTF:"notWTF",							#benned from Round 1
	#everyThread:"everyThread",					#culled from Round 1
	#navySealPasta:"navySealPasta",				#culled from Round 1
	#omgWhoTheHellCares:"omgWhoTheHellCares",	#culled from Round 1
	#EAIsHitler:"EAIsHitler",					#culled from Round 1
	#source:"source",							#culled from Round 1
	#checkYourPrivilege:"checkYourPrivilege"	#culled from Round 1
	oneTrueGod:"oneTrueGod",					#ROUND 1
	sarahJessicaParker:"sarahJessicaParker",
	murica:"murica",
	anneFrankly:"anneFrankly",
	atheismIsShit:"atheismIsShit",
	noWords:"noWords",
	thats_racist:"thats_racist",
	hello_timmie:"hello_timmie",
	randomPasta:"randomPasta",
	requestBravery:"requestBravery",

	badComments:"badComments",					#ROUND 2
	breadsticks:"breadsticks",
	penisEnlargementPill:"penisEnlargementPill",
	Hello:"Hello",
	alot:"alot",
	rwordexplainer:"rwordexplainer",
	winningArgument:"winningArgument",
	leSexual:"leSexual",
	ilovemales:"ilovemales",
	fuckYou:"fuckYou",
	botLogic:"botLogic",
	#mysonisgaybutChristian:"mysonisgaybutChristian",
	middleschool:"middleschool",
	sofuckingedgy:"sofuckingedgy",
	shamelessplug:"shamelessplug",
	Reddit:"Reddit",
	leXKCD:"leXKCD",
	gnu:"gnu",
	republicansAreEvil:"republicansAreEvil",
	leaking:"leaking",
}


listOfSubmissionRules = { #Rules to apply to submissions.
	#n_noHomo:"n_noHomo", 						#culled from Round 1
	selfPenisEnlargementPill:"selfPenisEnlargementPill", #ROUND 2
	bemygirlfriend:"bemygirlfriend",
	myFeels:"myFeels",
	searchongoogle:"searchongoogle",
}

# List of subreddits to check all rules in.
trackingSubreddits = [
	"test",
	"braveryjerk",
	"circlejerk",
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
]

# These subreddits will not be checked by any rules EXCEPT those which explicitly
# say so in subredditRestrictions.
specialSubreddits = [
	"gonewild",
	"BodyAcceptance",
]

# Every rule listed here will be applied only to comments or submissions in the
# subreddits listed next to it. Rules not listed here will be applied to all
# subreddits in trackingSubreddits.
subredditRestrictions = {
	bemygirlfriend:["gonewild"],
	myFeels:["BodyAcceptance"],
}


###################### END CONFIGURATION LISTS #######################
######################################################################






######################################################################
################## BEGIN DARK ATHEIST PYTHON MAGIC ###################

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

feederPlaceHolder = ""
file = open("feederPlaceHolder.txt")
for line in file.readlines():
	feederPlaceHolder = line
	break
file.close()

throttlingFactors = {}
file = open("throttlingFactors.txt")
for line in file.readlines():
	array = line.split()
	ruleName = array[0]
	tf = array[1]
	throttlingFactors[ruleName] = float(tf)
file.close()

for rule in listOfRules:
	ruleName = listOfRules[rule]
	if ruleName not in throttlingFactors: throttlingFactors[ruleName] = 1
for rule in listOfSubmissionRules:
	ruleName = listOfSubmissionRules[rule]
	if ruleName not in throttlingFactors: throttlingFactors[ruleName] = 1

feederThreadsWeveAnswered = []
feederRepliesWeveMade = []
file = open("feederHistory.txt")
lines = file.readlines()
feederThreadsWeveAnswered = lines[0].split()
feederRepliesWeveMade = lines[1].split()
file.close()







def dumpMemory():
	global placeHolders
	global submissionPlaceHolders
	global feederPlaceHolder

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

	file = open("feederPlaceHolder.txt","w")
	file.write(feederPlaceHolder)
	file.close()

	file = open("feederHistory.txt","w")
	file.write(string.join(feederThreadsWeveAnswered," "))
	file.write("\n")
	file.write(string.join(feederRepliesWeveMade," "))
	file.close()

	print "Memory successfully dumped."


def dumpThrottlingFactors():
	file = open("throttlingFactors.txt","w")
	file.write("")
	file.close()
	file = open("throttlingFactors.txt","a")
	for ruleName in throttlingFactors:
		file.write(ruleName+" "+str(throttlingFactors[ruleName]))
		file.write("\n")
	file.close()
	print "Throttling factors successfully dumped."



delayedComments = []
nextDelayedComments = []

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
	elif type(myReply).__name__ == "Submission":
		thread = myReply.id
	else:
		raise Exception("Error: myReply is of unknown type: "+type(myReply).__name__)

	if ruleFunction in listOfRules:
		threadsWeveRepliedTo[listOfRules[ruleFunction]].append(thread)
		repliesWeveMade[listOfRules[ruleFunction]].append(thread+"#"+myReply.id)
	elif ruleFunction in listOfSubmissionRules:
		threadsWeveRepliedTo[listOfSubmissionRules[ruleFunction]].append(thread)
		repliesWeveMade[listOfSubmissionRules[ruleFunction]].append(thread+"#"+myReply.id)
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
						if random.random() <= throttlingFactors[listOfRules[rule]]:
							implementedRule(comment,body)
				elif sr in specialSubreddits:
					if rule in subredditRestrictions and sr in subredditRestrictions[rule]:
						if random.random() <= throttlingFactors[listOfRules[rule]]:
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
						if random.random() <= throttlingFactors[listOfSubmissionRules[rule]]:
							implementedRule(submission,is_self,title,url,selftext)
				elif sr in specialSubreddits:
					if rule in subredditRestrictions and sr in subredditRestrictions[rule]:
						if random.random() <= throttlingFactors[listOfSubmissionRules[rule]]:
							implementedRule(submission,is_self,title,url,selftext)
				else:
					print "WARNING! THIS LINE SHOULD NEVER BE PRINTED!"

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
				if iscomment: x = linked_thing.reply(selftext)
				else: x = linked_thing.add_comment(selftext)

				permalink = x.permalink
				print "Successfully posted feeder comment:", permalink
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
			r.login(username="SOTB-bot", password=PASSWORD)
			y = submission.add_comment(callbackText)
			print "Posted callback:", y.permalink
			r.login(username=USERNAME, password=PASSWORD)
		except Exception, ex:
			print "Error in posting callback. User's out of luck; there's nothing else we can do.", ex
		finally:
			r.login(username=USERNAME, password=PASSWORD)
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






user_agent = "Bravery bot 2.0 by /u/VULGARITY_IN_ALLCAPS"
r = praw.Reddit(user_agent=user_agent)
r.login(username=USERNAME, password=PASSWORD)



# Before we start, update the throttlingFactors based on the karma totals,
# not from the previous day, but from the day before that.
#"""
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
implementedRules =           [(rule,implementRule(rule))           for rule in listOfRules]
implementedSubmissionRules = [(rule,implementSubmissionRule(rule)) for rule in listOfSubmissionRules]
startTime = time.time()

#Go!
while True:
	print "Start loop."

	try:
		feeder = r.get_subreddit("SurvivalOfTheBravest")
		posts = feeder.get_new(place_holder=feederPlaceHolder,limit=40)
		postsList = [s for s in posts]

		feederPlaceHolder = postsList[0].id
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
		checkSubreddit(sr)
	for sr in specialSubreddits:
		checkSubreddit(sr)

	print "Checking submissions:"
	for sr in trackingSubreddits:
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


	print "Done applying rules."



	print "Sleeping..."
	time.sleep(60)

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

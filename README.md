survivalofthebravest
====================

***THE ENGLISH MAJOR'S GUIDE TO WRITING BRAVERY RULES***
(lel, DAE STEM?)

This bot is written in Python.
We've tried to handle all the dirty work so you can do what you
 do best: BRAVERY.

A Bravery Rule is a function that takes as input a Reddit
 comment (`comment`) and its text (`body`).
It then has to decide what to do with it.
This decision is expressed in a RETURN STATEMENT: a line of code
 that says "return [something]"
In most cases, you're going to want to do nothing. For this, say:

	return None

What if you want to make a comment in response? Then, your return
 statement will look like:

	return (textOfYourReply, thingToReplyTo)

For example, the following:

	return ("SO BRAVE", comment)

replies with "SO BRAVE" to the comment we're currently looking at.
In most cases, the thingToReplyTo is going to be simply `comment`,
 because we want to reply to the same comment that we just read.
(But this doesn't always have to be the case.)
If there's more than one return statement, the one that is reached
 first will rule.

This bot uses the Python Reddit API Wrapper (PRAW) module to
 communicate with Reddit.
For more information about PRAW, see:
 http://github.com/praw-dev/praw/wiki
In particular, this documentation tells you how to access
 information about the comment, such as:

	comment.author	(the user who wrote it)

The easiest way to get started is to just copy the existing examples
 and modify them till they do what you want.

GO AHEAD, 420 CODE IT FAGGET

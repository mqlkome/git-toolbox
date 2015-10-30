##This file is for learning about GIT!
from random import randint

#Mostly it is print statements
print "hello! " + "a short python program"

#there are also random numbers happening
x = randint(0,5)
print x

print "another small change"

y = randint(0,5)
print x-y

#We also have some probability happening
if x == 3 or y == 3:
	print "both were three! what's the chance of that?"
	chance = (1.0/6.0)*(1.0/6.0)
	print "chance = " + str(chance)
if x > y:
	print "x was greater than y! what's the chance of that?"
	print "chance = figure it out yourself I'm busy"


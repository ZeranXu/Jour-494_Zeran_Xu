# opening files
# r for read, a for append, w for overwrite

"""
f = open ("gettysburg.txt", "a")

print (t.read())

f.write("TEST ONE TWO THREE")

f.close()

"""

# Conditions
## if statements

"""
a = 5
b = 7
if a==b: #(condition)
	print ("a is same as b") # instruction
else:
	print ("a is not same as b") # instruction
"""

"""
fruits = ["orange", "apple", "watermelon"]
veggies = ["cucumber", "squash", "onion"]

x = "strawberry"

if x in fruits:
	print (x+" is a fruit")
elif x in veggies:
	print (f"{x} is a vegetable")
else:
	print (f"{x} is not a fruit or a vegetable")
"""

# For loops to iterate through the fruits list

"""
fruits = ["orange", "apple", "watermelon"]
for f in fruits:
	print (f+ "is a fruit")
"""

"""
# loop through a list and write
e = open ("example", "w")
fruits = ["orange", "apple", "watermelon"]

e.writelines(f for f in fruits)
"""

"""
# Combine loops and if statements 
numbers = [1,2,3,4,5,6]

for n in numbers:
	if n > 3:
		print (f"{n} number is greater than 3")
	elif n < 3:
		print (f"{n} number is less than 3")
	else:
		print (f"{n} number is 3")
"""

#Functions
#def myFunction():
#print ("helloworld") (it's not work, beacuse function does not run unless called)
# just use "myFunction()"

# defining a function with a parameter

"""
def callout(x):
	print (f"hello {x}!")

# calling the function
callout("William")
callout("Iris")
"""

"""
def greetings(x,y,z):

	s = f"Are you {x}?" 
	b = f"Are you {y}?"
	aa = f"Hello {x} and {y}."
	bb = f"Hello {x} and {y} and {z}."
	print (s)
	print (b)
	print (aa)
	print (bb)

greetings ("Bob", "Rob", "William")
"""


# how many words are in the gettysburg address?

"""
g = open("gettysburg.txt", "r")

# read the file
text = g.read()

# split the string into a list, divided by space
words = text.split()

# get the length of the list of words
words_length = len(words)

print(words_length)
"""

# How many articles are in the gettysburg address?

"""
g = open("gettysburg.txt", "r")
text = g.read()
words = text.split()
words_length = len(words)
"""

"""
article = ["a", "an", "the"]
n=0

for w in words:
	if w in article:
	    n = n+1 # add one to n and set it as n
	    print (n)
"""
"""
articles = ["a", "the", "an"]
empty = []
for w in words:
	if w in articles:
		# add that article to the empty list
	    empty.append(w)
print (empty)
print (len(empty))

# how many of each article is in gettysburg address?
words_list = {"a":0, "an":0, "the":0}
print(words_list)
for w in words:
	if w.lower() in articles:
		words_list[w.lower()] = words_list[w.lower()]+1
print (words_list)
"""

"""
def articleCounter(x):
	t = open(x,"r")
	
	text = t.read()

	words = text.split()

	articles = ["a","an","the"]
	words_list = {"a":0,"an":0,"the":0}

	for w in words:
		if w.lower() in articles:
			words_list[w.lower()] = words_list[w.lower()]+1

	print (words_list)

articleCounter("gettysburg.txt") # put the file name in "" to open or caculate any file.
"""
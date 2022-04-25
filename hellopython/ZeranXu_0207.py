# Task 1: five variables with fruits/vegetables after 5 containers

menu = "spinach" 
# named a varible as a kind of fruit or vegetables and stored as strings
print ("The vegetarian menu contains the " + menu)
# stored and print strings after a container

box = "watermelon"
print ("The fruit box contains a " + box)

bucket = "buleberries"
print ( "In the bucket, there are some " + bucket)

pocket = "raspberries"
print ("The gift pocket consists of some " + pocket)

case = "bananas"
print ("The fruit case has some " + case)


# Task 2: store all the sentence and quotes in a variable called "sentence"

sentance = "Kalvan said that producers have \"called my agent asking, \'Why you should repesent this guy?\' Any thing that lowers your odds is going to hurt.\""
# Set words and quotes in the variable "sentence"
print (sentance) 
# print variable


# Task 3: create a list called "president" with 5 names

presidents = ["George Washington", "John Adams", "Thomas Jefferson", "James Madison", "James Monroe"]
# set 5 American presidents name in the list "presidents"
print (presidents) 
# print the list "presidents"


#Task 4: create another list called "birthyears"

birthyears = [1789, 1797, 1801, 1809, 1817] 
# set 5 American presidents' birthyears in the list "birthyears"
print (birthyears) 
# print the list "birthyears"


#Task 5: create a dictionary called "p_data"

p_data = {"George Washington": 1789, "John Adams":1797, "Thomas Jefferson":1801, "James Madison":1809, "James Monroe":1817} 
# Generated dictionary with presidents' name and birthyears, and structured as "president name": matched brithyear
print(p_data)
# print dictionary


"""
Another way to use "zip" for Taks 5
p_data2  = dict (zip(president, birthyears))
print(p_data2)
"""



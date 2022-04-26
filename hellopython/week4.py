#print ("hello world")

#string data type
trojan = "She said \"hello world\""

#integer data type
gold = 789
red = 230

# type() asks what type of data a variable is
datatype = type(gold)

"""
boolean varible (True/False)
Ask if gold is same as red, 
and saving it in the compare varible
"""

compare = (gold == red)

# print(compare)

#len() gets the length of a variable

str_len = len(trojan)

#print (trojan)

#how to combine strings

one = "Here is "
two = "how to"
three = " combine."


#print(one + two + three)
#print (one + "my computer.")
#f-string example

#print (f"{one}my computer.")
#computer = 25
#print (computer)






# string operations

#cookies = "thorugh it, girls learn five essentials skills"
#print (cookies)

# replace grils with students
#cookies = cookies.replace("girls","students")

#print(cookies)

# split cookies on the space
#split_cookies = cookies.split(",")

# print (split_cookies)















# lists and dictionaries

box = ["a","sample","list","of","strings","and",500]

box.append("!")

len_list = len(box)

#---len:计算一个数列中的个数


#get the first item on the list (in python order starts at 0)
first = box[0]

#print(len_list)
#print(first)

#get the last item
last = box[-1]

#get items in between 1-4, includes 1, excludes 4
between = box[3:4]

#dictionaries are key, values paris
fire = {1:"welcome", 2:2, 3:"class"}

#get value by key
value = fire[3]

# print (value)

# reading and writing files
# r = read, a = append, w=write

f = open("gettysburg.txt","r") #open a file
text = f.read() #read that file

print(text)

#write a file

#w = open("example.txt", "w") 
#w.write("hello world!") # is . means opreation? like print?
#w.close()

#append to existing file
e = open("example.txt", "a")

e.write("hello again!")

e.close








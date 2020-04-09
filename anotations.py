# Some Python Introduction

#Some Strings manipulations type

string = 'Batiman fazendo batmisse'
strUp = string.upper() ## Uppercase
strStride = string[::2] #Get te every 2 positions of a string
strSlice = string[0:5:2] #Slice picks up every second element in the range 0 to 4
Numbers="0123456"
strEven = Numbers[::2] # obtain the even elements

print(Numbers.find('1')) # find a pattern

###Lists and Tuples###

#Tuples are and ordered sequence like Ratings = (10,9,6,5,10,8,9,6,2)
#Tuple can contain tuple1= ('disco,1,1.4) strings, floats, integers
#Tuples are immutables
#Tuples can contain other tuples, like : NT = (1,2,("pop","rock"),(3,4),("disco,(1,2")))
#They are called NESTING
#NESTINGS can be access by indexing
#We can concatenate or combine tuples by using the + sign:

# Concatenate two tuples
​
tuple2 = tuple1 + ("hard rock", 10)
tuple2

##List's are the same, but mutables

L = ["Michael jackson", 10.1, 1982]
L.extend(["pop",10]) ###extends adds the new elements one by one
##expected result :
#L = ["Michael jackson", 10.1, 1982,"pop",10]
L.append(["pop",10]) ### This adds the following list into one position 
##expected result :
#L = ["Michael jackson", 10.1, 1982,["pop",10]]

##CLONE LIST##
A = ["hsrd rock",10,10.3]
B = A[:] #clone
 

C = ["a","b","c"]
print(C[1:])


###SETS#######
#unlike lists and tuples they are unordered
#they not record the elements position
#set ={"pop","rock","soul","rock"}#when the set is created he not allows duplicate elements like "rock"
#they have some really good methods like "&" to discover the intersection between two sets
#"diference" to discover the diferences between 2 sets
#"intersection" the name explains for himself

###DICTIONARIES###
##they are a collection type


###LOOPS###
##Types of index FOR

listColors = ["Red","Violet","Orange","Black", "Seafom Green"]

for i in range(len(listColors)):##In range type 1

for colors in listColors: #Type 2 Will pick every index values like "Red" and "Violet"

for index, colors in enumerate(listColors): # @ parameter i can pick the index and the value of each position of the list

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

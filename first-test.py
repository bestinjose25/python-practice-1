#print("hello")

"""
print("hello")
print("hello")
print("hello")
print("hello")
"""
from dataclasses import asdict

#######
a=["cherry", "rose", "greenpeas"]

print(a[1]) # list

b=("cherry", "rose", "greenpeas")

print(b[0]) #tuple

c={"cherry", "rose", "greenpeas"}

#print(c{2})  #set
#########


######
intA=123
floatA=123e2  # e means 10th postion is added, ie e2 means 00 added, e5 means 00000 is added
complexA=23j

print(intA)
print(floatA)
print(complexA)

######




#####random , to pick random number from a specific range
import random

print(random.randrange(20, 35))


#####random


#####string
stringB ="Hallo, wie gehts?"
print(stringB[7])

stringC="One girl is sitting near me, her name is gopika"
print(stringC[1:20:2]) # here the last one indicates to skip  words
#####string


asd= "hallo guys, how are you?"
if "hallo" in asd :
    print("yes, there is hallo")
else:
    print("no, there is no hallo")


print(asd[-10:-4])



name="beStin Jose "

print(name.strip()) #remove white sapce from the begining and ending

print(name.replace("n","y"))

ageOfBestin=25;
print(name+ f"is {ageOfBestin}")

priceOfProduct=456
print(f"price of product is  \n* {priceOfProduct:.2f}")  #4f represent decimal points


#print(name.center())



listA=["apple","banana", "grape", "orange", "carrot", "betroot"]

#listA[1]="orange"
listA[1:4] = "spinach","cabbage","coliflour"
print(listA)



print(listA[-3:-1])
if "orange"  in listA:
    print("no")


tupleA = ("boys","girls","trans")
#tupleA(3,"man") # we cannot add or remove from a tuple
print(tupleA)



floatB=.5e4
print(floatB)


#need to use specail character

stringB=r"I\t bestin" #if we user infront of the string then \t will not work
print(stringB)

abc='sgag'
print(abc.upper())
print(abc.count("s"))





snowball = "I made myself a snowball\nAs perfect as could be.\nI thought I'd keep it as a pet\nAnd let it sleep with me.\nI made it some pajamas\nAnd a pillow for its head.\nThen last night it ran away,\nBut first it wet the bed."

#1)How many the word it does the poem have? --> Store the output in a variable called it_count

it_count=snowball.count("it")
print(it_count)

#2)How many characters in the poem, including the spaces and punctuations? --> Store the output in a variable called len_poem

len_poem=len(snowball)
print(len_poem)

#3)Where is the first occurrence for the word it? --> Store the output in a variable called it_first

it_first = snowball.index("it")
print(it_first)

#4)Where is the last occurrence for the word I? --> Store the output in a variable called I_last

I_last=snowball.rfind("I")
print(I_last)




# txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
# #numbered indexes:
# txt2 = "My name is {0}, I'm {1}".format("John",36)
# #empty placeholders:
# txt3 = "My name is {}, I'm {}".format("John",36)
#
# print(txt1)
# print(txt2)
# print(txt3)

#-----format function------
bioBes="his name is {vorname} {nachname} and he lives in {ort}".format(vorname="Bestin", nachname="Jose", ort="Kochi")
print(bioBes)
bioBes1="his name is {0} {1} and he lives in {2} and he is {3} of age"
formatTry1=bioBes1.format("Bestin", "Jose", "Kochi",25)
print(formatTry1)

bioBes2="his name is {} {} and he lives in {} and he is {} of age and he is still unmarried".format("Bestin", "Jose", "Kochi",25)

print(bioBes2)
#-----format function------

welcome=input("please enter the message\n")
#print(welcome)

inputName=input("please enter a letter to get the count\n")
#print(inputName)


lenthOfLetter=welcome.count(inputName)
print(f"Count of the let    ter in the message is {lenthOfLetter}")

lengthOfWelcome=(len(welcome))
percent=(lenthOfLetter)/(lengthOfWelcome)*100
#print(percent)

print(welcome)
#print(letterOne)
print(lenthOfLetter)
print(percent)




print("" == False) #these checks the empty string is equal to the boolean, but this always reslts False because boolean can't be compared with any OTHER DATA TYEPS
print("afhkjaf" == True) # results false because of the different data type
print(bool("")) #this results false
print(bool("")==False) #this results True, because 'bool("") results false, and then checks false == false' , so results true


print(id(welcome))   # this results the 'variable storage ID'  for the WELCOME variable


#------idenity operator
asdf=30
dfgh=30
print(asdf is dfgh) # 'is' is an identity operator
print(id(asdf) , id(dfgh)) # storage ID between the integer -5 to 256 has the same ID but more than or else than that have different ID

asdf1=301
dfgh1=302
print(asdf1 is dfgh1)
print(id(asdf1) , id(dfgh1)) # storage ID between the integer -5 to 256 has the same ID but more than or else than that have different ID

#------idenity operator

#membership operator
qwe="bestin"
qwer="bestin jose"
print(qwe in qwer)

#membership operator


# ------bitwise   operator  - binary number operation

bitA= 6
bitB= 2

print(bin(bitA), bin(bitB)) # bin is used to convert integer to binary
                            #110 binary of 6
                            #010 binary of 2
                            #---
                            #110 - that is binary of 6

bitC = bitA|bitB  # this is bitwise OR operator , here this opertor ADD the BINARY of bitA and bitB and store in bitC
print(bitC)


bitD = bitA&bitB  # here bitwise AND operator, here this is substracted that is
print(bitD)    #110 binary of 6
               #010 binary of 2
               #---
               #010 - that is binary of 2

print(~bitA)  # bitwise not
#bitA is 6(110) and bitwise not results in -7(-111  that means negative is added and one position is shifted and added a binary 1)


print(bitA^bitB) # bitwise XOR operation
                # 110 binary of 6
                # 010 binary of 2
                # ---
                # 100 - that is binary of 4 (XOR means odd one then one ie, 1 - 0 => 1, 1 -1 => 0 , 0 - 0 => 0)

# ------bitwise   operator  - binary number operation



#----List---

list_quiz = [ 100 , 30 , 2 , 15 , -4 , 3 , 40 , -9 , 10]

#values in between
last_4=list_quiz[5:10]
print(last_4)
#largest value
max_val=max(list_quiz)
print(max_val)

# Descending order sorting
print(sorted(list_quiz, reverse=True))

# to sort list there are two function sort() and sorted(),
# sort() - it will sort and store in the same list itself and sort() can only be used for list sorting
# sorted() - it will create another sorting list and will provide the sorting list , it can be used for any like tuple, dict ...





#----List---

# tuple----

tupleB=(1,2, "hello", "ladsfjlj",6) # tuple is immutable and cannot be edited
print(tupleB)
# tuple----



# set----

setB={1,2, "hello", "ladsfjlj",6} # set is mutable and does not have indexing
setB.add(10)
print(setB)

setB.pop()
print(setB)
# set----


# dictionary----

dictB={"name":["babu","john", "haseel"], "id":[2,7,9], "age":[25,27,25], "profession":["Engineer","Doctor","Clerk"], "name":["appu","mahin", "kadhar"]}
#dictionary doesnot have idexing but can be retrieved onylwith the key, and this key will be unique
# if the same key is in the dictionary then the latest key will replace the oldest key and its values, there is "name" key replaced with the newest one
print(dictB)
print(dictB.get("idee")) # to get the value of a key

print("id" in dictB) # key can be searched to find

# dictionary----


sampleList=["abc", {"me":"bestin"}, [1],(1,"hai")]
print(sampleList[1])

# dictionary----


sampleList=["abc",{"me":"bestin"}, [1],{"you": "abdul", "him":"who","come":["willkommen"]},(1,"hai")]
print(sampleList[3]["come"])


sampleDict={"abc": [{"me":"bestin"}, [[1],{"you": "abdul", "him":"who","come":["willkommen"]},(1,"hai")]]}
print(sampleDict.get("abc"))


dictAdd={"fruit": ["apple","orange","grape"],2:"name"} #creating dict

dictAdd[3]="place" #adding dict
print(dictAdd)

dictAdd["address"]=["Kmgm", "muvtpza", "ekm"] #adding dict
print(dictAdd)

dictAdd[3]="Ort"  # replacing dict value
print(dictAdd)

del dictAdd[3]  # to delete an item b key

abcd=dictAdd.pop(2)  # to delete using pop()
print(dictAdd)
print(abcd)



# if ----


ifX=int(input("enter the first number\t"))
ifY=int(input("enter the second number\t"))
if ifX==ifY:
    print(f"both {ifX} and {ifY} both are same")

elif ifX>ifY:
    print(ifX, "is the biggest value")
else:
    print(ifY, "is the biggest value")

# if ----

# for loop
listC=["just as it is","Hello welcome back", 59,["Go to hell"]]

if ["Go to hell"] in listC:
    print("Yes")
else:
    print("No")

for char in listC:  # we can assign any name and thst that name can be printed , same like i value for iteration
    print(char)

for i in range(0,20,3):  # 0 to 20 will be printed with a gap of 3,ie: 0,3,6,9.....18
    print(i)


dict_quiz = { 1 : 10 , 20 : 5 , 3 : 2 }
for i in dict_quiz:
    print(i)  # for dictionary printing , we print only the key values ie 1 20 3 and not the values of the key



for i in range (1, 10,2):   #for loop pyramid
    for j in range (1,i+1,2):
        print(j,end=" ")
    print(end="\n")
    print("Haii am i")


# for loop

#while loop---
# basic syntax of while
ii=1;   # initalisation
while ii<9:  # condtion checking
    print(i)
    i+=1     # incrementation

#while loop---


#break----

for i in range(1,4) :
    print(i)
    print(i,"it is for loop")
    if(i==3):
        print("9 reached in and now in the if loop, for-if loop")
    for j in range(10,14):
        print(j,"in the for- for loop")
        if (j==13):
            print("it is in the for-for-if")
            break
        break
    print("im in the last of for loop")


web_list = [ "start" , 10313 , 1415 , "afvav", "vbagaga", "mid", 3.415, {"A":12121}, {"xava":11} , 1.21, "end"]

index=0
list_length=len(web_list)
val =web_list[0]
while index<=list_length:
    if(web_list[index]=="end"):
        print("Found them! Stop the code!")
        break
    else:
        print("Not yet. Still searching..")
    index+=1


#break----

# continue-----


listCont=[2,3,"hello", "Don't read just skip this", "read me please", 8, 5]

for element in listCont:
    if element =="Don't read just skip this":
        continue
    print(element) # here the iteration will continue and skipped ""Don't read just skip this"", this line is skipped and remaining iteration are working fine.

# continue-----

# to add select onyl even numbers and add to another list
list_ages = [10 , 11 , 19 , 7 , 8 , 24 , 91 , 74 , 25 , 53 , 41 , 50 , 63 , 86]
ages_even = []
len=len(list_ages)
for i in range(0,len):
    if list_ages[i]%2==0:
        ages_even.append(list_ages[i])
print(ages_even)




#zip function--------

listOne =[2,3,4]
listTwo =[5,6,7]

zipList=zip(listOne,listTwo)  # to convert list to zip

listCreate=list(zipList)  # zip will be created as an object and we need to change this object to any other data type, like list, set etc....
print(listCreate)  # result will be [(2,5),(3,6),(4,7)]




list_quiz = [ 1, 2, 10 , 5]
dict_quiz = { "quiz": 3 , 4 : 9}
tuple_quiz = (6 , 8 , 12 )
for x,y,z in zip(list_quiz, dict_quiz , tuple_quiz):  # using for loop
     print(x,y,z)  # If the lists are uneven, zip() stops at the shortest one

#zip function--------
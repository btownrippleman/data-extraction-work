import random, os, sys


# This string literal contains all lowercase ASCII letters.


letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "!@#$%^&*()_+"

elementsHashMap = {

"letters" : letters,
"numbers" : numbers,
"upperCase" : upperCase,
"symbols" : symbols,

}


outputString = ""
elementsChosen = ""
if len(sys.argv) < 2:
	endrange = 15
else:
	endrange = int(sys.argv[1])


lowvals = ["L","U","N","S"]

if lowvals[0] in sys.argv[2:] or lowvals[1] in sys.argv[2:] or lowvals[2] in sys.argv[2:] or lowvals[3] in sys.argv[2:]:

	print("argvals in sys.argv")


	if "L" in sys.argv[2:]:
		del elementsHashMap['letters']

	if "N" in sys.argv[2:]:
		del elementsHashMap['numbers']

	if "U" in sys.argv[2:]:
		del elementsHashMap['upperCase']

	if "S" in sys.argv[2:]:
		del elementsHashMap['symbols']

lowvals = ["l","u","n","s"]

if lowvals[0] in sys.argv[2:] or lowvals[1] in sys.argv[2:] or lowvals[2] in sys.argv[2:] or lowvals[3] in sys.argv[2:]:
	print("if l u n s in sys.argv[2:]:")
	elementsHashMap = {}
	print("elementsHashMap ="+ str(elementsHashMap))
	
	if "l" in sys.argv[2:]:
		elementsHashMap["letters"] = letters

	
	if "u" in sys.argv[2:]:
		elementsHashMap["upperCase"] = upperCase

	
	if "n" in sys.argv[2:]:
		elementsHashMap["numbers"] = numbers

	
	if "s" in sys.argv[2:]:
		elementsHashMap["symbols"] = symbols


print(elementsHashMap)





for i in elementsHashMap:
	elementsChosen = elementsChosen + str(elementsHashMap[i])
	




for i in range (0, endrange): # random.choice returns a random character.
    l = random.choice(elementsChosen)
    outputString = outputString+l
print (outputString)


#***** only works in linux\
# and must have xclip installed
os.system("echo -n \""+outputString+"\" | xclip -selection clipboard")






#next time you want to make this a permanent command just add the line 

#export $makepassword ="python /path/to/this/file"

#to the end of .bashrc file in home directory


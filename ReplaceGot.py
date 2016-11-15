#This script replaces get,getting, got, gotten with 'obtain', 'derive'

string = "I need to get a new phone. I got that one too. I will be getting one."
ssplit = string.split()
L = list()

for word in ssplit:
	L.append(word)

for word in L:
	index = L.index(word)
	if ("getting" in word):
		L[index] = "obtaining"
	elif(word == "get"):
		L[index] = "obtain"
	elif(word == "got" or word == "gotten"):
		L[index] = "obtained"
newSentence = ' '.join(L)
print "Old string: \n" + string
print "New string: \n" + newSentence
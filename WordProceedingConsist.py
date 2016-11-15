#This script takes a string. If the word consist is not followed by 'of', it replaces the next word with

string = "It consists in, consisting in, should consist as"
ssplit = string.split()
L = list()
for word in ssplit:
	L.append(word)

for word in L:
	if word == "consist" or word == "consists" or word == "consisting":
		indexOfwordAfter = L.index(word) + 1;
		if(L[indexOfwordAfter] != "of"):
			L[indexOfwordAfter] = "of"

		newSentence = ' '.join(L)
print "Old string: \n" + string
print "New string: \n" + newSentence



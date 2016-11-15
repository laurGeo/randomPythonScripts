#This script takes a string. If the word participate is not followed by 'in', it replaces the next word with

string = "I will participate at this. Participating of that. She participates at events."
ssplit = string.split()
L = list()
for word in ssplit:
	L.append(word)

for word in L:
	if word == "participate" or word == "participates" or word == "Participating":
		indexOfwordAfter = L.index(word) + 1;
		if(L[indexOfwordAfter] != "in"):
			L[indexOfwordAfter] = "in"

		newSentence = ' '.join(L)
print "Old string: \n" + string
print "New string: \n" + newSentence



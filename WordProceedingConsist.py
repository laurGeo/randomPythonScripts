#This script takes a string. If the word consist is not followed by 'of', it replaces the next word with

string = "It should consist in"
ssplit = string.split()
L = list()
for word in ssplit:
	L.append(word)

for word in L:
	if word == "consist":
		indexOfwordAfter = L.index(word) + 1;
		if(L[indexOfwordAfter] != "of"):
			L[indexOfwordAfter] = "of"
			print "New sentence is now: "
			print ' '.join(L)

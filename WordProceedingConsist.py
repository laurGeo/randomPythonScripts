#This script takes a string. If the word consist is not followed by 'of', it replaces the next word with
def WordProceedingConsistFunc(str):
	ssplit = str.split()
	L = list()
	for word in ssplit:
		L.append(word)

	for word in L:
		if word == "consist" or word == "consists" or word == "consisting" or word == "consisted":
			indexOfwordAfter = L.index(word) + 1;
			if(L[indexOfwordAfter] != "of"):
				L[indexOfwordAfter] = "of"

			newSentence = ' '.join(L)

	print "Old string: \n" + str
	print "New string: \n" + newSentence


WordProceedingConsistFunc("consist in")



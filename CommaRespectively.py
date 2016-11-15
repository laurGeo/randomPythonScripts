string = "Average sentence length for English and French being 22 and 24 words respectively."
ssplit = string.split()
L = list()
for word in ssplit:
	L.append(word)

for word in L:
	#Does the word 'respectively' appear in any of the words (taking into account punctuation)
	if("respectively" in word):
		indexOfwordBefore = L.index(word) -1;
		if L[indexOfwordBefore][-1:] != ",":
			L[indexOfwordBefore] += ","

newSentence= ' '.join(L)
print "Old string: \n" + string;
print "New string: \n" + newSentence;
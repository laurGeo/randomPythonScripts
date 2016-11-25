#WordFunctions.py
#applyRules applies all the rules in this WordFunctions.py file
def applyRules(textData, filename):
	print textData
	newFile = open(filename, 'r+')
	textData = replaceGot(textData)
	#print textData
	textData = WordProceedingConsistFunc(textData)
	#print textData
	textData = WordProceedingParticipate(textData)
	#print textData
	textData = CommaRespectively(textData)
	print textData

	#Only write the data to the file once.
	newFile.write(textData)
	newFile.close()



def replaceGot(textData):
	ssplit = textData.split()
	L = list()

	for word in ssplit:
		L.append(word)

	for word in L:
		index = L.index(word)
		if ("getting" in word):
			L[index] = "obtaining"
		elif(word == "get" or word == "Get"):
			L[index] = "obtain"
		elif(word == "got" or word == "gotten" or word == "Got" or word == "Gotten"):
			L[index] = "obtained"
	newSentence = ' '.join(L)
	#print "Old string: \n" + textData
	#print "New string: \n" + newSentence
	return newSentence

#Rule7
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

	return newSentence

#Rule8
#This script takes a string. If the word participate is not followed by 'in', it replaces the next word with
def WordProceedingParticipate(textData):
	
	ssplit = textData.split()
	L = list()
	for word in ssplit:
		L.append(word)

	for word in L:
		if word == "participate" or word == "participates" or word == "Participating" or word == "participated":
			indexOfwordAfter = L.index(word) + 1;
			if(L[indexOfwordAfter] != "in"):
				L[indexOfwordAfter] = "in"

	newSentence = ' '.join(L)

	return newSentence

#Rule14
#This script puts a comma before any word that preceeds the word 'respectively'.
def CommaRespectively(textData):
	ssplit = textData.split()
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
	return newSentence




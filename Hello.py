import WordFunctions

#Take the user given file
oldFile = open('text.txt', 'r')

#Read it into fileData. Store original in the 'oldFile' file.
fileData = oldFile.read()
oldFile = open('oldFile', "w")
oldFile.write(fileData)
oldFile.close()

#Apply all the rules
WordFunctions.applyRules(fileData, 'text.txt')
#newFile = open('text.txt', 'w')



import os
import re
os.getcwd()
os.chdir('C:\\Users\\ASUS\\PycharmProjects\\pythonProject3')

openText= open("mrMiyagi.txt","r") #open the txt and read
readText= openText.read()
openText.close()

upperCase="([A-Z])" # from line 10-16 is the variabel that will appear in the text
lowerCase="([a-z])"
sampleTitles="(Mr|St|Mrs|Ms|Dr)[.]"
periodsInternal = "[.](com|net|org|io|gov)"
suffixes = "(Inc|Ltd|Jr|Sr|Co)"
other = "(i)[.](e)[.]"
digits="([0-9])"

editText= readText.replace("\n"," ") #replace line with space
#avoids splitting in each grouping
editText= re.sub(sampleTitles,"\\1<prd>",editText) 
editText= re.sub(periodsInternal,"<prd>\\1",editText)
editText= re.sub(""+suffixes+"[.]","\\1",editText)
editText= re.sub("[.]"+digits,"<prd>\\1",editText)
editText= re.sub(other,"i<prd>e<prd>",editText)

#add stop and replace it with certain symbols
editText= editText.replace("...","<prd><prd><prd><stop>")
editText= editText.replace(".",".<stop>")
editText= editText.replace("?","?<stop>")
editText= editText.replace("!","!<stop>")
editText= editText.replace("<prd>", ".")


splitSentence = editText.split("<stop>")
splitSentence = [sentence.strip() for sentence in splitSentence]

print(*splitSentence,sep="\n")


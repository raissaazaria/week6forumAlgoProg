file =open("myVacation.txt","r") #open text file that have the original text and use r to read the whole text
myList = file.readlines() #use readlines to returns into a list

count = 1 # start adding from number one and not 0
newList=[] # add empt list
for line in myList:
    count = count + 1 #for each new line, plus 1
    formula = "{} {}".format(count,line) #add the formula into the new text
    newList.append(formula) #append into new text

newListIntoStr= " ".join([str(list)for list in newList]) #transform the list into string, because newFile.write doesnt accept list

newFile=open("myVacationResult.txt","w") #open the empty file to write the result
newFile.write(newListIntoStr) #use the one that we have alr transform to list
file.close() #close file

file =open("myVacation.txt","r")
myList = file.readlines()

count = 1
newList=[] # add list
for line in myList:
    count = count + 1
    formula = "{} {}".format(count,line)
    newList.append(formula)

newListIntoStr= " ".join([str(list)for list in newList]) # here u have to basically transform the list into string, because newFile.write doesnt accept list

newFile=open("myVacationResult.txt","w")
newFile.write(newListIntoStr)
file.close()
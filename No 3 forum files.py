file= open("plainText.txt","r") #open the text and read
content = file.read()
splitWords=content.split() #split the word in content file

wordTokenLength = sum(len(word)for word in content.split()) #sum the length of the word lin content.split
wordToken =len(content.split()) #basically it just couunt the length in content.spliy
wordLength = wordTokenLength/wordToken #the formula of the word length is the total of wordTokenLength divided with wordToken

print("The average word length of the text is" ,round(wordLength,2)) #print the word and enter the wordLength with the rounding so it will not be full
file.close()

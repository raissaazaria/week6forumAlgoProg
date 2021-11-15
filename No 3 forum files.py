file= open("plainText.txt","r")
content = file.read()
splitWords=content.split()

wordTokenLength = sum(len(word)for word in content.split())
wordToken =len(content.split())
wordLength = wordTokenLength/wordToken

print("The average word length of the text is" ,round(wordLength,2))
file.close()
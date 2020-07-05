#Write code that will print out the anagrams (words that use the same
#letters) from a paragraph of text.
paragraph=str(input("Enter your paragraph"))
words=list(paragraph.split(" "))
li = []
for a in words: 
    for b in words: 
        if a!= b and (sorted(a)==sorted(b)):
            li.append(a)
print('The anagrams in the given sentences are',list(set(li)))
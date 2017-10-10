import re

text = ''.join(open('brown-test.txt').readlines())
sentences = re.split(r' *[\.\?!][\'"\)\]]* *', text)
list = []
for s in sentences :
    list.append('<s>'+" " + s + " " + '</s>' + " ")
#print(list)
article = [s.lower() for s in list]
#print(list2)

dict = {}

for s in article :
    for c in s.split() :
        if c in dict :
            dict[c] += 1
        else :
            dict[c] = 1
print(dict)


#print(article)
newArticle = []
for s in article :
    for c in s.split() :
        if c in dict and dict[c] == 1 :
            newArticle.append(s.replace(c,"<unk>"))
        else :
            newArticle.append(s)

print(newArticle)

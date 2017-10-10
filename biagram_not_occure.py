import re
from languagePreProcessing import newArticle
#Q4
#clean brown-test
docName = "brown-test.txt"
text = ''.join(open(docName).readlines())
sentences = re.split(r' *[\.\?!][\'"\)\]]* *', text)
list = []
for s in sentences :
    list.append('<s>'+" " + s + " " + '</s>' + " ")
#print(list)
brown_test = [s.lower() for s in list]
#print(list2)

dictBrownTest = {}

brownTestOriginalTotalWord = 0
for s in brown_test :
    for c in s.split() :
        brownTestOriginalTotalWord += 1
        if c in dictBrownTest :
            dictBrownTest[c] += 1
        else :
            dictBrownTest[c] = 1

brownTestArticle = []
for s in brown_test :
    for c in s.split() :
        if c in dictBrownTest and dictBrownTest[c] == 1 :
            #print(s)
            brownTestArticle.append(c.replace(c,"<unk>"))
            #print(s.replace(c,"<unk>"))
        else :
            brownTestArticle.append(c)

#print(brownTestArticle)
docName = "learner-test.txt"
text = ''.join(open(docName).readlines())
sentences = re.split(r' *[\.\?!][\'"\)\]]* *', text)
list = []
for s in sentences :
    list.append('<s>'+" " + s + " " + '</s>' + " ")
#print(list)
learner_test = [s.lower() for s in list]
#print(list2)

dictLearnerTest = {}

learnerTestOriginalTotalWord = 0
for s in learner_test :
    for c in s.split() :
        learnerTestOriginalTotalWord += 1
        if c in dictLearnerTest :
            dictLearnerTest[c] += 1
        else :
            dictLearnerTest[c] = 1

learnerTestArticle = []
for s in learner_test :
    for c in s.split() :
        if c in dictLearnerTest and dictLearnerTest[c] == 1 :
            #print(s)
            learnerTestArticle.append(c.replace(c,"<unk>"))
            #print(s.replace(c,"<unk>"))
        else :
            learnerTestArticle.append(c)

#print(learnerTestArticle)
#put all consequtive two words in brown-train into hashMap

# key is the first word, value is the second word inside the map
brown_train_map = {}

for i in range(0, len(newArticle) - 1) :
    str = newArticle[i] + newArticle[i + 1]
    if str in brown_train_map :
        brown_train_map[str] += 1
    else :
        brown_train_map[str] = 1


#check the brown-test & learner-test's existance inside the hashMap
# brown-test
count = 0
for i in range(0, len(brownTestArticle) - 1) :
    str = brownTestArticle[i] + brownTestArticle[i + 1]
    if str in brown_train_map :
        count += 1
bt_percentageDoesnotOccure = (float(len(brownTestArticle) - count)) / float(len(brownTestArticle))
print("bigram not occure in brownTest Article : ")
print(bt_percentageDoesnotOccure)

count = 0
for i in range(0, len(learnerTestArticle) - 1) :
    str = learnerTestArticle[i] + learnerTestArticle[i + 1]
    if str in brown_train_map :
        count += 1
lt_percentageDoesnotOccure = (float(len(learnerTestArticle) - count)) / float(len(learnerTestArticle))
print("bigram not occure in learnerTest Article : ")
print(lt_percentageDoesnotOccure)

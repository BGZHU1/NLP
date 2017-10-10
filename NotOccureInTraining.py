
#Q3
import re
from languagePreProcessing import dict
#print(dict)
print('answer for question 3 :')

print('for brown-test : ')

docName = "brown-test.txt"
text = ''.join(open(docName).readlines())
brown_test = re.split(r' *[\.\?!][\'"\)\]]* *', text)
brown_test = [s.lower() for s in brown_test]

totalBrownTestWords = 0
notInBrownTestWords = 0
for s in brown_test :
    for c in s.split() :
        totalBrownTestWords += 1
        if c not in dict :
            notInBrownTestWords += 1
print(notInBrownTestWords)
print(float(notInBrownTestWords)/ float(totalBrownTestWords))

#print(dict)

print('for learner-test : ')
docName = "learner-test.txt"
text = ''.join(open(docName).readlines())
learner_test = re.split(r' *[\.\?!][\'"\)\]]* *', text)
learner_test = [s.lower() for s in learner_test]

totalLearnerTestWords = 0
notInLearnerTestWords = 0
for s in learner_test :
    for c in s.split() :
        totalLearnerTestWords += 1
        if c not in dict :
            notInLearnerTestWords += 1
print(notInLearnerTestWords)
print(float(notInLearnerTestWords)/ float(totalLearnerTestWords))

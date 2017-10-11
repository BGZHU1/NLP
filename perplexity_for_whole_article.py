#Q7
from languagePreProcessing import newDict
from biagram_not_occure import dictBrownTest
import re
import math
#brown-test article pre processing
docName = "brown-test.txt"
text = ''.join(open(docName).readlines())
brown_test = re.split(r' *[\.\?!][\'"\)\]]* *', text)
brown_test = [s.lower() for s in brown_test]

list = []
for s in brown_test :
    list.append('<s>'+" " + s + " " + '</s>' + " ")
#print(list)
brown_test = [s.lower() for s in list]

dictBrownTest = {}
totalBrownTestLength = 0
for s in brown_test :
    totalBrownTestLength += 1
    for c in s.split() :
        if c in dictBrownTest :
            dictBrownTest[c] += 1
        else :
            dictBrownTest[c] = 1

brown_test_article= []
for s in brown_test :
    for c in s.split() :
        if c in dictBrownTest and dictBrownTest[c] == 1 :
            #print(s)
            brown_test_article.append(c.replace(c,"<unk>"))
            #print(s.replace(c,"<unk>"))
        else :
            brown_test_article.append(c)
#print(brown_test_article)


#learner-test article for preProcessing
docName = "learner-test.txt"
text = ''.join(open(docName).readlines())
learner_test = re.split(r' *[\.\?!][\'"\)\]]* *', text)
learner_test = [s.lower() for s in brown_test]

list = []
for s in learner_test :
    list.append('<s>'+" " + s + " " + '</s>' + " ")
#print(list)
learner_test = [s.lower() for s in list]

dictLearnerTest = {}

totalLearnerTestLength = 0
for s in learner_test :
    for c in s.split() :
        totalLearnerTestLength += 1
        if c in dictLearnerTest :
            dictLearnerTest[c] += 1
        else :
            dictLearnerTest[c] = 1

learner_test_article= []
for s in learner_test :
    for c in s.split() :
        if c in dictLearnerTest and dictLearnerTest[c] == 1 :
            #print(s)
            learner_test_article.append(c.replace(c,"<unk>"))
            #print(s.replace(c,"<unk>"))
        else :
            learner_test_article.append(c)
#print(learner_test_article)

#unigram model
print("unigram model perpelxity for whole article")
print("brown-test perplexity for unigram model")
#unigram model:
#logp = logp1 + logp2 + logp3
brown_test_unigram_results = {}
for s in dictBrownTest :
    result = 0.0
    for c in s.split() :
        prob = dictBrownTest.get(c)
        #print(prob)
        if prob == None :
            result += 0
        else :
            temp = math.log(float(prob)) - math.log(float(totalBrownTestLength))
            result += temp
brown_test_unigram_results = 2**(-result/float(totalBrownTestLength))
print(brown_test_unigram_results)

print("learner-test perplexity for unigram model")
learner_test_unigram_results = {}
for s in dictLearnerTest :
    result = 0.0
    for c in s.split() :
        prob = dictLearnerTest.get(c)
        #print(prob)
        if prob == None :
            result += 0
        else :
            temp = math.log(float(prob)) - math.log(float(totalLearnerTestLength))
            result += temp
learner_test_unigram_results = 2**(-result/float(totalLearnerTestLength))
print(learner_test_unigram_results)

#-----------------------------------------------------

#bigram model
print("biagram model perpelxity for whole article")
print("brown-test perplexity for biagram model")

for s in brown_test :
    result = 0.0
    temp = s.split()
    for i in range(0, len(s.split()) - 1):
        divident_word = temp[i] + temp[i + 1]
        divisor_word = temp[i]
        prob_divident = dictBrownTest.get(divident_word)
        prob_divisor = newDict.get(divisor_word)

        if (prob_divisor == None or prob_divident == None) :
            result += 0.0
        else :
            prob = math.log(float(prob_divident)) - math.log(float(prob_divisor))
            result += prob
brown_test_biagram_result = 2**(-result/float(totalBrownTestLength))
print("brown_test_biagram_result :")
print(brown_test_biagram_result)

print("learner-test perplexity for biagram model")

for s in learner_test :
    result = 0.0
    temp = s.split()
    for i in range(0, len(s.split()) - 1):
        divident_word = temp[i] + temp[i + 1]
        divisor_word = temp[i]
        prob_divident = dictBrownTest.get(divident_word)
        prob_divisor = newDict.get(divisor_word)
        #print(prob_divisor)
        #print(prob_divident)
        if (prob_divisor == None or prob_divident == None) :
            result += 0.0
        else :
            prob = math.log(float(prob_divident)) - math.log(float(prob_divisor))
            result += prob
learner_test_biagram_result = 2**(-result/float(totalLearnerTestLength))

print("learner_test_biagram_result : ")
print(learner_test_biagram_result)

#add one smoothing bigram model
print("add one smoothing model perpelxity for whole article")
print("brown-test perplexity for add one smoothing model")
for s in brown_test :
    result = 0.0
    temp = s.split()
    countAdding = 0
    for i in range(0, len(s.split()) - 1):
        divident_word = temp[i] + temp[i + 1]
        divisor_word = temp[i]
        prob_divident = dictBrownTest.get(divident_word)
        prob_divisor = newDict.get(divisor_word)

        if (prob_divident == None) :
            countAdding += 1
            prob_divident = 1
        if (prob_divisor == None) :
            prob_divisor = 1
            countAdding += 1
        prob = math.log(float(prob_divident)) - math.log(float(prob_divisor + countAdding))
        result += prob
add_one_smoothing_brown_test_result = 2**(-result/float(totalBrownTestLength))
print("adding_one_smoothing_brown_test_result : ")
print(add_one_smoothing_brown_test_result)


print("learner-test perplexity for add one smoothing model")
for s in learner_test :
    result = 0.0
    temp = s.split()
    countAdding = 0
    for i in range(0, len(s.split()) - 1):
        divident_word = temp[i] + temp[i + 1]
        divisor_word = temp[i]
        prob_divident = dictBrownTest.get(divident_word)
        prob_divisor = newDict.get(divisor_word)

        if (prob_divident == None) :
            countAdding += 1
            prob_divident = 1
        if (prob_divisor == None) :
            prob_divisor = 1
            countAdding += 1
        prob = math.log(float(prob_divident)) - math.log(float(prob_divisor + countAdding))
        result += prob
add_one_smoothing_learner_test_results = 2**(-result/float(totalLearnerTestLength))
print("learner_test_biagram_result : ")
print(add_one_smoothing_learner_test_results)

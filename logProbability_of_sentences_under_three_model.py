#Q5
from languagePreProcessing import newDict, totalTokens
from biagram_not_occure import dictBrownTest
import math


list = {'<s > He was laughed off the screen . </s>', ' <s> There was no compulsion behind them . </s>',
'<s> I look forward to hearing your reply . </s>' }

list = [s.lower() for s in list]


#unigram model:
#logp = logp1 + logp2 + logp3
unigram_results = {}
for s in list :
    result = 0.0
    for c in s.split() :
        prob = newDict.get(c)
        #print(prob)
        if prob == None :
            result += 0
        else :
            temp = math.log(float(prob)) - math.log(float(totalTokens))
            result += temp
    unigram_results[s] = result
print(unigram_results)

#bigram model
biagram_results = {}
for s in list :
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
    biagram_results[s] = result

print(biagram_results)

#add one smoothing
add_one_smoothing_biagram_results = {}

for s in list :
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
    add_one_smoothing_biagram_results[s] = result

print(add_one_smoothing_biagram_results)

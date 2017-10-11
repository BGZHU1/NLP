#Q6
from logProbability_of_sentences_under_three_model import unigram_results,biagram_results,add_one_smoothing_biagram_results

#l = 1/m sum (logp(si))

#unigram maxium likelihood model
print("unigram perplexity :")
#print(unigram_results)
unigram_perplexity_results = {}
for s in unigram_results :
    length = len(s.split())
    unigram_perplexity = unigram_results[s]/length
    unigram_perplexity_results[s] = unigram_perplexity
print(unigram_perplexity_results)

#biagram maxium likelihood model
print("biagram perplexity :")
biagram_perplexity_results = {}
for s in biagram_results :
    length = len(s.split())
    biagram_perplexity = biagram_results[s]/length
    biagram_perplexity_results[s] = biagram_perplexity
print(biagram_perplexity_results)
#add one smoothing likelihood model
print("add one smoothing perplexity :")
add_one_perplexity_results = {}
for s in add_one_smoothing_biagram_results :
    length = len(s.split())
    add_one_perplexity_result = add_one_smoothing_biagram_results[s]/length
    add_one_perplexity_results[s] = add_one_perplexity_result
print(add_one_perplexity_results)

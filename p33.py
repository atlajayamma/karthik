#unigram
from nltk.util import ngrams
sentence='The greatest glory in living lies not in never falling, but in rising every time we fall'
unigrams=ngrams(sentence.split(), 1)
for items in unigrams:
    print(items)
#bigram
from nltk.util import ngrams
sentence='The greatest glory in living lies not in never falling, but in rising every time we fall'
bigrams=ngrams(sentence.split(), 2)
for items in bigrams:
    print(items)
#trigram
from nltk.util import ngrams
sentence='The greatest glory in living lies not in never falling, but in rising every time we fall'
trigrams=ngrams(sentence.split(), 3) 
for items in trigrams:
    print(items)

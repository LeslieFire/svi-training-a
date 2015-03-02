'''
Created by Peter Norvig 2007
Comments by Antonio Ortiz 03/02/2015
Input: any word or preferrably a mispelled word
Output: a corrected word
'''

import re, collections
from pprint import pprint

def words(text)
	'''
	This is to find all the word in the specified file.
	'''
	'''
	 '*' means zero or more. '+' is one or more.
	 re.findall 1st argument is the pattern, 2nd is the string which are all converted to small letters.
	'''
	return re.findall('[a-z]+', text.lower())

def train(features):
	'''
	count the occurences of words and return a tuple.
	'''
	'''
	defaultdict: used for sorting.
	lambda: an anonymous function that is not bound to a name.
	everytime f occurs, the function adds 1 to key f with the default value of 1. e.g. if there 3 occurrences of letter 'd'
	in the features, it model will have a tuple of ('d', 3+1). if lambda is 0, then it will just be ('d', 3)
	'''
	'''
	lambda is 1 because the author wants to employ smoothing in the training list but there is no point on this
	if we'll only be computing the results under a unigram language model.
	'''

	model = collections.defaultdict(lambda: 1)
	for f in features:
		model[f] += 1

	return model

#gets the words on big.txt and returns the word and their corresponding count in occurrence.
NWORDS = train(words(file('big.txt').read()))

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def edits1(word):
	'''returns all the words (most are not real words) with minimum edit distance of 1 by iterating through all possible
	deletes (n occurences), transposes (n-1 occurences), replacements(26n occurences, 26 because of the alphabet)
	and inserts ((n+1)26 because new letter can be inserted at the start and at the bottom'''

	splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
	
	deletes = [a + b[1:] for a, b in splits if b]
	transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
	replaces = [a + c + b[1:] for a, b in splits for c in alphabet if b]
	inserts = [a + c + b for a, b in splits for c in alphabet]

	return set(deletes + transposes + replaces + inserts)

def edits2(word):
	'''
	returns all words minimum edit distance of 2 by making rersults of edits1 run through itself again. This would most
	Probably return hundreds of thousands of words but only a small percentage of those are real words.
	'''
	return 	set(e2 for e1 in edits1(word) for e2 in edits1(e1))

def known_edits2(word):
	'''
	returns only all the known words on words with a minimum edit distance of 2. (real words that are found in our corpus).
	'''
	return set(e2 for e1 in edits1(word) for e2 in edits1(e1) if e2 in NWORDS)

def known(words):
	'''
	a function that requires an input of words and returns a list of words if they including in our list of known words NWORDS.
	'''
	return set(w for w in words if w in NWORDS)

def correct(word):
	'''
	returns the best possible guess of the script on what the mistaken word is by return the known word that is most commonly
	occuring in our list of known words with occurences in the corpus
	'''
	candidates = known([word]) or known(edits1(word)) or known_edits2(word) or [word]
	
	#returns the value of the key which are the candidates and is called by NWORDS.get()
	return max(candidates, key=NWORDS.get)



def spelltest(tests, bias=None, verbose=False):
    '''
    This is for testing whether the results of the code above is accurate or not.
    Input is a list of words with common mispellings.
    This tests whether the script above will return the key of the common mispelling which is the actual word.
    '''
    import time
    n, bad, unknown, start = 0, 0, 0, time.clock()
    if bias:
        for target in tests: NWORDS[target] += bias
    for target,wrongs in tests.items():
        for wrong in wrongs.split():
            n += 1
            w = correct(wrong)
            if w!=target:
                bad += 1
                unknown += (target not in NWORDS)
                if verbose:
                    print '%r => %r (%d); expected %r (%d)' % (
                        wrong, w, NWORDS[w], target, NWORDS[target])
    return dict(bad=bad, n=n, bias=bias, pct=int(100. - 100.*bad/n), 
                unknown=unknown, secs=int(time.clock()-start) )

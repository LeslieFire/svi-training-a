#CS 124 / LING 180 From Languages to Information, Dan Jurafsky, Winter 2015 
####Week 2: Group Exercises on Language Modeling, Tuesday Jan 20, 2015

####Part 1: Group Exercise
We are interested in building a language model over a language with three words: A, B, C. Our training corpus is

	*AAABACBABBBCCACBCC*

First train a unigram language model using maximum likelihood estimation. What are the probabilities? (Just leave in the form of a fraction)?

	P(A) = 6/18
	
	P(B) = 6/18
	
	P(C) = 6/18

Next train a bigram language model using maximum likelihood estimation. Fill in the probabilities below. Leave your answers in the form of a fraction.

	P(A|A) = C(A,A)/P(A) = 2/6
	
	P(A|B) = C(B,A)/C(B) = 1/6
	
	P(A|C) = C(C,A)/C(C) = 1/6
	
	P(B|A) = C(A,B)/C(A) = 2/6
	
	P(B|B) = C(B,B)/C(B) = 2/6
	
	P(B|C) = C(C,B)/C(C) = 2/6
	
	P(C|A) = C(A,C)/C(A) = 2/6
	
	P(C|B) = C(B,C)/C(B) = 2/6
	
	P(C|C) = C(C,C)/C(C) = 2/6

####Now evaluate your language models on the corpus ABACABB
What is the perplexity of the unigram language model evaluated on this corpus?

	PP(W)	= P(w1*w2...wn)**-(1/n)

 			= (6/18**n)**-(1/n)

			= (6/18)**-1

			= 18/6

			= 3

What is the perplexity of the bigram language model evaluated on this corpus? 

	PP(W)	= P(w1*w2...wn)**-(1/n)

			= (P(B|A)*P(A|B)*P(C|A)*P(A|C)*P(B|A)*P(B|B))**-(1/n)

			= ((2/6)*(1/6)*(2/6)*(1/6)*(2/6)*(2/6))**-(1/7)

			= 3.1258608823116254

####Now repeat everything above for add-1 smoothing.

First train a unigram language model using maximum likelihood estimation. What are the probabilities? (Just leave in the form of a fraction)?

	P(A) = (6+1)/(18+3) = 1/3
	
	P(B) = (6+1)/(18+3) = 1/3
	
	P(C) = (6+1)/(18+3) = 1/3
		
Next train a bigram language model using maximum likelihood estimation. Fill in the probabilities below. Leave your answers in the form of a fraction.

	P(A|A) = (C(A,A)+1)/((C(A|A)+1)+(C(B|A)+1)+(C(C|A)+1)) = 1/3
	
*formula above is the same as the ones below
	
	P(A|B) = (C(B,A)+1)/(C(B)+3) = (1+1)/(6+3) = 2/9
	
	P(A|C) = (C(C,A)+1)/(C(C)+3) = (1+1)/(6+3) = 2/9
	
	P(B|A) = (C(A,B)+1)/(C(A)+3) = (2+1)/(6+3) = 1/3
	
	P(B|B) = (C(B,B)+1)/(C(B)+3) = (2+1)/(6+3) = 1/3
	
	P(B|C) = (C(C,B)+1)/(C(C)+3) = (2+1)/(6+3) = 1/3
	
	P(C|A) = (C(A,C)+1)/(C(A)+3) = (2+1)/(6+3) = 1/3
	
	P(C|B) = (C(B,C)+1)/(C(B)+3) = (2+1)/(6+3) = 1/3
	
	P(C|C) = (C(C,C)+1)/(C(C)+3) = (2+1)/(6+3) = 1/3

####Part 2: Challenge Problems
Suppose you build an interpolated trigram language model, with three weights lambda1 for unigrams, lambda2 for bigrams, and lambda3 for trigrams. Normally we set these lambdas on a held-out set. Suppose instead we set them on the training data. This will cause the lambdas to take on very unusual values. What will these lambdas look like? Why? 
 

*Still havent answered this*


Show that if we estimate two bigram language models using unsmoothed relative frequencies (MLE), one from a text corpus and the second from the same corpus in reverse order, the models will assign the same probability to new sentences (when applied in forward and backward order respectively). Hint: First write out the entire equation for sentence probabilities in terms of counts.

*Still havent answered this*




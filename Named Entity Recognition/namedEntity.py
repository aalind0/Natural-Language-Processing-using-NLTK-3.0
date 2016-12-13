# Chunking
# part of pre-processing.

import nltk
from nltk.corpus import state_union

# Punkt Sentence Tokenizer - Unsupervised Machine Learning Tokenizer (can be retrained rather than using default.)
from nltk.tokenize import PunktSentenceTokenizer



train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

# training the tokenizer
custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

# using the tokenizer on actual text
tokenized = custom_sent_tokenizer.tokenize(sample_text)

# using the part of speech tagging to tag all parts of speech per sentence.
def process_content():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            
            namedEnt = nltk.ne_chunk(tagged, binary = True)
            
            namedEnt.draw()
    
    except Exception as e:
        print(str(e))
        
process_content()
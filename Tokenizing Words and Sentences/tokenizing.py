# Tokenizing Words and Sentences using NLTK-3

from nltk.tokenize import sent_tokenize, word_tokenize

# Tokenizing - Word tokenizers and Sentence tokenizers
# Corpora - body of text
# Lexicon - words and their meanings

Example_text = "Hi there developer, what's up ? Machine Learning is awesome. Do not puke on your screen."

##print(sent_tokenize(Example_text))

##print(word_tokenize(Example_text))

for i in word_tokenize(Example_text):
    print(i)

for i in sent_tokenize(Example_text):
    print(i)
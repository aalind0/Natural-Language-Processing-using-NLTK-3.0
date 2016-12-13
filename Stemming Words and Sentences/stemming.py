# Stemming Words - Sort of pre-processing.
# Using the most popular stemming algo Porter Stemmer (1979). wow !

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

example_words = ["python", "pythoner", "pythoning", "pythoned", "pythonly", "ride", "riding", "ridden", "rides"]

for w in example_words:
    print(ps.stem(w))

# Stemming a sentence now.    
new_text = "It is very important to be pythonly while you are pythoning with python. All pythoners have pythoned poorly at least once."

words = word_tokenize(new_text)

for w in words:
    print(ps.stem(w))
# Stop Words Removal 

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

Example_sentence = "Hi there developer, what's up ? Machine Learning is awesome. Do not puke on your screen."

stop_words = set(stopwords.words("english"))

words = word_tokenize(Example_sentence)

filtered_sentence = []

for w in words:
    if w not in stop_words:
        filtered_sentence.append(w)
        
# basically doing the same thing as the above loop but now in one line.
filtered_sent = [w for w in words if not w in stop_words]
        
print(filtered_sentence)
print(filtered_sent)
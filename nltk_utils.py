import nltk
from nltk.stem.snowball import PorterStemmer
import nltk
import numpy as np
nltk.download('punkt')

def tokenize(sentence):
  return nltk.word_tokenize(sentence)

def stem(word):
  stemmer = nltk.stem.porter.PorterStemmer()
  return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence, all_words):
    """
    sentence = ["hello", "how", "are", "you"]
    words = ["hi", "hello", "I", "you", "bye", "thank", "cool"]
    bag =    [0,       1,    0 ,  1,      0,      0,        0]
    """
    tokenized_sentence = [stem(w) for w in tokenized_sentence]
    bag = np.zeros(len(all_words), dtype = np.float32)
    for idx, w in enumerate(all_words):
        if w in tokenized_sentence:
            bag[idx] = 1.0
    return bag

  



a = "how are u Fucking doing"
print(a)

a = tokenize(a)
print(a)

a = [stem(word) for word in a]
print(a)

# create training data

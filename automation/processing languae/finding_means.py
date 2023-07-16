import nltk
from nltk.stem import WordNetLemmatizer

x = "was"
y = "is"

nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()
lemma = lemmatizer.lemmatize(x,'v') #Valid options are "n" for nouns, "v" for verbs, "a" for adjectives, "r" for adverbs and "s" for satellite adjectives.
print(lemma)

lemma_two = lemmatizer.lemmatize(y,'v') #Valid options are "n" for nouns, "v" for verbs, "a" for adjectives, "r" for adverbs and "s" for satellite adjectives.
print(lemma)

print(lemma_two == lemma)
    
lemma = lemmatizer.lemmatize("vegetables",'v') #Valid options are "n" for nouns, "v" for verbs, "a" for adjectives, "r" for adverbs and "s" for satellite adjectives.
lemma_two = lemmatizer.lemmatize("vegetable",'v') #Valid options are "n" for nouns, "v" for verbs, "a" for adjectives, "r" for adverbs and "s" for satellite adjectives.
print(lemma_two == lemma)

lemma = lemmatizer.lemmatize("vegetables",'n') #Valid options are "n" for nouns, "v" for verbs, "a" for adjectives, "r" for adverbs and "s" for satellite adjectives.
lemma_two = lemmatizer.lemmatize("vegetable",'v') #Valid options are "n" for nouns, "v" for verbs, "a" for adjectives, "r" for adverbs and "s" for satellite adjectives.
print(lemma_two == lemma)
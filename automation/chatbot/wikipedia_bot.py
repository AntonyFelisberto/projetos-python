import nltk
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import wikipedia 

nltk.download('wordnet')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

lemmatizer = WordNetLemmatizer()

sentence = wikipedia.page("Vegetables").content #you can replace Vegetables with something that the user write

question = "what are vegetables ?"

def lemma_me(sent):
    sentence_tokens = nltk.word_tokenize(sent.lower())
    pos_tags = nltk.pos_tag(sentence_tokens)

    sentence_lemmas = []
    for token, pos_tag in zip(sentence_tokens, pos_tags):
        if pos_tag[1][0].lower() in ['n', 'v', 'a', 'r']:
            lemma = lemmatizer.lemmatize(token, pos_tag[1][0].lower())
            sentence_lemmas.append(lemma)

    return sentence_lemmas

def process(sentence,question):
    sentence_tokens = nltk.sent_tokenize(sentence)
    sentence_tokens.append(question)

    tv = TfidfVectorizer(tokenizer=lemma_me)
    tf = tv.fit_transform(sentence_tokens)

    values = cosine_similarity(tf[-1],tf)   #tf[-1] is the last item in the array, tf is the entire array

    index = values.argsort()[0][-2]

    values_flat = values.flatten()
    values_flat.sort()
    coeff = values_flat[-2]

    if coeff > 0.3:
        return sentence_tokens[index]
    
while True:
    question = input("What do you want to know ? \n")
    output = process(sentence=sentence,question=question)
    if output: #you can do output!=None too, is the same thing
        print(output)
    elif question=='quit':
        break
    else:
        print("i don´t know")
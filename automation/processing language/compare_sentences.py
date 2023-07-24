import nltk
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

lemmatizer = WordNetLemmatizer()
sentence = "vegetables are types of plants."

sentence_lemmas = []

def lemma(sent):
    sentence_token = nltk.word_tokenize(sent.lower())
    pos_tags = nltk.pos_tag(sentence_token)
    for token, pos_tag in zip (sentence_token, pos_tags):
        if pos_tag[1][0].lower() in ['n','v','a','r']:
            lemma = lemmatizer.lemmatize(token,pos_tag[1][0].lower())
            sentence_lemmas.append(lemma)
    return sentence_lemmas

print(lemma(sentence))
import nltk
import pandas
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('wordnet')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

lemmatizer = WordNetLemmatizer()
sentence = "Originally, vegetables were collected from the wild by hunter-gatherers. Vegetables are all plants. Vegetables can be eaten either raw or cooked."
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


sentence_tokens = nltk.sent_tokenize(sentence)
sentence_tokens.append(question)
print(sentence_tokens)

tv = TfidfVectorizer(tokenizer=lemma_me)
print(tv)

tf = tv.fit_transform(sentence_tokens)
print(tf)

print(tf.toarray())

df = pandas.DataFrame(tf.toarray(),columns=tv.get_feature_names_out())
print(df)

values = cosine_similarity(tf[-1],tf)   #tf[-1] is the last item in the array, tf is the entire array
print(values)

index = values.argsort()[0][-2]
print(index)

values_flat = values.flatten()
print(values_flat)
coeff = values_flat[-2]

if coeff > 0.3:
    print(sentence_tokens[index])
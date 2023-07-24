import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')
nltk.download('twitter_samples')
text = "Hey, what a beautiful day! how amazing it is"

analyzer = SentimentIntensityAnalyzer()
print(analyzer.polarity_scores(text))

if analyzer.polarity_scores(text)['compound'] > 0:
    print("positive")
else:
    print("negative")

nltk.corpus.twitter_samples.strings()
tweet = nltk.corpus.twitter_samples.strings()[1045]
print(analyzer.polarity_scores(tweet))
# https://towardsdatascience.com/synonyms-and-antonyms-in-python-a865a5e14ce8
# https://spacytextblob.netlify.app/docs/example
import nltk
import spacy
from nltk.corpus import wordnet
from spacytextblob.spacytextblob import SpacyTextBlob


nltk.download('wordnet')

nlp = spacy.load("en_core_web_sm")
nlp.add_pipe("spacytextblob")


def nlpFunc(text):
    synonyms = []
    words = []
    neg_words = []
    neu_words = []
    neg_words = []

    # NLP analysis of single-line text
    doc = nlp(text)

    # print(doc._.assessments)

    if len(text) != 0:

        # list comphresion to get the emotional words

        if doc._.polarity > 0:
            words = list(zip(*doc._.assessments))

        elif doc._.polarity == 0:
            neu_words = list(zip(*doc._.assessments))

        else:
            neg_words = list(zip(*doc._.assessments))

        # for index in range(0, len(words)):
        if (len(words) != 0):

            word = list(zip(*words[0]))
            print("pos", word)
            word3 = list(zip(*word))

            for index in range(0, len(word3)):
                # print(index, "-", *word3[index])

                # Word Cloud
                # looks for synonym(s) of the emotional word(s)
                for sy in wordnet.synsets(*word3[index]):
                    # returns the synonyms of the emotional word(s)
                    for le in sy.lemmas():
                        # adds the snonym(s) to the synonyms list
                        synonyms.append(le.name())
                # prints the synonym(s) of the emotional word(s)
                print("pos syn", set(synonyms))

        elif(len(neu_words) != 0):

            neu_words2 = list(zip(*neu_words[0]))
            print("neu", neu_words2)
            neu_words3 = list(zip(*neu_words2))

            for index in range(0, len(neu_words3)):
                # print(index, "-", *word3[index])

                # Word Cloud
                # looks for synonym(s) of the emotional word(s)
                for sy in wordnet.synsets(*neu_words3[index]):
                    # returns the synonyms of the emotional word(s)
                    for le in sy.lemmas():
                        # adds the snonym(s) to the synonyms list
                        synonyms.append(le.name())
                # prints the synonym(s) of the emotional word(s)
                print("neu syn", set(synonyms))

        elif len(neg_words) != 0:

            neg_words2 = list(zip(*neg_words[0]))
            print("negative", neg_words2)
            neg_words3 = list(zip(*neg_words2))

            for index in range(0, len(neg_words3)):
                # print(index, "-", *word3[index])

                # Word Cloud
                # looks for synonym(s) of the emotional word(s)
                for sy in wordnet.synsets(*neg_words3[index]):
                    # returns the synonyms of the emotional word(s)
                    for le in sy.lemmas():
                        # adds the snonym(s) to the synonyms list
                        synonyms.append(le.name())
                # prints the synonym(s) of the emotional word(s)
                print("negative syn", set(synonyms))

            # Input multiple lines of text
            docs = list(nlp.pipe([text]))





        else:
            synonyms = ["no synonyms found"]

        # for doc in docs:
        # print('Assessments:', doc._.assessments)
    else:
        synonyms = ["Please enter text"]

    return synonyms


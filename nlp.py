# https://towardsdatascience.com/synonyms-and-antonyms-in-python-a865a5e14ce8
# https://spacytextblob.netlify.app/docs/example
import nltk
import spacy
from nltk.corpus import wordnet
from spacytextblob.spacytextblob import SpacyTextBlob
import en_core_web_sm


nltk.download('wordnet')

nlp = en_core_web_sm.load()
nlp.add_pipe("spacytextblob")


def nlpFunc(text):
    # Input single text?
    synonyms = []
    doc = nlp(text)

    # print(doc._.assessments)

    if(len(text)!=0):
        # list comphresion to get the emotional words
        words = list(zip(*doc._.assessments))
        # for index in range(0, len(words)):
        word = list(zip(*words[0]))
        word3 = list(zip(*word))

        for index in range(0, len(word3)):
            # print(index, "-", *word3[index])

            # Word Cloud
            for syn in wordnet.synsets(*word3[index]):
                for lm in syn.lemmas():
                    synonyms.append(lm.name())  # adding into synonyms

            print(set(synonyms))

        # Input multiple lines of text?
        docs = list(nlp.pipe([text]))


        # for doc in docs:
            # print('Assessments:', doc._.assessments)


        
    return synonyms

    

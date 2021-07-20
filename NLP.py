# https://towardsdatascience.com/synonyms-and-antonyms-in-python-a865a5e14ce8
# https://spacytextblob.netlify.app/docs/example
import nltk
import spacy
from nltk.corpus import wordnet
from spacytextblob.spacytextblob import SpacyTextBlob


nltk.download('wordnet')

nlp = spacy.load("en_core_web_sm")
nlp.add_pipe("spacytextblob")

def get_polarity(text):

    doc = nlp(text)

    for span in doc.sents:

        print(span.text, span._.polarity, span._.subjectivity)

        return span._.polarity


def nlp_func(text):
    pos_synonyms = []
    neu_synonyms = []
    neg_synonyms = []

    # NLP analysis of single-line text
    #doc = nlp(text) 
    
    doc = list(nlp.pipe([text]))
    emotional_words = dict()

    for word in doc: 
        #captures the emotional words
        for assessment in word._.assessments:
           tmp = assessment[0]
           polarity = assessment[1]
           for emotional_word in tmp:
               emotional_words[str(emotional_word)] = float(polarity)

    #[(word, polarity)]
    print(emotional_words)

    for x in emotional_words:
        print(x)
        if x in emotional_words:
            if(emotional_words[x] > 0):
                    pos_synonyms.append(str(x))
                    for syn in wordnet.synsets(str(x)):
                        for lm in syn.lemmas():
                            #if lm.name()in pos_synonyms :
                            # adds the snonym(s) to the synonyms list
                            pos_synonyms.append(lm.name())
            elif(emotional_words[x] < 0):
                    neg_synonyms.append(str(x))
                    for syn in wordnet.synsets(str(x)):
                        for lm in syn.lemmas():
                            #if lm.name()in pos_synonyms :
                            # adds the snonym(s) to the synonyms list
                            neg_synonyms.append(lm.name())
                #returns the synonyms of the emotional word(s)
            elif(emotional_words[x] == 0):
                    neu_synonyms.append(str(x))
                    for syn in wordnet.synsets(str(x)):
                        for lm in syn.lemmas():
                            #if lm.name()in pos_synonyms :
                            # adds the snonym(s) to the synonyms list
                            neu_synonyms.append(lm.name())
                #returns the synonyms of the emotional word(s)
            
        
    print("positive: ")           
    print(set(pos_synonyms))
    
    print("negative")
    print(set(neg_synonyms))

    print("neutral: ")           
    print(set(neu_synonyms))

#OLD TIMES:

    
    # words = []
    # # neg_words = []
    # neu_words = []
    # neg_words = []

    # word = ""
    # polarity = 0.0

    # pos_polarity = dict()
    # neu_polarity = dict()
    # neg_polarity = dict()

    # print(doc._.assessments)

    # seperate out words

    # if len(text) != 0:

    #     # list comphresion to get the emotional words

    #     if doc._.polarity > 0:
    #         words = list(zip(*doc._.assessments))
    #         # pos_polarity[doc._.assessments] = doc._.polarity

    #     elif doc._.polarity == 0:
    #         neu_words = list(zip(*doc._.assessments))
    #         # neu_polarity[doc._.assessments] = doc._.polarity

    #     else:
    #         neg_words = list(zip(*doc._.assessments))
    #         #print(neg_words)
    #         # neg_polarity[doc._.assessments] = doc._.polarity

    #     print("Polarity:")
    #     print(doc._.polarity)


    #     # for index in range(0, len(words)):
    #     if (len(words) != 0):

    #         word = list(zip(*words[0]))
    #         #print("pos", word)
    #         word3 = list(zip(*word))

    #         for index in range(0, len(word3)):
    #             # print(index, "-", *word3[index])

    #             # Word Cloud
    #             # looks for synonym(s) of the emotional word(s)
    #             for syn in wordnet.synsets(*word3[index]):
    #                 # returns the synonyms of the emotional word(s)
    #                 for lm in syn.lemmas():
    #                     if lm.name() not in pos_synonyms :
    #                         # adds the snonym(s) to the synonyms list
    #                         pos_synonyms.append(lm.name())
    #             # prints the synonym(s) of the emotional word(s)
    #             # print("pos syn", set(pos_synonyms))

    #     elif(len(neu_words) != 0):

    #         neu_words2 = list(zip(*neu_words[0]))
    #         # print("neu", neu_words2)
    #         neu_words3 = list(zip(*neu_words2))

    #         for index in range(0, len(neu_words3)):
    #             # print(index, "-", *word3[index])

    #             # Word Cloud
    #             # looks for synonym(s) of the emotional word(s)
    #             for syn in wordnet.synsets(*neu_words3[index]):
    #                 # returns the synonyms of the emotional word(s)
    #                 for lm in syn.lemmas():
    #                     if lm.name() not in neu_synonyms:
    #                         # adds the snonym(s) to the synonyms list
    #                         neu_synonyms.append(lm.name())
    #             # prints the synonym(s) of the emotional word(s)
    #             # print("neu syn", set(neu_synonyms))

    #     elif len(neg_words) != 0:

    #         neg_words2 = list(zip(*neg_words[0]))
    #         #print("negative", neg_words2)
    #         neg_words3 = list(zip(*neg_words2))

    #         for index in range(0, len(neg_words3)):
    #             # print(index, "-", *word3[index])

    #             # Word Cloud
    #             # looks for synonym(s) of the emotional word(s)
    #             for syn in wordnet.synsets(*neg_words3[index]):
    #                 # returns the synonyms of the emotional word(s)
    #                 for lm in syn.lemmas():
    #                     if lm.name() not in neg_synonyms:
    #                         # adds the snonym(s) to the synonyms list
    #                         neg_synonyms.append(lm.name())
    #             # prints the synonym(s) of the emotional word(s)
    #             # print("negative syn", set(neg_synonyms))

    #         # Input multiple lines of text
    #         # docs = list(nlp.pipe([text]))





    #     else:
    #         synonyms = ["no synonyms found"]

    #     # for doc in docs:
    #     # print('Assessments:', doc._.assessments)
    # else:
    #     synonyms = ["Please enter text"]

    # return  pos_synonyms, neu_synonyms, neg_synonyms


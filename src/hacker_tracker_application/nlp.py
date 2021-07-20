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

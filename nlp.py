import spacy
from homeScreen import Page4
from spacy.matcher import PhraseMatcher

class NlpPage:
    nlp = spacy.load("en_core_web_sm")

    # PhraseMatcher
    matcher = PhraseMatcher(nlp.vocab)

    # Terms to match
    moods_list = ['happy', 'sad', 'excited', 'enjoy', 'depressed']

    # Make a list of docs
    patterns = [nlp.make_doc(text) for text in moods_list]

    matcher.add("phrase_matcher", None, *patterns)


if __name__ == "__main__":
    print("test")
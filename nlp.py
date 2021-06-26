import spacy
from spacy_wordnet.wordnet_annotator import WordnetAnnotator

if __name__ == "__main__":

    # Load an spacy model (supported models are "es", "en" and "pt")
    nlp = spacy.load('en_core_web_sm')
    # Spacy 3.x
    nlp.add_pipe("spacy_wordnet", after='tagger', config={'lang': nlp.lang})
    # Spacy 2.x
    # self.nlp_en.add_pipe(WordnetAnnotator(self.nlp_en.lang))
    token = nlp('prices')[0]

    # wordnet object link spacy token with nltk wordnet interface by giving acces to
    # synsets and lemmas
    token._.wordnet.synsets()
    token._.wordnet.lemmas()

    # And automatically tags with wordnet domains
    token._.wordnet.wordnet_domains()

    economy_domains = ['emotion', 'banking']
    enriched_sentence = []
    print("I am very happy now that I ate some food")
    test = input()
    sentence = nlp(test)

    # For each token in the sentence
    for token in sentence:
        # We get those synsets within the desired domains
        synsets = token._.wordnet.wordnet_synsets_for_domain(economy_domains)
        if not synsets:
            enriched_sentence.append(token.text)
        else:
            lemmas_for_synset = [lemma for s in synsets for lemma in s.lemma_names()]
            # If we found a synset in the economy domains
            # we get the variants and add them to the enriched sentence
            enriched_sentence.append('({})'.format('|'.join(set(lemmas_for_synset))))

    # Let's see our enriched sentence
    print(' '.join(enriched_sentence))
    # >> I (need|want|require) to (draw|withdraw|draw_off|take_out) 5,000 euros
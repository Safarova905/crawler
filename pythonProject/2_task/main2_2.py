from natasha import Doc, MorphVocab, Segmenter, NewsEmbedding, NewsMorphTagger
import codecs
from razdel import tokenize
import re

# lematization
for i in range(1, 101):
    with codecs.open('fileOutput%i.txt' %i, "r", "utf_8_sig") as f:
        text_original = f.read()

    segmenter = Segmenter()
    morph_vocab = MorphVocab()
    emb = NewsEmbedding()
    morph_tagger = NewsMorphTagger(emb)


    def natasha_lemmatize(text):
        doc = Doc(text)
        doc.segment(segmenter)
        doc.tag_morph(morph_tagger)
        for token in doc.tokens:
            token.lemmatize(morph_vocab)
        return {_.lemma: _.text for _ in doc.tokens}


    with codecs.open('lemmas/list_words%i.txt' %i, "w") as f1:
        d = natasha_lemmatize(text_original)
        for key, values in d.items():
            result_key = re.sub("[^а-яА-я]", "", str(key))
            result_value = re.sub("[^а-яА-я]", "", str(values))

            if result_value != "" and result_key != "":
                f1.write(result_key + ": " + result_value + '\n')

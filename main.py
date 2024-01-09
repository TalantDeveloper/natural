# pip install -U spacy
# python -m spacy download en_core_web_sm
import spacy
from translate import Translator

# Load English tokenizer, tagger, parser and NER
nlp = spacy.load("en_core_web_sm")

# Process whole documents
text = ("When Sebastian Thrun started working on self-driving cars at "
        "Google in 2007, few people outside of the company took him "
        "seriously. “I can tell you very senior CEOs of major American "
        "car companies would shake my hand and turn away because I wasn’t "
        "worth talking to,” said Thrun, in an interview with Recode earlier "
        "this week.")
doc = nlp(text)

# Analyze syntax
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "NOUN"])

verbs = [token.lemma_ for token in doc if token.pos_ == "VERB"]
print(verbs)
# for verb in verbs:
#         translator = Translator(provider='libre', from_lang='en', to_lang='ru')
#         translation = translator.translate(verb)
#         print(f"{verb}: {translation}")

translator = Translator(provider='libre', from_lang='en', to_lang='ru')
print(translator.translate('start'))

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)

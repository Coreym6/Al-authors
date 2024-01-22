# here is the documentation for the spacy library
# https://spacy.io/
# pip install -U spacy
# python -m spacy download en_core_web_sm
import spacy

# Load English tokenizer, tagger, parser and NER
nlp = spacy.load("en_core_web_sm")

# Process whole documents
'''text = ("When Sebastian Thrun started working on self-driving cars at "
        "Google in 2007, few people outside of the company took him "
        "seriously. “I can tell you very senior CEOs of major American "
        "car companies would shake my hand and turn away because I wasn’t "
        "worth talking to,” said Thrun, in an interview with Recode earlier "
        "this week.")''' 
# This above was from directly from the spacy website. 
text = ("James Agee, an influential figure in American literature, was born in Knoxville, Tennessee," 
         "and experienced the untimely loss of his father in a car accident during his childhood"
         "After completing his education at prestigious institutions such as St. Andrews School" 
         "and Phillips Exeter Academy, Agee embarked on a successful career in writing,"
         "working for notable publications such as Fortune magazine and Time magazine"
         "His significant contributions to literature include the renowned book"
         "His posthumously published novel A Death in the Family was awarded the Pulitzer Prize for Fiction in 1958."
        )# tried this with James, Agee the first author in the list of AL Authors, from the site 
doc = nlp(text)

# Analyze syntax
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)
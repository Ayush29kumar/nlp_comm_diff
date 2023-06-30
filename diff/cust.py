import spacy

nlp = spacy.load("en_core_web_sm")

# Define the custom dictionary mapping words to their desired part-of-speech tags
custom_dictionary = {
    "launch": {"pos": "VERB"},
    "gmail": {"pos": "PROPN"},
    "open": {"pos": "VERB"},
    "terminal": {"pos": "NOUN"}
}

# Function to update the part-of-speech tags based on the custom dictionary
def update_pos_with_custom_dictionary(doc):
    for token in doc:
        if token.text.lower() in custom_dictionary:
            token.pos_ = custom_dictionary[token.text.lower()]["pos"]
    return doc

# Add the custom pipeline component to the Spacy model
nlp.add_pipe(update_pos_with_custom_dictionary, name="custom_dictionary_pos", after="tagger")

# Apply the customized model to the text
texts = ["Launch Gmail", "Open terminal", "Launch terminal"]

for text in texts:
    doc = nlp(text)
    # Check the part-of-speech tags after the custom dictionary update
    for token in doc:
        print(token.text, token.pos_)
    print()
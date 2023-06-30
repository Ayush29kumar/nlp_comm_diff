import stanfordnlp
# Load the English language model
nlp = stanfordnlp.Pipeline(processors='tokenize,pos', lang='en')

while True:
    text = input("enter a sentence")
# Perform POS tagging
    doc = nlp(text)
    for sentence in doc.sentences:
        for word in sentence.words:
            print(word.text, word.pos)

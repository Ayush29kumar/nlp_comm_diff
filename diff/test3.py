import spacy , stanfordnlp , sys
nlp1 , nlp2 = spacy.load('en_core_web_sm') ,stanfordnlp.Pipeline(processors='tokenize,pos', lang='en')
while True :
    Verb_array = []
    conjuctions_array = []
    noun_array = []
    adp_array = []
    pronoun_array = []
    adv_array = []
    texts = input("enter the text").strip().lower()
    doc ,doc2 = nlp1(texts),nlp2(texts)
    spacy_pos_tags = [(token.text, token.pos_) for token in doc]
    stanford_nlp_postags = [(word.text, word.pos) for sentence in doc2.sentences for word in sentence.words]
    spacy_filtered_pos_tags = [(token.text, token.pos_) for token in doc if token.pos_ not in ["DET", "INTJ","SCONJ" ,]]
    stanford_filtered_pos_tags = [(word.text, word.pos) for sentence in doc2.sentences for word in sentence.words if word.pos not in ["DT", "UH"]]
    print(spacy_pos_tags)
    print(spacy_filtered_pos_tags)
    for loop in spacy_filtered_pos_tags:
        if loop[1] == "VERB" :
            Verb_array.append((loop[0] , spacy_filtered_pos_tags.index(loop)))
        if loop[1] == "CCONJ" or  loop[1] == "CONJ" :
            conjuctions_array.append((loop[0] ,spacy_filtered_pos_tags.index(loop)))
        if loop[1] == "ADP" :
            adp_array.append((loop[0] ,spacy_filtered_pos_tags.index(loop)))
        if loop[1] == "NOUN":
            noun_array.append((loop[0], spacy_filtered_pos_tags.index(loop)))
        if loop[1] == "PRON":
            pronoun_array.append((loop[0], spacy_filtered_pos_tags.index(loop)))
        if loop[1] == "ADV":    
            adv_array.append((loop[0] ,spacy_filtered_pos_tags.index(loop)))
        
    print(Verb_array, conjuctions_array , noun_array, adp_array, pronoun_array)
    if len(Verb_array) != 0:
        if len(Verb_array) == 1:
            pass
        if len(Verb_array) == 2 and len(conjuctions_array)!=0:
            
            pass








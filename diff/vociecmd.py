import spacy , stanfordnlp , sys
nlp1 , nlp2 = spacy.load('en_core_web_sm') ,stanfordnlp.Pipeline(processors='tokenize,pos', lang='en')
while True :
    sequence_of_POS = []
    #declaring variables
    filtered_present_commands = []
    command_sentence_prediction = ""
    #creating arrays
    verb_noun_adverb_presence = ['VERB','NOUN','ADP']
    verb_positions , adverb_positions , noun_positions = [] ,[] , []
    verb_name_position = []
    cmd_pattern_1 ,cmd_pattern_2  = [],[]
    conjuction_presence = []
    #taking input
    texts = input("Enter a sentence ").strip()
    while texts == "" :
        texts = input("Enter a sentence ").strip()
    if texts == "exit":
        sys.exit(0)
    #processing input
    doc ,doc2 = nlp1(texts),nlp2(texts)
    spacy_pos_tags = [(token.text, token.pos_) for token in doc]
    stanford_nlp_postags = [(word.text, word.pos) for sentence in doc2.sentences for word in sentence.words]
    spacy_filtered_pos_tags = [(token.text, token.pos_) for token in doc if token.pos_ not in ["DET", "INTJ","SCONJ"]]
    stanford_filtered_pos_tags = [(word.text, word.pos) for sentence in doc2.sentences for word in sentence.words if word.pos not in ["DT", "UH"]]
    
    count1 = 0
    for i in spacy_filtered_pos_tags:
        sequence_of_POS.append(i[1])
        if i[1] in verb_noun_adverb_presence :
            if i[1]=="VERB":
                verb_positions.append(count1)
                verb_name_position.append(i)
            if i[1]=="NOUN":
                noun_positions.append(count1)
            if i[1]=="ADP" :
                adverb_positions.append(count1)
            cmd_pattern_1.append(i[1])
        count1+=1
        if  "CCONJ" in i[1] :
            conjuction_presence.append(i[1])


    if len(conjuction_presence) == 0:
        remove_count = 0
        if "VERB" in sequence_of_POS and "NOUN" in sequence_of_POS and ("ADP" in sequence_of_POS or "ADV" in sequence_of_POS):
            for i in spacy_filtered_pos_tags:
                if i[1] == 'ADP' or i[1] == "ADV" :
                    if spacy_filtered_pos_tags.index(i) < spacy_filtered_pos_tags.index(verb_name_position[0]):
                        spacy_filtered_pos_tags.remove(i)
                        remove_count+=1
                        verb_positions = [x + (-1) for x in verb_positions]
                        if i[1]=="ADP":
                            adverb_positions.pop[0]
                        else:
                            pass




                        
            print(spacy_filtered_pos_tags)
            if ("VERB" == spacy_filtered_pos_tags[verb_positions[0]][1] and "NOUN" == spacy_filtered_pos_tags[verb_positions[0]+1][1] and "ADP" == spacy_filtered_pos_tags[verb_positions[0]+2][1]) or ( "VERB" == spacy_filtered_pos_tags[verb_positions[0]][1] and "NOUN" == spacy_filtered_pos_tags[verb_positions[0]+2][1] and "ADP" == spacy_filtered_pos_tags[verb_positions[0]+1][1]):
                command_sentence_prediction="True"
                for j in spacy_filtered_pos_tags:
                   pass
            else:
                print("----",spacy_filtered_pos_tags,"----")
    #now classifying the sentences using patterns
    print(command_sentence_prediction)
    print("---------------")
    print(sequence_of_POS)
    #printing pos and filtered pos array
    print(spacy_pos_tags)
    #print(stanford_nlp_postags)
    print(spacy_filtered_pos_tags)
    #print(stanford_filtered_pos_tags)
    print(cmd_pattern_1)
    print(f"verb present {verb_positions}")
    print(f"conjuction present {conjuction_presence}")
    print(f"vna presence {verb_noun_adverb_presence}")
    print(f"position of verbs are {verb_positions}\n position of nouns are {noun_positions}\n and position of adverbs are {adverb_positions}")
    print("---------------")
            

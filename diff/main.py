import spacy
import stanfordnlp
nlp2 = stanfordnlp.Pipeline(processors='tokenize,pos', lang='en')
nlp = spacy.load('en_core_web_sm')
import joblib
a ={}
auxandall=[]
while True:
    present_cmd = []
    sentence = input("Enter any sentence to get part of speech : ")
    pro_noun_between_verb_and = []
    propernoun_location = []
    doc = nlp(sentence)
    pos_tags = [(token.text, token.pos_) for token in doc]
    a[sentence] = pos_tags
    print(pos_tags)
    for i in pos_tags:
        if i[1]=="DET" or i[1] == "INTJ" :
            print()
            pos_tags.remove(i)
    print(pos_tags)
    count = 0
    z = ""
    occrofverbs = []
    for i in range(0,len(pos_tags)):
        if pos_tags[i][1]=='VERB':
            print(i)
            occrofverbs.append(i)
        if pos_tags[i][1]=="VERB" :
            present_cmd.append("v")
        if pos_tags[i][1]=="NOUN" :
            present_cmd.append("n")
        if pos_tags[i][1]=="ADP" :
            present_cmd.append("a")
        if pos_tags[i][1]=="PRON" :
            pro_noun_between_verb_and.append(i)
        if pos_tags[i][1]=="PROPN" :
            propernoun_location.append(i)
    print(f"the location of pronoun is {i} and verb is {occrofverbs}")
    for d in occrofverbs :
        print(present_cmd)
        if len(present_cmd) == 1:
                print(present_cmd)
                pass
        elif len(present_cmd) == 3 :
                if (pos_tags[d][1] == "VERB" and pos_tags[d+1][1] == 'NOUN' and pos_tags[d+2][1] == 'ADP') or (pos_tags[d][1] == "VERB" and pos_tags[d+2][1] == 'NOUN' and pos_tags[d+1][1] == 'ADP'):
                    if d !=0:
                        for partspeech in auxandall: 
                            pass
                    z = "command present (use of verb noun and adverb )"
                else:
                    z = "command not present"

        else :
            if len(present_cmd) == 2:
                    if pos_tags[d][1]=="VERB" and pos_tags[d+1][1]=="NOUN" :
                        z = 'command present (use of verb and noun)'
                    else :
                        z = "command not present"
            else:
                pass
    stanl = []
    sentence_recheck = ""
    if len(present_cmd) == 1 :
        print("here we use stanford")
        doc = nlp2(sentence)
        for sentence in doc.sentences:
            for word in sentence.words:
                stanl.append((word.text, word.pos))
        print(len(stanl))
        for i in range(0,len(stanl)):
            if stanl[i][1]=="DT" or stanl[i][1]=="UH":
                print('hello')
                stanl.pop(i)
        for  i in stanl:
            sentence_recheck += i[0] + " "
            
        doc2 = nlp2(doc2.sentence_recheck)
        for word in doc2.sentences:

        print(stanl)
    print(z)
    

    


    

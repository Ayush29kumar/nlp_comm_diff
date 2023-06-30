from textblob import TextBlob
while True :
    text = input("enter a sentence ")
    # Create a TextBlob object
    blob = TextBlob(text)

    # Perform POS tagging
    pos_tags = blob.tags

    # Print the POS tags
    for word, tag in pos_tags:
        print(word, tag)

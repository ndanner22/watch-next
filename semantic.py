import spacy # import spacy module

nlp = spacy.load('en_core_web_md') # run 'en_core_web_md' model

# save nlp verion of below string to variable 'tokens'
tokens = nlp('cat apple monkey banana ')

# for loop through tokens
for token1 in tokens:
    # for loop through tokens a second time
    for token2 in tokens:
        # print text of token1, text of token2, and the results of running .similarity() of token1 with token2
        print(token1.text, token2.text, token1.similarity(token2))
print()
# save below string to variable 'sentence_to_compare'
sentence_to_compare = "Why is my cat on the car"
# create list variable 'sentences' and add the below five strings to the list
sentences = ["where did my dog go","Hello, there is my car","I\'ve lost my car in my car","I\'d like my boat back","I will name my dog Diana"]
# create variable 'model_sentence' and save nlp version of sentence_to_compare to variable
model_sentence = nlp(sentence_to_compare)
# for loop through sentences
for sentence in sentences:
    # create variable similarity and save result of running .similarity() of nlp version of current value of sentences with model_sentence
    similarity = nlp(sentence).similarity(model_sentence)
    # print current value of sentences and current value of similarity
    print(sentence +" - ",similarity)



# it is interesting to me that the similarity function recognises a relationship between monkey and banana

'''it's also interesting that apple doesn't have more of a similarity with monkey and cat. Being a food item,
even though it is not popular with cats and monkeys, I would have thought it was more similar'''

'''when I ran this program with 'en_core_web_sm' it gave me the following warning - The model you're using has no word 
vectors loaded, so the result of the Token.similarity method will be based on the tagger, parser and NER, which may not 
give useful similarity judgements. As a result of not having any word vectors loaded, the similarity results are completely
different and don't make a lot of sense.'''
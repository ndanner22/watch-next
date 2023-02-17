import spacy # import spacy module

nlp = spacy.load('en_core_web_md') # run 'en_core_web_md' model

# create variable 'hulk_syn' and save description of Planet Hulk to variable
hulk_syn = "Will he save their world or destory it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."
# save nlp verion hulk_syn to hulk_syn
hulk_syn = nlp(hulk_syn)

# define function 'gen_next'
def gen_next():
    # read movies.txt into variable 'file'
    file = open("movies.txt", "r")
    # create variable 'reviews' and read lines of file into the new variables
    reviews = file.readlines()
    # create variable 'sim' set to value of 0
    sim = 0
    # for loop through reviews
    for review in reviews:
        # strip current value of reviews and save to new variable 'temp'
        temp = review.strip()
        # split temp by a colon and resave to variable temp
        temp = temp.split(":")
        # create variable 'similarity' and save result of running .similarity() of nlp version of current value of temp at index 1 with hulk_syn
        similarity = nlp(temp[1]).similarity(hulk_syn)
        # if the value of similarity cast a float is greater than current value of sim
        if float(similarity) > sim:
            # set value of sim to similarity cast as a float
            sim = float(similarity)
            # create new variable 'title' and set equal to value of temp at index 0
            title = temp[0]
    print()
    # print the below string along with variable title, which is the title of the most similar movie from movies.txt and Plant Hulk
    print(f"Based on your watching of Planet Hulk, you should now watch {title}.")
    print()
    # close file movies.txt
    file.close()
    return
# run function gen_next
gen_next()
import nltk
from nltk.corpus import conll2000

# Experiment: Apply k-inference algorithm on POS tags for Noun Phrases (NP) found in the CONLL2000 Corpus

test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])


######## Extract NP chunks ###############
def get_np_chunks(test_sents, np_chunks):
    for s in test_sents:
        if is_np(s):
            np_chunks.append(s)


# returns true if chunk is a tree. Since we only use NP chunk types [see line 8] it returns true if it is NP chunk
def is_np(s):
    return type(s) == nltk.tree.Tree


########## Extract POS tags ###########
np_pos = []


def get_np_pos(np_chunks, np_pos):
    for t in np_chunks:
        traverse(t, np_pos)

    np_pos_str = []
    for pos_list in np_pos:
        str = pos_to_str(pos_list)
        if str != '' and len(str.split(" ")) > 1 and all(x.isalpha() or x.isspace() for x in str):
            np_pos_str.append(str)

    return np_pos_str


# traverses the tree and gets pos tags
def traverse(t, np_pos):
    try:
        t.label()
    except AttributeError:
        if type(t) == tuple:
            (t, pos) = t
            np_pos[len(np_pos) - 1].append(str(pos))

    else:
        # Now we know that t.node is defined
        # print "label"
        # print(t.label())
        np_pos.append([])
        for child in t:
            traverse(child, np_pos)


def pos_to_str(pos_list):
    str = ""
    for pos in pos_list:
        if pos != '.' and pos != ',':
            str += pos
            str += " "

    return str[:-1]


########## GET SAMPLE ########################
def get_sample(test_sents):
    np_chunks = []
    get_np_chunks(test_sents, np_chunks)

    np_pos = []

    return get_np_pos(np_chunks, np_pos)


###### TEST ##########
# get_np_chunks(test_sents, np_chunks)

# S = get_np_pos(np_chunks, np_pos)
corpus = ""
S = get_sample(test_sents)

########### Create and Read file into array ###########
for l in S:
    spl = l.split(" ")
    for i in xrange(len(spl)):
        corpus += spl[i]
        if i != len(spl) - 1:
            corpus += " "
    corpus += ";"


def get_corpus(filename):
    S = []
    f = open(filename, 'r')

    line = f.readline()
    while line is not None:
        split = line.split(";")
        for entry in split:
            S.append(entry)
        line = f.readline()
    return S

# Implementation of the algorithms described by Dr. Dana Angluin in her paper Inference of Reversible Languages (1982)

import copy
import numpy as np
import CONLL2000Experiments as conll
import inference as inf
import sys


# Inputs:
# fname - the name of the file with the strings separated by ';'
# k - the variable for the k-inference algorithm
def main(fname, k):
    S = inf.get_corpus(fname)
    inf.k_RI(S, k)

fname = sys.argv[1]
k = sys.argv[2]
main(fname, k)

################ TESTING ########################################
S = ["Mary bakes cakes", "John bakes cakes", "Mary eats pies", "Mary bakes pies", "Mary bakes"]

aux_data = ["Judy gives bread", "Judy is giving bread", "Judy has given bread", "Judy has been giving bread",
            "Judy gave bread", "Judy was giving bread", "Judy had given bread", "Judy had been giving bread",
            "Judy does give bread", "Judy did give bread", "Judy can give bread", "Judy can be giving bread",
            "Judy can have given bread", "Judy can have been giving bread", "Judy could give bread",
            "Judy could be giving bread", "Judy could have given bread", "Judy could have been giving bread",
            "Judy may give bread", "Judy may be giving bread", "Judy may have given bread",
            "Judy may have been giving bread", "Judy might give bread", "Judy might be giving bread",
            "Judy might have given bread", "Judy might have been giving bread", "Judy must give bread",
            "Judy must be giving bread", "Judy must have given bread", "Judy must have been giving bread",
            "Judy shall give bread", "Judy shall be giving bread", "Judy shall have given bread",
            "Judy shall have been giving bread", "Judy should give bread", "Judy should be giving bread",
            "Judy should have given bread", "Judy should have been giving bread", "Judy will give bread",
            "Judy will be giving bread", "Judy will have given bread", "Judy will have been giving bread",
            "Judy would give bread", "Judy would be giving bread", "Judy would have given bread",
            "Judy would have been giving bread", "Judy is given bread", "Judy is being given bread",
            "Judy has been given bread", "Judy has been being given bread", "Judy was given bread",
            "Judy was being given bread", "Judy had been given bread", "Judy had been being given bread",
            "Judy does get given bread", "Judy did get given bread", "Judy can be given bread",
            "Judy can be being given bread", "Judy can have been given bread", "Judy can have been being given bread",
            "Judy could be given bread", "Judy could be being given bread", "Judy could have been given bread",
            "Judy could have been being given bread", "Judy may be given bread", "Judy may be being given bread",
            "Judy may have been given bread", "Judy may have been being given bread", "Judy might be given bread",
            "Judy might be being given bread", "Judy might have been given bread",
            "Judy might have been being given bread", "Judy must be given bread", "Judy must be being given bread",
            "Judy must have been given bread", "Judy must have been being given bread",
            "Judy shall be given bread", "Judy shall be being given bread", "Judy shall have been given bread",
            "Judy shall have been being given bread", "Judy should be given bread", "Judy should be being given bread",
            "Judy should have been given bread", "Judy should have been being given bread", "Judy will be given bread",
            "Judy will be being given bread", "Judy will have been given bread",
            "Judy will have been being given bread",
            "Judy would be given bread", "Judy would be being given bread", "Judy would have been given bread",
            "Judy would have been being given bread"]
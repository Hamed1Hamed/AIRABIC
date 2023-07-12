# -*- coding: utf-8 -*-

import gensim
from gensim.models import Word2Vec
import gensim
import re
import numpy as np
from nltk import ngrams
from Utilities import *

with open('model_path.txt', 'r') as f:
    path = f.readline().strip()  # .strip() removes the newline character at the end

model = gensim.models.Word2Vec.load(path)

def word2Vectector(word1,word2):
    # Replace "path/to/model" with the path of the pre-trained AraVec model

    # word1 = "فَتَحَ"
    # word2 = "فتح"

    if word1 in model.wv:
        print(f"The vector representation of the word '{word1}' is:\n{model.wv[word1]}")
    else:
        print(f"The word '{word1}' is not in the model's vocabulary.")

    print("---------------------------------------------------------------------------------------------------------------------------")

    if word2 in model.wv:
        print(f"The vector representation of the word '{word2}' is:\n{model.wv[word2]}")
    else:
        print(f"The word '{word2}' is not in the model's vocabulary.")



def obtainSimmilarWords(word):
    token = clean_str(f'{word}').replace(" ", "_")

    if token in model.wv:
        most_similar = model.wv.most_similar( token, topn=10 )
        for term, score in most_similar:
            term = clean_str(term).replace(" ", "_")
            if term != token:
                print(term, score)

    word_vector = model.wv[ token ]

# # Let's assume the word you want to embed is "كتاب" which means "book"
# word = "كتاب"
#
# # Check if the word is in the vocabulary
# if word in aravec.wv.key_to_index:
#     vector = aravec.wv[word]
#     print(f"The vector representation of the word '{word}' is:")
#     print(vector)
# else:
#     print(f"The word '{word}' does not exist in the model vocabulary.")

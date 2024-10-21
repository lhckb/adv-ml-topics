import math
import re

def td_idf(word_count, all_doc_words, total_docs, all_docs_word):
    tf = word_count / all_doc_words
    idf = math.log10(total_docs / all_docs_word)

    return tf * idf

doc1 = "O gato subiu no tapete"
doc2 = "O gato perseguiu o rato"
doc3 = "O cachorro perseguiu o rato"

all_tokens = {}
bows = []

for doc in [doc1]:
    doc = doc.lower()

    bow = {}
    
    for token in doc.split(" "):
        all_tokens[token] = 0
        # bow[token] = doc.count(token)
        bow[token] = len(re.findall(token, doc))
    bows.append(bow)
    del bow
        # try:
        #     bow[i][token] = bow[i][token] + 1    
        # except:

    # print(all_tokens)
    print()
    print(bows)
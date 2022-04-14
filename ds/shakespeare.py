


# %%
import os, re
import numpy as np
import tensorflow as tf


# %%
file_path = '../data/shakespeare.txt'
with open(file_path, 'r') as f:
    raw_corpus = f.read().splitlines()

print(raw_corpus[:9])

# %%

for idx, sentence in enumerate(raw_corpus):
    if len(sentence) == 0: continue
    if sentence[-1] == ":": continue
    if idx > 9: break

    print(sentence)
# %%
def preprocess_sentence(sentence):
    sentence = sentence.lower().strip()
    sentence = re.sub(r"([?.!,])", " ", sentence)
    sentence = re.sub(r'[" "]+'," ", sentence)
    sentence = re.sub(r"[^a-zA-Z?.!,]+", " ", sentence)
    sentence = sentence.strip()
    sentence = '<start> ' + sentence + ' <end>'
    return sentence

print(preprocess_sentence("This is @;;; sample sentence."))
# %%
corpus = []

for sentence in raw_corpus:
    if len(sentence)==0: continue
    if sentence[-1] == ":": continue

    preprocessed_sentence = preprocess_sentence(sentence)
    corpus.append(preprocessed_sentence)

print(corpus[:10])
# %%

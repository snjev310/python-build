#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 16:49:01 2019

@author: aditya
"""

from nltk.corpus import reuters 
from nltk import word_tokenize
from nltk.stem.porter import PorterStemmer
import re
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

stopwordsList = stopwords.words("english")

def tokenize(text):
    min_length = 3
    words = map(lambda word: word.lower(), word_tokenize(text));
    words = [word for word in words if word not in stopwordsList]
    tokens =(list(map(lambda token: PorterStemmer().stem(token), words)));
    p = re.compile('[a-zA-Z]+');
    filtered_tokens = list(filter(lambda token: p.match(token) and len(token)>=min_length, tokens));
    return filtered_tokens

# Return the representer, without transforming
def tf_idf(docs):
    tfidfVectorizer = TfidfVectorizer(tokenizer=tokenize, use_idf=True, sublinear_tf=True);
    matrix = tfidfVectorizer.fit_transform(docs);
    return tfidfVectorizer, matrix;

def transform_query(query, tfidfVectorizer):
    query_trans = tfidfVectorizer.transform([query])
    return query_trans

def get_train_test_reauter_data():
    train_docs = []
    test_docs = []
    
    for doc_id in reuters.fileids():
        if doc_id.startswith("train"):        
            train_docs.append(reuters.raw(doc_id))
        else:
            test_docs.append(reuters.raw(doc_id))
    
    sliceObject = slice(5)	
    train_docs = train_docs[sliceObject]
    test_docs = test_docs[sliceObject]
    return train_docs, test_docs


dataset = ['A Course on Integral Equations',
'Attractors for Semigroups and Evolution Equations',
'Automatic Differentiation of Algorithms, Theory, Implementation and Application',
'Geometrical Aspects of Partial Differential Equations',
'Ideals, Varieties, and Algorithms: An Introduction to Computational Algebraic Geometry and Commutative Algebra',
'Introduction to Hamiltonian Dynamical Systems and the N-Body Problem',
'Knapsack Problems: Algorithms and Computer Implementations',
'Methods of Solving Singular Systems of Ordinary Differential Equations',
'Nonlinear Systems',
'Ordinary Differential Equations',
'Oscillation Theory for Neutral Differential Equations with Delay',
'Oscillation Theory of Delay Differential Equations',
'Pseudo differential Operators and Nonlinear Partial Differential Equations',
'Since Methods for Quadrature and Differential Equations',
'Stability of Stochastic Differential Equations with Respect to Semi-Martingales',
'The Boundary Integral Approach to Static and Dynamic Contact Problems',
'The Double Mellin-Barnes Type Integrals and Their Applications to Convolution Theory']



#train_docs, test_docs = get_train_test_reauter_data()
train_docs = dataset
def main():        
    tfidfVectorizer, tfidfmatrix = tf_idf(train_docs)
    tfidfmatrix = (tfidfmatrix.toarray()).T
    u,s,v = np.linalg.svd(tfidfmatrix)
    #print(tfidfVectorizer.vocabulary_)
    print(s)
    k = 7
    uk = u[:,0:k]
    sk = np.diag(s[0:k])
    vk = v[0:k,:]
    query = 'Differential'
    queryT = transform_query(query, tfidfVectorizer).toarray()
    #print(queryT)
    queryK = np.dot(np.dot(queryT, uk), np.linalg.inv(sk))
    
    score = np.dot(queryK, vk)[0]
    sorted_doc = sorted(range(len(score)), key=lambda k: score[k], reverse = True)
    sorted_doc = [n+1 for n in sorted_doc]
    #print(score)
    print(sorted_doc)

main()


#for doc in test_docs:
#    print(feature_values(doc, tfidfVectorizer))


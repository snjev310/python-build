#!/usr/bin/env python
# coding: utf-8

# In[133]:


from nltk.corpus import reuters 
from nltk import word_tokenize
from nltk.stem.porter import PorterStemmer
import re
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import matplotlib.pyplot as plt


# In[134]:


stopwordsList = stopwords.words("english")
def tokenize(text):
    min_length = 3
    words = map(lambda word: word.lower(), word_tokenize(text));
    words = [word for word in words if word not in stopwordsList]
    tokens =(list(map(lambda token: PorterStemmer().stem(token), words)));
    p = re.compile('[a-zA-Z]+');
    filtered_tokens = list(filter(lambda token: p.match(token) and len(token)>=min_length, tokens));
    return filtered_tokens


# In[135]:


def tf_idf(docs):
    tfidfVectorizer = TfidfVectorizer(tokenizer=tokenize, use_idf=True, sublinear_tf=True);
    matrix = tfidfVectorizer.fit_transform(docs);
    return tfidfVectorizer, matrix;


# In[136]:


def transform_query(query, tfidfVectorizer):
    query_trans = tfidfVectorizer.transform([query])
    return query_trans


# In[137]:


def train_test_reuiter_data():
    train_doc = []
    test_doc = []
    
    for doc_id in reuters.fileids():
        if doc_id.startswith("training"):
            train_doc.append(reuters.raw(doc_id))
        else:
            test_doc.append(reuters.raw(doc_id))
    sliceObject = slice(5)
    train_doc = train_doc[sliceObject]
    test_doc = test_doc[sliceObject]
   # print('***********************************')
   # print(train_doc)
    #print('***********************************')
   # print(test_doc)
    return train_doc, test_doc


# In[138]:


def load_Adi_dataset():
    with open('ADI.ALL') as f:
        temp = []
        for l in f:
            temp.append(l.replace('\n',' '))
        training = ''.join(temp).replace('.T','').split('.I')
    with open('ADI.QRY') as f:
        temp = []
        for l in f:
            temp.append(l.replace('\n',' '))
        testing = ''.join(temp).replace('.W','').split('.I')
    del training[0]
    del testing[0]
    
    return training,testing;


# In[139]:


train_doc,test_doc = load_Adi_dataset()
def get_Rel_doc(query, k):
    tfidfVectorizer, tfidfmatrix = tf_idf(train_doc)
    tfidfmatrix = (tfidfmatrix.toarray()).T
    u,s,v = np.linalg.svd(tfidfmatrix)
#     print(u)
#     print(s)
#     print(v)
#     input()

    uk = u[:,0:k]
    sk = np.diag(s[0:k])
    vk = v[0:k,:]
    quertT = transform_query(query,tfidfVectorizer).toarray()
#     print(quertT)
#     print(np.dot(query, uk))
#     print(np.linalg.inv(sk))
    queryK = np.dot(np.dot(quertT, uk), np.linalg.inv(sk))
    
    score = np.dot(queryK, vk)[0]    #0the index because it is returning 2d type
    sorted_doc = sorted(range(len(score)), key=lambda k: score[k], reverse = True)
    sorted_doc = [n+1 for n in sorted_doc]
    return sorted_doc


# In[140]:


def load_actual_doc(queryFile):
    actual_rel_doc = []
    with open('ADI.REL') as f:
        for l in f:
            temp = l.split()
            if int(temp[0]) == queryFile:
                actual_rel_doc.append(int(temp[1]))
    print(actual_rel_doc)
    return actual_rel_doc


# In[141]:


def getPrecision(k):
    totalPrecison = 0
    for query_no in range(5):
        actual_rel_docs = load_actual_doc(query_no+1)
        
        predicted_rel_docs = get_Rel_doc(test_docs[query_no], k)
        #print(len(predicted_rel_docs))
        
        print(get_Rel_doc(test_docs[query_no], k))
        count = 0
        for doc_no in actual_rel_docs:
            if predicted_rel_docs.index(doc_no) < len(actual_rel_docs):
                count += 1
        totalPrecison +=count/len(actual_rel_docs)
    print('For K = {} average Precison is {}'.format(k,totalPrecison/5))
    return totalPrecison/5
           
X = list(range(0, len(train_docs), 5))       
Y = list(map(getPrecision,X))

Y = [i*100 for i in Y]
plt.plot(X, Y)


# In[ ]:





import re
import os
import string
from nltk.tokenize import word_tokenize
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

#Creating a list of document ids
doc_no=[]
#Creating a list of words in the documents
words=[]

#Opening the corpus and reading the file
f=open('./Text_corpus/wiki_00', 'r' , encoding='utf8')
content = f.read()
content=str(content)

#Removing <a>...</a> tags
pattern = re.compile("<(/)?a[^>]*>")
content_new = re.sub(pattern,"", content)

#Creating a folder to hold the seperated documents
if not os.path.exists("./Documents") :
    os.mkdir ("./Documents")

#Creating a soup using a html parser and iterating through each 'doc'
soup=BeautifulSoup(content_new,'html.parser')
for doc in soup.findAll('doc'):
    #Opening a file to write the contents of the doc
    o=open('./Documents/'+str(doc['id'])+".txt",'w', encoding='utf8')
    doc_no=doc_no+[(int(doc['id']))]
    text=doc.get_text()

    #Making all the text lowercase
    text=text.lower()

    #Replaces punctuations with spaces
    text=text.translate(str.maketrans(string.punctuation, ' '*len(string.punctuation)))
    #Removes weird punctuations. Add a sapce and symbol you want to replace respectively
    text=text.translate(str.maketrans("‘’’–——−",'       '))

    #Tokeinzing word from the doc and adding it to 'words' dictionary 
    words=words+word_tokenize(text)

    #Eliminating the duplicate words
    words=list(set(words))

    #Writing the text and closing the file
    o.write(doc.get_text())
    o.close()

df=pd.DataFrame(index=doc_no,column=)
#print(doc_no)
#print(sorted(words))
#print(len(words))

f.close()
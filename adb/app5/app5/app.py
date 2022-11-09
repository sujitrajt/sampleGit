from flask import Flask,render_template,request
import nltk
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
from nltk import word_tokenize
import string

stmr=SnowballStemmer("english")

def indexing1(text):
    #splitting the text to sentences
    sent_text = nltk.sent_tokenize(text) 
    # cleaning the text by removing punctuation and stop words
    stop = set(stopwords.words('english') + list(string.punctuation))

    ##preparing a index by stemming and tokenizing the sentence
    data = list()
    for s in sent_text:
        temp = dict()
        temp['sent'] = s
        words = [i for i in word_tokenize(s.lower()) if i not in stop]
        temp1 = list()
        for w in words: 
            temp1.append(stmr.stem(w))  
        temp['words'] = temp1  
        data.append(temp)
    return data
    

#reading the data from file in lower case
index1 = list()
f = open("Alice.txt", "r", encoding="utf-8")
text = f.read()
index1 = index1 + indexing1(text)
with open('index1.txt','w') as file:
    file.write(str(index1))

f = open("Shakespeare-100-0.txt", "r", encoding="utf-8")
text = f.read()
index1 = index1 + indexing1(text)
with open('index1.txt','w') as file:
    file.write(str(index1))

app = Flask(__name__)

@app.route("/")
def task1():
    return render_template("task1.html")

@app.route("/result1", methods=["GET","POST"])
def result1():
    formdata = dict(request.form)
    text = formdata['text'].lower()
    wor = indexing1(text)[0]
    print(wor)
    final1 = list()
    #searching through the index
    for t in index1:
        #logic to match the search words with index
        match1 = list()
        for j in wor['words']:
            for i in t['words']:
                if j==i:
                    match1.append(j)
                    break
        print(match1)
        if(len(wor['words'])==len(match1)):
            final1.append(t['sent'])
    print(len(final1))
    
    return render_template("result1.html", data=final1, count=len(final1))       

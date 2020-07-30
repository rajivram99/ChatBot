

import nltk
import numpy as np
import random
import string # to process standard python strings
import sys

import warnings
warnings.filterwarnings("ignore")

nltk.data.path.append("nltk_data")

f=open('chat.txt','r')
raw=f.read()
raw=raw.lower()# converts to lowercase


sent_tokens = nltk.sent_tokenize(raw)# converts to list of sentences 
word_tokens = nltk.word_tokenize(raw)# converts to list of words

lemmer = nltk.stem.WordNetLemmatizer()
#WordNet is a semantically-oriented dictionary of English included in NLTK.
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey",)
GREETING_INPUTS1 = ("Who Are You","who are you","who are you?,")
GREETING_RESPONSES = ["\nHi, Welcome to BITSathy","\nHello, Welcome to BITSathy"]
GREETING_RESPONSES1 = ["\nHi,Iam Bit-ChatBot","\nHello,Iam Bit-ChatBot"]

def greeting(sentence):
 
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)
        elif word.lower() in GREETING_INPUTS1:
            return random.choice(GREETING_RESPONSES1)
	        
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def response(user_response):
    robo_response=''
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
 
    if(req_tfidf==0):
        robo_response=robo_response+"\nI am sorry! I don't understand you"
        return robo_response
    else:
        robo_response = robo_response+sent_tokens[idx]
        robo_response = robo_response.split("\n",1)[1]
        return robo_response.capitalize()
    
flag=True


user_response = ""
for n in range(1,len(sys.argv)):
  user_response +=" "
  user_response += str(sys.argv[n])
#user_response=input("")
user_response=user_response.strip()
user_response=user_response.lower()
if(user_response!='bye'):
	if(user_response=='thanks' or user_response=='thank you' ):
		flag=False
		print("\nYou are welcome..")
	else:
		if(greeting(user_response)!=None):
			print(greeting(user_response))
		else:
			sent_tokens.append(user_response)
			word_tokens=word_tokens+nltk.word_tokenize(user_response)
			final_words=list(set(word_tokens))
			#print("BITBOT: ",end="")
			print(response(user_response))
			#print(user_response)
			sent_tokens.remove(user_response)
else:
	flag=False
	print("\nBye! take care..")

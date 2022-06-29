#pip install tensorflow==1.2
#pip install numpy==1.14.2
#pip install tflearn
#pip install windows-curses
#pip install nltk
#nltk.download('punkt')
#pip install firebase-admin
#pip install json
#pip install keyboard


import nltk
import pickle
import numpy
import tflearn
import tensorflow
import random
import json
import os
import firebase_admin
from googletrans import Translator
from firebase_admin import credentials,db
import speech_recognition as sr
from gtts import gTTS


os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

translator = Translator()
from nltk.stem.lancaster import LancasterStemmer

stemmer = LancasterStemmer()

with open("voice data.json") as file:
    data = json.load(file)



try:
    with open("data.pickle", "rb") as f:
        words, labels, training, output = pickle.load(f)
except:
    words = []
    labels = []
    docs_x = []
    docs_y = []
    continuation = []

    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            wrds = nltk.word_tokenize(pattern)
            words.extend(wrds)
            docs_x.append(wrds)
            docs_y.append(intent["tag"])

        if intent["tag"] not in labels:
            labels.append(intent["tag"])

    words = [stemmer.stem(w.lower()) for w in words if w != "?"]
    words = sorted(list(set(words)))

    labels = sorted(labels)

    training = []
    output = []

    out_empty = [0 for _ in range(len(labels))]

    for x, doc in enumerate(docs_x):
        bag = []

        wrds = [stemmer.stem(w.lower()) for w in doc]

        for w in words:
            if w in wrds:
                bag.append(1)
            else:
                bag.append(0)

        output_row = out_empty[:]
        output_row[labels.index(docs_y[x])] = 1

        training.append(bag)
        output.append(output_row)

    training = numpy.array(training)
    output = numpy.array(output)

    with open("../data.pickle", "wb") as f:
        pickle.dump((words, labels, training, output), f)

tensorflow.reset_default_graph()

net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)

if os.path.exists("../model.tflearn.meta"):
    model.load("model.tflearn")
else:
    model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
    model.save("model.tflearn")


    def bag_of_words(s, words):
        bag = [0 for _ in range(len(words))]

        s_words = nltk.word_tokenize(s)
        s_words = [stemmer.stem(word.lower()) for word in s_words]

        for se in s_words:
            for i, w in enumerate(words):
                if w == se:
                    bag[i] = 1

        return numpy.array(bag)

cred = credentials.Certificate('firebase-json.json')

firebase_admin.initialize_app(cred,{
    'databaseURL': 'https://my-ai-81afb.firebaseio.com/'
})

def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1

    return numpy.array(bag)

def recreatedChat():
        print("Use phone to speak your command")
        ref2 = ''
        while True:
            # Read input from DB
            ref = db.reference('My input/input')


            ref1 = ref.get()
            if ref1 != ref2:
                recieved_text = ref1
                trans_text = translator.translate(recieved_text)
                inp = trans_text.text
                if ref1.lower() == "quit":
                    break
                results = model.predict([bag_of_words(inp, words)])
                results_index = numpy.argmax(results)
                tag = labels[results_index]

                for tg in data["intents"]:
                 if tg['tag'] == tag:
                     responses = tg['response']

                upload_response = random.choice(responses)
                # datafile = "testing"
                # numberfile = 54
                # addon = upload_response + datafile
                print(upload_response)
                # print(addon)

                # Upload data to DB
                ref = db.reference('AI output')
                ref.update({
                    'output': upload_response
                    # 'output': addon
                })

                ref2 = ref1

recreatedChat()





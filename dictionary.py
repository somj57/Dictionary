'''
pip3 install flask
How to run????
open terminal
type
export FLASK_APP=dictionary.py

export FLASK_ENV=development

flask run

'''

from flask import Flask, render_template, url_for , request,redirect
import json
import difflib
import smtplib
list1= ['a','b']
data = json.load(open('data.json'))

app = Flask(__name__)
print(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods = ['POST','GET'])
def answer():
    data = request.form.to_dict()
    word1 = data["letter"]
    print(word1)
    list1= translate(word1)
    return render_template("index.html", var1=list1[0],var2=list1[1])





def translate(word):
    word = word.lower()
    if word in data:
        disp = [word]
        men = data[word]
        com=[disp,men]
        return com
    else:
        word1 = difflib.get_close_matches(word, data.keys())
        if len(word1)>0:
            
            disp =[f"Did you mean {word1[0].capitalize()}? Showing search for {word1[0].capitalize()}"]
            men = [disp,data[word1[0]]]
            return men
        else:
            #print("Word dosent exists  . . . .")
            return [['Try entering something else '],['']]
'''
print('Enter /end to exit')
while True:
    i=1
    word = input("Enter Word : ")
    if word == '/end':
        break
    out = translate(word)
    for dat in out:
        print(f"{i}: {dat}")
        i=i+1
'''
'''
pip3 install flask
How to run????
open terminal
type
export FLASK_APP=server.py

export FLASK_ENV=development

flask run

'''

from flask import Flask, render_template, url_for , request,redirect
import json
import difflib
import smtplib
list1= ['a','b']
data = json.load(open('data.json'))

app = Flask(__name__)
print(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods = ['POST','GET'])
def answer():
    data = request.form.to_dict()
    word1 = data["letter"]
    print(word1)
    list1= translate(word1)
    return render_template("index.html", var=list1)





def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    else:
        word1 = difflib.get_close_matches(word, data.keys())
        if len(word1)>0:
            #print(f"Did you mean {word1[0].capitalize()}? Showing search for {word1[0].capitalize()}")
            return data[word1[0]]
        else:
            #print("Word dosent exists  . . . .")
            return ['Try entering something else ']
'''
print('Enter /end to exit')
while True:
    i=1
    word = input("Enter Word : ")
    if word == '/end':
        break
    out = translate(word)
    for dat in out:
        print(f"{i}: {dat}")
        i=i+1
'''

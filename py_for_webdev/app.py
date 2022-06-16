# let's import the flask
from pickle import GET
from turtle import title
from webbrowser import get
from flask import Flask, render_template, request, redirect, url_for
import os # importing operating system module

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/') # this decorator create the home route
def home():
    techs = ['HTML', 'CSS', 'Flask', 'Python']
    name = 'Code'
    return render_template('home.html',techs=techs,name=name,title='Home')
    #return '<h1>Welcome<h1>'

@app.route('/about')# this line set the address
def about():
    name = 'Code'
    return render_template('about.html',name=name,title='About Us')
    #return '<h1>About us</h1>'

@app.route('/result/<content>')
def result(content):
    words = word_counter(content)
    top_10_words = word_useed(content)
    print(top_10_words)
    # for word in top_10_words:
    #     print(word[0])
    return render_template('result.html',content=content, words=words, top_10_words=top_10_words, mostF=top_10_words[0][0])

@app.route('/post', methods= ['GET','POST'])
def post():
    name = 'Text Analyzer'
    if request.method == 'GET':
        return render_template('post.html', name = name, title = name)
    if request.method == 'POST':
        content = request.form['content']
        if content != '':
            word_counter(content)
        #print(content)
            return redirect((f'/result/{content}'))
        else:
            return render_template('post.html', name = name, title = name)


def word_counter(content):
    list_of_word = content.split()
    return (len(list_of_word))
    #print(len(list_of_word))

def word_useed(content):
    words = dict()
    list_of_words = content.split()
    for word in list_of_words:
        if word not in words:
            words[word] = 1
        else:
            words[word] += 1
    words = dict(sorted(words.items(), key=lambda item: item[1],reverse=True)).items()
    return(list(words))




if __name__ == '__main__':
    port = int(os.environ.get("PORT",5000))
    app.run(debug=True,host='0.0.0.0',port=port)
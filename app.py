from flask import Flask, render_template, request, redirect
import requests
import json

app = Flask(__name__)

with open('rootdict121.json') as f:
    roots = json.load(f)

with open('static/lemmas12-2-20.json') as f:
    lemmas = json.load(f)

@app.route('/')
def index():
    rootfamilies = list(roots.keys())
    lengthdict = dict()
    for rf in rootfamilies:
        lengthdict[rf] = len(roots[rf])
    return render_template('index.html',rootfamilies=rootfamilies,lengthdict=lengthdict)

@app.route('/contents',methods=['GET','POST'])
def contents():
    if request.method == 'POST':
        rootfamily = request.form.get("rootfamily")
        rootlemmas = sorted(roots[rootfamily])
        print(rootlemmas)
        levellist = []
        for rootlemma in rootlemmas:
            for lemma in lemmas:
                if lemma['lemma'] == rootlemma:
                    levellist.append(lemma['level'])
        length = len(rootlemmas)
        print(levellist)
        return render_template('contents.html',rootlemmas=rootlemmas,rootfamily=rootfamily,levellist=levellist,length=length)
    if request.method == 'GET':
        rootfamilies = list(roots.keys())
        return render_template('index.html', rootfamilies=rootfamilies)

from flask import Flask
from flask import request
from flask import render_template
import requests
import json, urlparse
import random
import pymongo

# Yo Render page where it fetches random song from persisted list
app = Flask(__name__)
topsongList = []
toplistName = []
connx = ""

def displayDict(dictObj):
    for key, val in dictObj.items():
        print key, "::", val

def retRandomPlaylist(listObj):
    max = len(listObj)
    if max > 0:
     rndindex = random.randrange(0, max)
     return rndindex
    else:
     return "" 

def selectRandom(key):
    print "Select Random called"
    connx = pymongo.Connection()
    db = connx["playlist_db"]
    hdl = db["playlist"]
    # cursor = db.hdl.find_one({"list_theme":key})
    cur = hdl.find({"list_theme":key})
    for doc in cur:
      list1 = doc['list_uri']
      list2 = doc['list_name']
      print doc

    rndIndex = retRandomPlaylist(list1)

    randomPlaylistUri  = str(list1[rndIndex])
    randomPlaylistName = str(list2[rndIndex])
 
    return randomPlaylistUri, randomPlaylistName
 
def playlist_init():
    connx = pymongo.Connection()
    # try catch needed here
    db = connx["playlist_db"]
    hdl = db["playlist"]

    if hdl.count() == 0:
       hdl.drop()
       hdl.insert({"_id":"TOPSONGS", "list_theme":"TOPSONGS",  "list_uri": [], "list_name": ""})
       hdl.insert({"_id":"ROCKSONGS", "list_theme":"ROCKSONGS", "list_uri": [], "list_name": ""})
 
    print "Init List called" 
    for doc in hdl.find():
        print doc

@app.route('/')
@app.route('/index')
def index():
    # Render template
    name = request.args.get('username')
    user = {'nickname': name}  
    pl, name  = selectRandom("TOPSONGS")
    
    links = [
             { 'uri': pl, #'spotify:user:1210795004:playlist:2PbILT4LGTYzNkuqZkdFiH',
               'app_name': name
             },
            ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           links=links)

@app.route('/firebase')
def firebase():
    # Render template
    return render_template('firebase.html',
                           title='Home',
                          )

@app.route('/get_playlists',methods=['GET', 'POST'])
def get_playlists():
    data = request.data
    decoded_data = json.loads(data) 
    # Iterate this for all keyWords
    print decoded_data["Top"]
    topsongList = decoded_data["Top"] 
    toplistName = decoded_data["TopName"]

    if len(topsongList) > 0 and len(toplistName) > 0:
       connx = pymongo.Connection()
       # try catch needed here
       db = connx["playlist_db"]
       hdl = db["playlist"]

       hdl.save({"_id":"TOPSONGS", "list_theme":"TOPSONGS", "list_uri": topsongList, "list_name": toplistName})             
    return "OK"
 
if __name__ == "__main__":
    app.debug = True 
    playlist_init()
    app.run(host='0.0.0.0', port=9024)

# http client sends json object [u'spotify:user:spotify:playlist:3ZgmfR6lsnCwdffZUan8EA', u'spotify:user:spotify:playlist:4hOKQuZbraPDIfaGbM3lKI', u'spotify:user:spotify:playlist:5FJXhjdILmRA2z5bvz4nzf', u'spotify:user:spotify:playlist:6LBZwjKY0VZLoe79qeGcCF']. Now from this pick a random song

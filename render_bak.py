from flask import Flask
from flask import request
from flask import render_template
import requests
import json, urlparse
import random
# Yo Render page where it fetches random song from persisted list

app = Flask(__name__)
topsongList = []
toplistName = []

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

def readConf(fileName, listObj):
    f = open(fileName, 'r')
    for line in f:
      listObj.append(line)

    #print retRandomPlaylist(listObj)
    f.close()

def selectRandom(fileName, listObj):
    print "Select Random called"
    readConf(fileName, listObj)
    readConf('name.txt', toplistName)
    rnd_index = retRandomPlaylist(listObj)
    pl = listObj[rnd_index]
    print "Playlist:", pl
    return rnd_index    

@app.route('/')
@app.route('/index')
def index():
    # Render template
    name = request.args.get('username')
    user = {'nickname': name}  
    rnd_index = selectRandom('conf.txt', topsongList)
    global toplistName 
    pl = topsongList[rnd_index]
    name = toplistName[rnd_index]

    links = [
             { 'uri': pl, #'spotify:user:1210795004:playlist:2PbILT4LGTYzNkuqZkdFiH',
               'app_name': name
             },
            ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           links=links)

@app.route('/get_playlists',methods=['GET', 'POST'])
def get_playlists():
    data = request.data
    decoded_data = json.loads(data) 
    # Iterate this for all keyWords
    print decoded_data["Top"]
    topsongList = decoded_data["Top"] 
    toplistName = decoded_data["TopName"]

    fd = open("conf.txt", "w")
    for x in topsongList:
      fd.write(x)
      fd.write('\n')
   
    fd.close()
    
    fd = open("name.txt", "w")
    for x in toplistName:
      fd.write(x)
      fd.write('\n')
    
    fd.close()

    print "namelist", toplistName[:]

    return "OK"
 
if __name__ == "__main__":
    app.debug = True 
    print selectRandom('conf.txt', topsongList)
    app.run(host='0.0.0.0', port=9024)

# http client sends json object [u'spotify:user:spotify:playlist:3ZgmfR6lsnCwdffZUan8EA', u'spotify:user:spotify:playlist:4hOKQuZbraPDIfaGbM3lKI', u'spotify:user:spotify:playlist:5FJXhjdILmRA2z5bvz4nzf', u'spotify:user:spotify:playlist:6LBZwjKY0VZLoe79qeGcCF']. Now from this pick a random song

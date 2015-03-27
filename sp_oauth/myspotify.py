import sys
import spotipy
import spotipy.util as util
import tmp
import random
import requests
import json, urllib, urllib2

#To Run: python myspotify.py 1210795004

scope = 'user-library-read'
playListMap = {}  # <Keyword, PlaylistObject> Mapping
topSongList = []  # List Object for storing TopSong Playlist Uri
topListName = []  # List Object for storing TopSong Playlist Names

render_url = "http://5.152.179.176:9024/get_playlists"

def addPlaylist(listObj, pl):
    listObj.append(pl)

def displayPlaylist(listObj):
    print listObj[:]

def displayDict(dictObj):
    for key, val in dictObj.items():
        print key, "::", val

def retRandomPlaylist(listObj):
    max = len(listObj)
    rndindex = random.randrange(0, max)
    return listObj[rndindex]

if __name__ == "__main__":
  playListMap = {"Top":topSongList, "TopName": topListName, "Rock":''}
  sessKeyWord = "Top"

  if len(sys.argv) > 1:
    username = sys.argv[1]
  else:
    print "Usage: %s username" % (sys.argv[0],)
    sys.exit()

  token = tmp.prompt_for_user_token(username, scope)

  if token:
    sp = spotipy.Spotify(auth=token)

    results = sp.user_playlists(username, limit=10)

    for item in results['items']:
        if item['name'].find(sessKeyWord) != -1:
           print item['name']
           addPlaylist(topSongList, str(item['uri']))
           addPlaylist(topListName, str(item['name']))

    displayDict(playListMap)
    print retRandomPlaylist(playListMap[sessKeyWord])
    #displayPlaylist(topSongList)
    resp = requests.post(render_url, data=json.dumps(playListMap))
    print resp

  else:
     print "Can't get token for", username



from flask import Flask
from flask import request
import requests

app = Flask(__name__)
#yo_api_token = "ba978dc5-80df-f22b-d8f2-dee502b12e6f"
yo_api_token = "2b78350c-eda8-4e09-9a12-f856915564f6"
test_url = "http://5.152.179.176:9024/" # Render URL

def yo_link_to_usr(api_token, usrname, playlist_link):
        return requests.post("http://api.justyo.co/yo/", data={'api_token': api_token,'username':usrname, 'link':playlist_link })

@app.route("/")
def entry_func():
    return "YoApp Default page"

@app.route("/fm_svc")
def callback():
    lastfm_token = request.args.get('token')
    print lastfm_token
    code = "Last FM App"
    return code

@app.route("/yo_svc")
def sp_callback():
    usr_name = request.args.get('username')
    global test_url
    url = test_url+"?username="+usr_name 
    print url
    yo_link_to_usr(yo_api_token, request.args.get('username'), url) 
    return "success" 

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=9500)


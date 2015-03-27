import os
import subprocess
import myOauth
import spotipy
import requests
import json, urllib2
#For webdriver
from selenium import webdriver
import time

def prompt_for_user_token(username, scope=None, client_id = None,
client_secret = None, redirect_uri = None):
    #client_id = "5c9bcec9ab554e779c94360665b03ad8"
    #client_secret = "8f2e9afb1abf444e92ef2834c9ff67da"
    client_id = "886ea3549d38496280ae16d5b1278489"
    client_secret = "ce5fff9067214f108db30b338bba3f31"
    redirect_uri = "http://5.152.179.176:9009/"
    sp_oauth = myOauth.SpotifyOAuth(client_id, client_secret, redirect_uri,
                                    scope=scope, cache_path=".cache-" + username)
# try to get a valid token for this user, from the cache,
# if not in the cache, the create a new (this will send
# the user to a web page where they can authorize this app)
#token_info = sp_oauth.get_cached_token()

    token_info = "empty"
    if token_info:
        auth_url = sp_oauth.get_authorize_url()
        print "Please navigate here: %s" % auth_url
        auto_login(auth_url) 
        r = requests.get('http://localhost:9009/getcode')
        print r.content
        token_info = sp_oauth.get_access_token(r.content)
        #token_info = r.content


    # Auth'ed API request

    if token_info:
        return token_info ['access_token']
    else:
        return None


def auto_login(url):
    driver = webdriver.PhantomJS()
    driver.get(url) 
    driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/a").click()
    driver.find_element_by_xpath('//*[@id="login-username"]').send_keys("spotifyondemand")
    driver.find_element_by_xpath('//*[@id="login-password"]').send_keys("test123")
    source = driver.page_source
    driver.find_element_by_xpath("/html/body/div/div[2]/form/div[3]/div[2]/button").click()
    #compare source add code later
    time.sleep(20)
    driver.close()


# yo hip service

# Run
   For a successful run, launch render.py, myFlask.py, yo_callback.py in the background. Run <python myspotify.py 1210795004> to populate the playlist database. Now yo to the YOLATESTSONGS channel and see the Magic happen.

# Codebase
1. The codebase consists of mainly two parts: Spotify OAuth code and Yo render page.

2. Spotify OAuth consists of a callback server for spotify (myFlask.py) running on a designated port.
   This flask server will persist the token and return token to the caller as and when called. 

3. myspotify.py does the user authentication(not automated yet) and fetches TOP Song playlist
  from the users public playlist. This is POSTed to render server which persists the list.

4. Render server renders playlist links for the channel. Its picks a playlist uri from the persisted
  database and returns to the user. Thus returned link will get opened in Spotify App.

# Note
// For now the whole Spotify OAuth codebase cannot be used automatically on the machine as it needs to be automated.
// As of now the render will read the conf.txt which was formed through run from my local machine.
// backup.txt is the backup file with the list  of playlist uri

# ToDo
  The sp oauth needs to automate the oauth process and keep populating render server with updated playlists.

# Contact Us:
    S V SHENOY(svshenoy@gmail.com),  LinkedIn Profile: www.linkedin.com/pub/shashidhar-shenoy/38/3b1/556
    PAWAN (pawanhn@gmail.com),  LinkedIn Profile: www.linkedin.com/in/pawanrao/   

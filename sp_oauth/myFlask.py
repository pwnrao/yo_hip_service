from flask import Flask
from flask import request
app = Flask(__name__)

myCode = "empty"
@app.route("/")
def callback():
    global myCode
    myCode = request.args.get('code')
    code = "Access Successful"
    return code

@app.route("/getcode")
def getcode():
    global myCode
    print "getcode call"
    print myCode
    return myCode

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=9009)


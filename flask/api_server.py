from flask import Flask,jasonify,Blueprint,request
import random
app = (__name__)
@app.route('/age/',methods = ['GET'])

def greet():
    username = request.args.get('name',defult = None,type = str)

    response = {}

    if username:
        response['age'] = random.randint(1,100)
    else :
        response['age'] = -1
    return jasonify(response)
def index():
    return ("<h1>All Is Well</h1>")

@app.route('/')

if __name__ == "__main__":
    app.run(debug=True)

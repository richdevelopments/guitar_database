import os
from flask import Flask

app = Flask(__name__)

# test function with a route in it display some text as a proof of consetp
@app.route('/')
def hello():
    return 'Hello World...again'

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
from simplewebtools import app
# app.run(host='127.0.0.1', port=5000, debug=True)

if __name__ == '__main__':
    app.run()



"""
from flask import Flask
from flask import g
from flask import render_template
from flask import request
from flask import Response

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'top'

@app.route('/hello')
@app.route('/hello/<username>')
def hello_world2(username=None):
    return render_template('hello.html', username=username)

@app.route('/post', methods=['POST', 'PUT', 'DELETE'])
def show_post():
    return str(request.values)

def main():
    app.debug = True
    app.run()

if __name__ == '__main__':
    main()


"""
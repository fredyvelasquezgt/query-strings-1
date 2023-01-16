from flask import Flask, render_template, request

app = Flask(__name__)

#la entrada de index tambien esta dentro de la misma funcion de hello_world
@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


#nueva route usando query strings
@app.route('/new/')
def query_strings(greeting='hello'):
    query_val = request.args.get('greeting', greeting)
    return '<h1> the greeting is: {0} </h1>'.format(query_val)



if __name__ == '__main__':
    app.run()


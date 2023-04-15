from flask import Flask 

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

    
@app.route('/dojo')
def success():
    return "dojo"
    

@app.route('/say/<name>')
def say(name):
    return f"Hi {name.capitalize()}!"

@app.route('/repeat/<int:num>/<string:word>')
def repeat_word(num, word):
    output = ''

    for i in range(0,num):
        output += f"<p>{word}</p>"

    return output

# @app.route('/repeat/<int:num>/<string:word>')
# def repeat_word(num, word):
#     return f"{word * num}"


if __name__=="__main__":
    app.run(debug=True)
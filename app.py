from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello world</h1>"

@app.route('/user/<name>')
def user(name):
    print(request.headers)
    return '<h1>Hello {}!</h1>'.format(name)

@app.route('/agent')
def user_agent():
    #print(request.headers)
    useragent = request.headers['User-Agent']
    print(useragent)
    return '<h3>Ваш юзерагент: {}</h3>'.format(useragent)

if __name__ == "__main__":
    app.run(debug=True)
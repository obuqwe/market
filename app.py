from flask import Flask, request, redirect, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return redirect('https://google.ru')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.route('/agent')
def user_agent():
    #print(request.headers)
    useragent = request.headers['User-Agent']
    print(useragent)
    return '<h3>Ваш юзерагент: {}</h3>'.format(useragent)

@app.route('/home')
def home_link():
    info = {
        'title': 'Welcome',
        'description': 'Добро пожаловать',
        'news': [
            {'title': 'Breaking news'},
            {'title': 'Hot news'},
            {'title': 'New news!'},
        ]
    }
    return render_template('home.html', info=info)

@app.route('/404')
def not_found():
    return '<h1>Bad request</h1>', 404

#@app.route('/')
#def redirect_to_google():
#    return redirect('https://google.ru')

if __name__ == "__main__":
    app.run(debug=True)
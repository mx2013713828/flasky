from flask import Flask
from flask import render_template
from flask.ext.bootstrap import Bootstrap
app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def hello_world():
    return render_template('index.html')
@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name,mydic={'key':'nihao wo shi ni baba'},comments=['zhao','qian''sun','sun','li'])
@app.route('/boots')
def boots():
    return render_template('boots.html')
@app.route('/base')
def base():
    return render_template('base.html')
if __name__ == '__main__':
    app.run(debug=True)

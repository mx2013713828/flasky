# -*- encoding:utf-8 -*-
from flask import Flask
from flask import render_template
from flask.ext.bootstrap import Bootstrap
from flask import request
from flask import url_for,redirect,session,flash
from flask_wtf import FlaskForm
# from flask.ext.wtf import Form
from wtforms.validators import DataRequired
from wtforms import StringField,SubmitField


from flask import current_app,g
#返回静态视图的时候需要设置static_path为空 或者 将url设为/static/
CSRF_ENABLD = True

app = Flask(__name__,static_path='')
app.config['SECRET_KEY']='123456'
bootstrap = Bootstrap(app)

#class 4 form


@app.route('/',methods=['GET','POST'])
def hello_world():
    #name = None #name值为空
    form = NameForm() #创建一个NameForm实例用于表单
    if form.validate_on_submit(): #form.validate_on_submit(#调用name上的Required();)验证输入表单中的数据是否被验证函数接受
        #name = form.name.data  #把用户输入的名字通过name的data属性传递给局部变量name，再把form_name设为空字符串，等待下次输入
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data #用户会话
        return redirect(url_for('hello_world'))#重定向此页面，刷新后可以不用弹出重新输入表单提示,session中存储用户输入的name值
        #form.name.data = ''

    user_agent = request.headers.get('User-Agent')
    return render_template('index.html',usr=user_agent,form=form,name=session.get('name')) #第一个form是index里渲染表单的语句中form变量，第二个是实例化的NmeForm
@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name,mydic={'key':'nihao wo shi ni baba'},comments=['zhao','qian''sun','sun','li'])
@app.route('/boots')
def boots():
    user_agent = request.headers.get('User-Agent')


    return render_template('boots.html',name=url_for('boots',_external=True))
@app.route('/base')
def base():

    return render_template('base.html')
@app.route('/hello')

#静态视图，app.send_static_file()
def hello():
    return app.send_static_file('/static/hello.html')

class NameForm(FlaskForm):
    name = StringField('what is your name?',validators=[DataRequired()])
    submit = SubmitField('Submit')

if __name__ == '__main__':
    app.run(debug=True)

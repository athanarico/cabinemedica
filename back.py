from flask import Flask, render_template, flash, redirect, request, session, g

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'

users = []
users.append(User(id=1, username='joao', password='123'))

app = Flask(__name__)
app.secret_key = 'senha_secreta'

@app.before_request
def before_request():
    g.user = None

    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user
        

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user_id', None)

        username = request.form['username']
        password = request.form['password']
        
        user = None
        for x in users: 
            if x.username == username:
                user = x

        if user and user.password == password:
            session['user_id'] = user.id
            return redirect('/cabine')

        return redirect('/')

    return render_template('login.html')

@app.route('/cabine')
def cabine():
    return render_template('cabine.html')

if __name__ == '__main__':
    app.run(host='127.0.0.9',port=4455,debug=True) 
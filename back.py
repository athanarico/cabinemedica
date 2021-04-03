############################################################################################################################
############################################ WEB SERVER DA CABINE MÉDICA ###################################################
############################################################################################################################

from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy  import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

# Configurações do Flask e linkagem do banco de dados
app = Flask(__name__)
app.config['SECRET_KEY'] = 'segredosecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/authari/Documents/cabine_medica/database.db'
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    """
    Classe que gerenciará a tabela User do banco de dados database.db
    
    Atributos
    ---------
    id : int
        id do usuário
    username: str
        nome do usuário
    email: str
        email do usuário
    password: string
        senha do usuário
        
    """

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))

@login_manager.user_loader
def load_user(user_id):
    """O método load_user será chamado a cada requisição, instanciando o objeto User de acordo com o id 
    do usuário em sessão"""

    return User.query.get(int(user_id))

class LoginForm(FlaskForm):
    """Classe que cria e gerencia o form de login"""

    username = StringField('nome de usuário', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('senha', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('lembrar-se')

class RegisterForm(FlaskForm):
    """Classe que cria e gerencia o form de registro"""

    email = StringField('email', validators=[InputRequired(), Email(message='Email inválido'), Length(max=50)])
    username = StringField('nome de usuário', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('senha', validators=[InputRequired(), Length(min=8, max=80)])

@app.route('/')
def index():
    return render_template('index.html')


#######################################################################
########################## PÁGINA DE LOGIN ############################
#######################################################################

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    # Valida usuário por meio de consulta 'query' na tabela User.
    if form.validate_on_submit():
        # Consulta a tabela, filtrando o username inserido.
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            # Criptografamos o input password e checamos se coincide com o hash armazenado no banco de dados.
            if check_password_hash(user.password, form.password.data):
                # Se o usuário existe, inicia a sessão e redireciona ao Dashboard
                login_user(user, remember=form.remember.data)
                return redirect(url_for('dashboard'))

        #Senão, volta para a página de login
        return redirect(url_for('login'))
        #return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'

    return render_template('login.html', form=form)

####################################################################
######################## PÁGINA DE REGISTRO ########################
####################################################################

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()

    # Se todos os campos de registro forem preenchidos corretamente, criamos o usuário.
    if form.validate_on_submit():
        # Criptografa o password, transformando-o em um hash
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        # Insere o novo usuário na tabela User
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('/'))
        #return '<h1>' + form.username.data + ' ' + form.email.data + ' ' + form.password.data + '</h1>'

    return render_template('signup.html', form=form)

#####################################################################
######################## PÁGINA DO DASHBOARD ########################
#####################################################################

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.username)

#######################################################################
######################### PÁGINA DE RELATÓRIOS ########################
#######################################################################

@app.route('/relatorios')
@login_required
def relatorios():
    return render_template('relatorios.html', name=current_user.username)

#######################################################################
################################ LOGOUT ###############################
#######################################################################

@app.route('/logout')
@login_required
def logout():
    # Encerra a sessão, voltando para a página inicial.
    logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, redirect

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap5

class MyForm(FlaskForm):
    email = StringField('EMAIL', validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Log In")

app = Flask(__name__)
app.config['SECRET_KEY'] = 'copy me :)'
bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = MyForm()
    if form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return redirect('/success')
        else:
            return redirect("/denied")
    return render_template('login.html', form=form)

@app.route("/success")
def success():
    return render_template("success.html")

@app.route("/denied")
def denied():
    return render_template("denied.html")

if __name__ == '__main__':
    app.run(debug=True)

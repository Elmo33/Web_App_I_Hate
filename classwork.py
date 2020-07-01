from flask import Flask, render_template, redirect, url_for, request, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'group 1.2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(30), nullable=False)

    def __str__(self):
        return f'Username: {self.username}, Password: {self.password}'


# db.create_all()
# b1 = Books.query.first()
# print(b1)
# all_books = Books.query.all()
# for each in all_books:
#     print(each)
# b1 = Books(title='სიბრძნე სიცრუისა', author='სულხან-საბა ორბელიანი', price=15)
# db.session.add(b1)
# db.session.commit()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        session['email'] = email
        return redirect(url_for('user'))

    else:
        if 'email' in request.args and 'password' in request.args:
            print(request.args["password"])
            email = request.args['email']
            return f'{email}'
        return render_template('login.html')


# @app.route('/user')
# def user():
#     if 'username' in session:
#         return f"Hello {session['username']}"
#     else:
#         return redirect(url_for('login'))

#
# @app.route('/logout')
# def logout():
#     session.pop('username', None)
#     return 'you are logged out'


# @app.route('/books', methods=['GET', 'POST'])
# def books():
#     if request.method == 'POST':
#         t = request.form['title']
#         a = request.form['author']
#         p = float(request.form['price'])
#         b1 = Books(title=t, author=a, price=p)
#         db.session.add(b1)
#         db.session.commit()
#         return 'წიგნი დამატებულია'
#
#     return render_template('books.html')


if __name__ == '__main__':
    app.run(debug=True)

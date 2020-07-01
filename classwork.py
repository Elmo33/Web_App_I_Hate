from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import time

# მარტივი ვებსაიტი, შედგება 5 გვერდისგან
# პირველ გვერდზე განთავსებულია სურათი, რომელიც ხსნის ვებსაიტის შინაარს
# ლოგინ გვერდის მთავარი დანიშნულებაა შეყვანილი იმეილის და პაროლის წამოღება და მონაცემთა ბაზაში შენახვა
# დამატების დაკლიკების შემდეგ გადმოვყავვართ მთავარ გვერდზე შეტყობინებით რომ მონაცემები წარმატებით დაემატა
# Cool stuff გვერდზე განთავსებულია ღილაკი რომელზე დაჭერის შემდეგ ჩაიტვირთება loading icon
# Users- გვერდზე გამოქვეყნებულია ყველა ის მონაცემი, რომელიც შეყვანილი მომხარებლის მონაცემთა ბაზაში
# ბოლოს კი Html-ში ჯავასკრიპტით აწყობილი კავკულატორი, რომელიც რა თქმა უნდა მე არ ამიწყვია

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vitomkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(30), nullable=False)

    def __str__(self):
        return f'Email: {self.email}, Password: {self.password}'


db.create_all()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        print(email)
        print(password)
        b1 = User(email=email, password=password)
        db.session.add(b1)
        db.session.commit()
        return render_template("index.html", text="Successfully added your info to our list")

    else:
        return render_template('login.html')


@app.route("/cool_stuff", methods=["GET", "POST"])
def cool_stuff():
    if request.method == "POST":
        return render_template("cool_stuff.html", waiting=True, function=time)
    return render_template("cool_stuff.html")


@app.route("/calculator")
def calculator():
    return render_template("calculator.html")


@app.route("/users", methods=["GET"])
def users():
    return render_template("users.html", user_list=User.query.all())


if __name__ == '__main__':
    app.run(debug=True)

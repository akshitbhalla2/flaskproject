from flask import Flask, render_template, url_for
from .forms import RegistrationForm, LoginForm

app = Flask(__name__)

# import secrets
# secret_key = secrets.token_hex(16)

app.config["SECRET_KEY"] = 'd8eed0b0a295ca457ea8def492983b00'

posts = [
    {
        "author": "Akshit Bhalla",
        "title": "Blog Post 1",
        "content": "First Post Content",
        "date": "April 20, 2020",
    },
    {
        "author": "Akshit Bhalla",
        "title": "Blog Post 2",
        "content": "Second Post Content",
        "date": "March 30, 2020",
    },
]

@app.route("/")
@app.route("/home")
def hello():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/blog")
def blog():
    return render_template("blog.html", posts=posts, title="Blog Page")

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template("register.html", title="register", form=form)
#
# @app.route("/login")
# def login():
#     form = LoginForm()
#     return render_template("login.html", title="login", form=form)

if __name__ == "__main__":
    app.run(debug=True) # Debug=True makes possible checking changes without restarting server
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ---------- MODEL ----------
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)

# ---------- ROUTES ----------

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        new_user = User(name=name, email=email)
        db.session.add(new_user)
        db.session.commit()
        return redirect("/")

    users = User.query.all()
    return render_template("index.html", users=users)


@app.route("/delete/<int:id>")
def delete(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return redirect("/")


# 🔴 👉 PUT THE EDIT CODE EXACTLY HERE 👇
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    user = User.query.get_or_404(id)

    if request.method == "POST":
        user.name = request.form["name"]
        user.email = request.form["email"]
        db.session.commit()
        return redirect("/")

    return render_template("edit.html", user=user)
# 🔴 👉 END HERE


# ---------- RUN APP ----------
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

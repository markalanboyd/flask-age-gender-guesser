from flask import Flask, render_template

from nationalagenderfy import Guesser

app = Flask(__name__)


@app.route("/<name>")
def guess(name):
    guesser = Guesser()
    age = guesser.age(name)
    gender = guesser.gender(name)
    nationality = guesser.nationality(name)
    return render_template(
        "guess.html", name=name.title(), age=age, gender=gender, nationality=nationality
    )


if __name__ == "__main__":
    app.run(debug=True)

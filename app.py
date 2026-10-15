
from flask import Flask, render_template

app = Flask(__name__)

movies = [
    {
        "id": 1,
        "title": "Avengers: Endgame",
        "genre": "Action, Sci-Fi",
        "rating": 8.4,
        "description": "Earth's heroes unite for their final battle."
    },
    {
        "id": 2,
        "title": "Interstellar",
        "genre": "Sci-Fi, Drama",
        "rating": 8.7,
        "description": "A team travels through space to save humanity."
    },
    {
        "id": 3,
        "title": "3 Idiots",
        "genre": "Comedy, Drama",
        "rating": 8.4,
        "description": "Three friends discover the true meaning of success."
    }
]

@app.route("/")
def home():
    return render_template("index.html", movies=movies)

if __name__ == "__main__":
    app.run(debug=True)

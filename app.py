

from flask import Flask, render_template

app = Flask(__name__)

movies = [
    {
        "id": 1,
        "title": "Avengers: Endgame",
        "genre": "Action, Sci-Fi",
        "rating": 8.4,
        "description": "Earth's heroes unite for their final battle.",
        "poster": "https://image.tmdb.org/t/p/w500/or06FN3Dka5tukK1e9sl16pB3iy.jpg"
    },
    {
        "id": 2,
        "title": "Interstellar",
        "genre": "Sci-Fi, Drama",
        "rating": 8.7,
        "description": "A team travels through space to save humanity.",
        "poster": "https://image.tmdb.org/t/p/w500/gEU2QniE6E77NI6lCU6MxlNBvIx.jpg"
    },
    {
        "id": 3,
        "title": "3 Idiots",
        "genre": "Comedy, Drama",
        "rating": 8.4,
        "description": "Three friends discover the true meaning of success.",
        "poster": "https://image.tmdb.org/t/p/w500/66A9MqXOyVFCssoloscw79z8Tew.jpg"
    }
]

@app.route("/")
def home():
    return render_template("index.html", movies=movies)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)

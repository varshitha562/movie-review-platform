
from flask import Flask, render_template,request


app = Flask(__name__)

movies = [
    {
        "id": 1,
        "title": "Avengers: Endgame",
        "genre": "Action, Sci-Fi",
        "rating": 8.4,
        "description": "Earth's heroes unite for their final battle.",
        "poster": "https://image.tmdb.org/t/p/w500/or06FN3Dka5tukK1e9sl16pB3iy.jpg",
        "year": 2019,
        "director": "Anthony and Joe Russo",
        "cast": "Robert Downey Jr., Chris Evans, Scarlett Johansson",
        "story": "The Avengers attempt to reverse the destruction caused by Thanos and save the universe."
    },
    {
        "id": 2,
        "title": "Interstellar",
        "genre": "Sci-Fi, Drama",
        "rating": 8.7,
        "description": "A team travels through space to save humanity.",
        "poster": "https://image.tmdb.org/t/p/w500/gEU2QniE6E77NI6lCU6MxlNBvIx.jpg",
        "year": 2014,
        "director": "Christopher Nolan",
        "cast": "Matthew McConaughey, Anne Hathaway, Jessica Chastain",
        "story": "A team of astronauts travels through a wormhole to find a new home for humanity."
    },
    {
        "id": 3,
        "title": "3 Idiots",
        "genre": "Comedy, Drama",
        "rating": 8.4,
        "description": "Three friends discover the true meaning of success.",
        "poster": "https://image.tmdb.org/t/p/w500/66A9MqXOyVFCssoloscw79z8Tew.jpg",
        "year": 2009,
        "director": "Rajkumar Hirani",
        "cast": "Aamir Khan, R. Madhavan, Sharman Joshi",
        "story": "Three engineering friends challenge traditional education and learn to follow their passion."
    }
]

@app.route("/")
def home():
    return render_template("index.html", movies=movies)

@app.route("/movie/<int:movie_id>")
def movie_details(movie_id):
    movie = next((m for m in movies if m["id"] == movie_id), None)

    if movie is None:
        return "Movie not found", 404

    return render_template("movie_details.html", movie=movie)


reviews = []

@app.route("/review", methods=["GET", "POST"])
def write_review():
    if request.method == "POST":
        reviews.append({
            "name": request.form["name"],
            "movie_id": int(request.form["movie_id"]),
            "rating": int(request.form["rating"]),
            "comment": request.form["comment"]
        })
        return "Review submitted successfully! <a href='/'>Back to Home</a>"

    return render_template("review.html", movies=movies)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

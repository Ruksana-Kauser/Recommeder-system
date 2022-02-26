from flask import Flask, render_template, redirect, request
from anime import recommender, genre_recommender, rating_recommender, checker, list_genre, list_name, list_rating

app = Flask(__name__) #initialization


@app.route('/')
def home():
    return render_template("index.html")


@app.route("/anime",methods=['GET','POST'])
def anime():
    if request.method=='POST':
        a = request.form["input"]
        
        if len(checker(a)) > 4:    
            b = recommender(a)
            genre = genre_recommender(a,11)
            rating = rating_recommender(a,11)
            return render_template("anime.html",ll = b, gg = genre, r = rating)
        else:
            ll = checker(a)
            return render_template("anime.html",ll = ll)
    ll = []
    return render_template("anime.html",ll = ll)

@app.route('/list')
def list():
    name = list_name()
    genre = list_genre()
    rate = list_rating()
    return render_template("list.html", name=name, genre=genre, rate=rate)


if __name__ == "__main__":
    app.run(debug=True)


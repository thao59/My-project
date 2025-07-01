from flask import Flask, render_template, redirect, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from functions import search

#configure application
app = Flask(__name__)


@app.after_request
def after_request(response):
    response.headers["Cache-control"] = 'no-cache, no-store, must-revalidate'
    response.headers["Expire"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():
     #ensure valid input
     anime_title = request.args.get("anime_name")

     if not anime_title:
        return render_template ("index.html")

     #redirect to search page, passing the anime title to query parameter q
     return redirect(url_for("look", q=anime_title))

#create a dict to store searched result 
search_anime = {}

@app.route("/search")
def look():
     
     #retrieve anime's name 
     anime_title = request.args.get("q")
     print(f"anime name input: {anime_title}")

     #check if anime's title has been searched before
     if anime_title in search_anime:
        print("anime has been searched before")
        info = search_anime[anime_title]
        return render_template("search.html", info=info, page="result")
     else:
         #search anime's info
         print("anime hasn't been searched before")
         search_info = search(anime_title)

         #if no anime found
         if not search_info:
             return render_template("not_found.html", message="Not found")
         else:
             #store result in dict 
             search_anime[anime_title] = search_info 
             return render_template("search.html", info = search_info, page="result")


@app.route("/anime")
def anime():

    #retrieve anime id
    anime_id= request.args.get("id")
    print(f"anime id: {anime_id}")

    anime_title = request.args.get("title")
    print(f"anime title: {anime_title}")


    #search id stored in dict 
    for value in search_anime.values():
        #access each row of value 
        for row in value:
            #loop through each dict to find matching id
            if row["_id"] == anime_id:
                print(f"id stored in server: {row["_id"]}, id retrieved from user's input: {anime_id}")
                #pass the dict to a variable 
                anime = row
                print(f"new anime dict: {anime}, row dict: {row}")
                for key,value in anime.items():
                    if not value:
                        anime[key] = "N/A"
                print(f"anime on page: {anime}")
                return render_template("anime-info.html", anime=anime, page="result")
    
    return render_template("not_found.html", message="Not found")









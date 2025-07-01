import requests


def search(anime_name):
    #ensure input has no space 
    anime_title = anime_name.lower()

    #search anime name
    url = "https://anime-db.p.rapidapi.com/anime"

    querystring = {"page": "1", "size": "10", "search": anime_title, "sortBy": "ranking"}
    headers = {
	    "x-rapidapi-key": "81f980fa29mshe241433e844a716p1707aejsn4bd9c757408e",
	    "x-rapidapi-host": "anime-db.p.rapidapi.com"
        }

    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status() #raise an error if page fails to load 
        search_anime = response.json()
        return search_anime["data"]
    
    except Exception as e:
        print(f"Error occur: {e}")
        return None


    




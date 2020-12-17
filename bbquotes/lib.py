import requests


def quotes():

    url = "https://breaking-bad-quotes.herokuapp.com/v1/quotes"
    r = requests.get(url).json()[0]

    quotes = r["quote"]
    author = r["author"]

    return f"QUOTE:{quotes} ({author})"

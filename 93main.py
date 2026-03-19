import requests

api_key = "YOUR_API_KEY"

query = input("What type of news are you interested in? ")

url = f"https://newsapi.org/v2/everything?q={query}&sortBy=publishedAt&apiKey={api_key}"

response = requests.get(url)
data = response.json()

if "articles" in data:
    for news in data["articles"]:
        print(news["title"])
else:
    print("Error:", data)
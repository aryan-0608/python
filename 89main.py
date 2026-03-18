# import requests
# response = requests.get("https://www.google.com")
# print(response.text)

# import requests

# url = "https://jsonplaceholder.typicode.com/posts"

# data = {
#     "title": "foo",
#     "body": "bar",
#     "userId": 1
# }

# headers = {
#     "Content-Type": "application/json; charset=UTF-8"
# }

# try:
#     response = requests.post(url, json=data, headers=headers)

#     print("Status Code:", response.status_code)
#     print("Response:", response.json())   # better than text

# except requests.exceptions.RequestException as e:
#     print("Error:", e)

import requests
from bs4 import BeautifulSoup

url = "https://example.com"
r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())
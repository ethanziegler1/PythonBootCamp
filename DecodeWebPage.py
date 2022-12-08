import requests
from bs4 import BeautifulSoup

baseURL = 'http://www.nytimes.com'
r = requests.get(baseURL)
soup = BeautifulSoup(r.text, features="html.parser")

for story_heading in soup.find_all(class_="story-heading"):
    if story_heading.a:
        print(story_heading.a.text.replace("\n", " ").strip())
    else:
        print(story_heading.contents[0].strip())
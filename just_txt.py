import requests
from bs4 import BeautifulSoup

def only_txt(url):
    req = requests.get(url)
    content = req.content
    soup = BeautifulSoup(content,'html.parser')

    for script in soup(["script", "style"]):
        script.decompose()
        
    strips = list(soup.stripped_strings)
    text = "".join(strips)

    return text
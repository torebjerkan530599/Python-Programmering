# read the title of a webpage
import urllib.request
from urllib.error import HTTPError

try:
    content = urllib.request.urlopen("https://en.wikipedia.org/wiki/Special:Random")
   
    text = content.read().decode()
    current = text.find("<title>") + len("<title>")
    end = text.find("</title>") - len(" - Wikipedia")
    print("URL: " + content.geturl())
    print()
    print("Title: " + text[current:end])
    
    
except HTTPError as ex:
    print(f'Something went wrong when trying to read from {ex.url}')
    
    

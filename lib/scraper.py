
from bs4 import BeautifulSoup
import requests

headers = {'user-agent': 'my-app/0.0.1'}
html = requests.get("https://flatironschool.com/", headers=headers)
doc = BeautifulSoup(html.text, 'html.parser')
# Check if the request was successful
if html.status_code == 200:
    # Create a Beautiful Soup object to parse the HTML
    doc = BeautifulSoup(html.text, 'html.parser')
    
    # Print the parsed HTML document
    print(doc.prettify())
else:
    print(f"Failed to retrieve the page. Status code: {html.status_code}")
from bs4 import BeautifulSoup
import requests
import nltk
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
nltk.download('punkt')



def seo_analysis(url):
    not_found = []
    found = []
    response = requests.get(url)
    if response.status_code != 200:
        print("Error: Unable to access the website " )
        return
    soup = BeautifulSoup(response.content, 'html.parser')
    # Extarcting the title and description
    title = soup.find('title').get_text()
    description = soup.find('meta', attrs={'name': 'description'}).get('content')
    # check if the title and title exits
    if title:
        found.append("Title Exists!")
    else:
        not_found.append("Title  Does Not Exists!")
    if description:
        found.append("Description Exists!")
    else:
        not_found.append("Description Does Not Exists!")
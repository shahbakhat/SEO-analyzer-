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
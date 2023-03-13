from bs4 import BeautifulSoup
import requests
import nltk
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
nltk.download('punkt')
url = 'https://codeinstitute.net/ie/'
soup = BeautifulSoup(requests.get(url).text, 'html.parser')
# print(soup.prettify())

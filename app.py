
from flask import Flask, render_template,url_for
from bs4 import BeautifulSoup
import requests

app = Flask(__name__, static_folder='C:\\Users\\arrib\\OneDrive\\Escritorio\\WEBREGLADO\\templates')


# FunciÃ³n para hacer web scraping
def scrape_website():
    url = 'https://quotes.toscrape.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = []
    for quote in soup.find_all('div', class_='quote'):
        text = quote.find('span', class_='text').text
        author = quote.find('small', class_='author').text
        quotes.append({'text': text, 'author': author})
    return quotes

@app.route('/')
def home():
    # Llamamos a la funciÃ³n de scraping
    quotes = scrape_website()
    return render_template('index.html', quotes=quotes)

if __name__ == '__main__':
    app.run(debug=True)
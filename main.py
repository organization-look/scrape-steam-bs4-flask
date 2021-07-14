import requests
import bs4
from flask import Flask,render_template

app = Flask(__name__, template_folder='template')


@app.route('/')
def hello():



    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'

    }
    url = 'https://store.steampowered.com/search/?filter=topsellers'
    r = requests.get(url, header)
    soup = bs4.BeautifulSoup(r.text, "html.parser")
    top_seller = soup.findAll('a', attrs={'data-gpnav':'item'})

    return render_template('index.html', top_seller=top_seller)

if __name__ == '__main__':
    app.run(debug=True)





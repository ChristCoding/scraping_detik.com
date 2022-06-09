import requests
from bs4 import BeautifulSoup
from flask import Flask , render_template

app = Flask ( __name__ )


@app.route ( '/' )
def home() :
    return render_template ( 'index.html' )


@app.route ( '/scraping_detik' )
def detik_populer() :
    html_req = 'https://www.detik.com/terpopuler'
    headers = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    try :
        res = requests.get ( html_req , headers )
    except :
        return None
    if res.status_code == 200 :
        soup = BeautifulSoup ( res.text , 'html.parser' )
        populer_area = soup.find ( attrs={ 'class' : 'grid-row list-content' } )
        titles = populer_area.findAll ( attrs={ 'class' : 'media__title' } )
        images = populer_area.findAll ( attrs={ 'class' : 'media__image' } )
        return render_template ( 'scraping_detik.html' , images=images )
    else :
        return None


@app.route ( '/idr_rates' )
def idr_rates() :
    try :
        source = requests.get ( 'http://www.floatrates.com/daily/idr.json' )
    except :
        return None
    if source.status_code == 200 :
        json_data = source.json ( )
        return render_template ( 'idr_rates.html' , datas=json_data.values ( ) )
    else :
        return None


if __name__ == '__main__' :
    app.run ( debug=True )

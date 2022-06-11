import requests
from bs4 import BeautifulSoup
from flask import Flask , render_template
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


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


@app.route ( '/carousell' )
def carousell() :
    driver = webdriver.Chrome ( )
    driver.get ( 'https://id.carousell.com/categories/photography-6/?searchId=5o7Gsh' )

    for n in range ( 1 , 50 ) :
        ActionChains ( driver ).scroll_by_amount ( 0 , 100 ).perform ( )
    for n in range ( 1 , 50 ) :
        ActionChains ( driver ).scroll_by_amount ( 0 , -100 ).perform ( )
    images = driver.find_elements ( By.CSS_SELECTOR , 'main img' )
    links = driver.find_elements ( By.CSS_SELECTOR , 'main a' )
    datas = [ ]
    title = None
    source = None
    titlelink = None
    for image , link in zip ( images , links ) :
        try :
            if image.get_attribute ( 'title' ) != '' :
                title = (image.get_attribute ( 'title' ))
                source = (image.get_attribute ( 'src' ))
            if link.get_attribute ( 'href' ).find ( 'https://id.carousell.com/p/' ) >= 0 :
                titlelink = (link.get_attribute ( 'href' ))
            data = {
                'title' : title,
                'titlelink' : titlelink,
                'source' : source,
            }
            datas.append ( data )
        except :
            break
    driver.quit ( )
    datas.pop ( 0 )
    driver.quit ( )
    datas.pop ( 0 )
    newdatas = [ ]
    for data in datas :
        newdatas.append ( data )
        if len ( newdatas ) > 2 :
            if newdatas [ len ( newdatas ) - 2 ] == newdatas [ len ( newdatas ) - 1 ] :
                newdatas.pop ( len ( newdatas ) - 1 )
    newdatas.pop ( 0 )
    return render_template ( 'carousell.html' , datas=newdatas )



if __name__ == '__main__' :
    app.run ( debug=True )

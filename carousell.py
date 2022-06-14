from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def carousell() :
    driver = webdriver.Chrome ( )
    driver.get ( 'https://id.carousell.com/categories/photography-6/?searchId=5o7Gsh' )

    for n in range ( 1 , 50 ) :
        ActionChains ( driver ).scroll_by_amount ( 0 , 100 ).perform ( )
    for n in range ( 1 , 50 ) :
        ActionChains ( driver ).scroll_by_amount ( 0 , -100 ).perform ( )
    images = driver.find_elements ( By.CSS_SELECTOR , 'main img' )
    links = driver.find_elements ( By.CSS_SELECTOR , 'main a' )
    prices= driver.find_element(By.TAG_NAME,'main').find_elements(By.TAG_NAME,'p')
    datas = [ ]
    data_price=[]
    title = None
    source = None
    titlelink = None

    for price in prices :
        if price.get_attribute ( 'title' ).find ( 'Rp' ) >= 0 :
            data_price.append(price.get_attribute ( 'title' ) )

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
                'price': 0,
            }
            datas.append ( data )
        except :
            break
    driver.quit ( )
    datas.pop ( 0 )
    newdatas = [ ]
    for data in datas :
        newdatas.append ( data )
        if len ( newdatas ) > 2 :
            if newdatas [ len ( newdatas ) - 2 ] == newdatas [ len ( newdatas ) - 1 ] :
                newdatas.pop ( len ( newdatas ) - 1 )
    newdatas.pop ( 0 )
    n=0
    for newdata in newdatas:
        newdata['price']=data_price[n]
        n+=1
    return newdatas
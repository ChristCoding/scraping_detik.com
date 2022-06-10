from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_driver_path = 'C:\PythonProj\chromedriver.exe'
driver = webdriver.Chrome ( )
driver.get ( 'https://id.carousell.com/categories/photography-6/?searchId=5o7Gsh' )


try:
    cards = driver.find_element ( By.XPATH , '//*[@id="root"]/div/div[3]/div/div[4]/main/div/div' )
    fold=4
except:
    cards = driver.find_element ( By.XPATH , '//*[@id="root"]/div/div[3]/div/div[5]/main/div/div' )
    fold=5


for n in range(1, 40):
    try:
        card_link=driver.find_element(By.XPATH,f'//*[@id="root"]/div/div[3]/div/div[{fold}]/main/div/div/div[{n}]/div/div[1]/a[2]').get_attribute('href')
        card_title=driver.find_element(By.XPATH,f'//*[@id="root"]/div/div[3]/div/div[{fold}]/main/div/div/div[{n}]/div/div[1]/a[2]/div[1]/div/div/img').get_attribute('title')
        card_img=driver.find_element(By.XPATH,f'//*[@id="root"]/div/div[3]/div/div[{fold}]/main/div/div/div[{n}]/div/div[1]/a[2]/div[1]/div/div/img').get_attribute('src')
        print(n,card_title,card_link,card_img)
    except:
        print(n)
        continue

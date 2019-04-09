from selenium import webdriver # 웹사이트 들어가기 위한 라이브러리
from bs4 import BeautifulSoup

ctx = '../crawler/chromedriver'
driver = webdriver.Chrome(ctx)
driver.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn') # 해당주소를 get 메소드를 통해보여준다
soup = BeautifulSoup(driver.page_source, 'html.parser')

all_tb = soup.find_all('tbody')

for i in all_tb:
    print("결과  :")
    print(i.text.split())
driver.close()




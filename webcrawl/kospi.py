from urllib.request import urlopen # url를 가져오는 라이브러리
from bs4 import BeautifulSoup # 웹크롤링을 하는 라이브러리


url = 'https://finance.naver.com/sise/'
page = urlopen(url)
soup = BeautifulSoup(page, 'html.parser')

all_span = soup.find_all('span', attrs={'id': 'KOSPI_now'})
all_span2 = soup.find_all('span', attrs={'id': 'time1'})

print(all_span)
print(all_span2)

res = [span.string for span in all_span]
for i in res:
    print(i)


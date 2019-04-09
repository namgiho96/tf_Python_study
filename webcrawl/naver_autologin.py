from selenium import webdriver # 웹불러오는 라이브러리

ctx = '../crawler/chromedriver'
driver = webdriver.Chrome(ctx)
driver.implicitly_wait(3)
driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')
driver.find_element_by_name('id').send_keys('giho123') # 아이디를 정해준다
driver.find_element_by_name('pw').send_keys('....')

driver.implicitly_wait(3) # 몇초뒤에 실해해라
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click() # 클릭을 했을때
driver.implicitly_wait(3)




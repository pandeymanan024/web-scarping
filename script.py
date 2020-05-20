from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import urllib.request

search = 'sneakers' 
Download_Directory = 'Download_Image'

driver = webdriver.Chrome('C:/Users\Manc\Downloads\chromedriver_win32\chromedriver.exe')
driver.get('https://www.google.com/')

driver.find_element_by_name('q').send_keys(search)

actions = ActionChains(driver)
actions.send_keys(Keys.ENTER).perform()
#actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
driver.find_element_by_xpath('//*[@id="hdtb-msb-vis"]/div[3]/a').click()
#//*[@id="hdtb-msb-vis"]/div[3]/a

count = scroll = 0
while True:
    count += 1
    scroll += 100
    try:
        driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[{}]/a[1]/div[1]/img'.format(count)).click()
        img = driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[{}]/a[1]/div[1]/img'.format(count))
        img_url = img.get_property('src')

        filepath = Download_Directory + '/Img' + str(count) +'.jpg'
        urllib.request.urlretrieve(img_url,filepath)
        driver.implicitly_wait(2)

        driver.execute_script('window.scrollTo(0,{})'.format(scroll))
        print(count)
    except:
        print(str(count) + 'Not Found')

driver.close()
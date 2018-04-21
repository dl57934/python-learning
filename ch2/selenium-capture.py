from selenium import webdriver 


url = "https://www.naver.com"

browser = webdriver.PhantomJS()

browser.implicitly_wait(3)
browser.get(url)
browser.save_screenshot("Website.png")

browser.quit()

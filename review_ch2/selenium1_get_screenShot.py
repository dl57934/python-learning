import selenium.webdriver as webdriver

browser = webdriver.PhantomJS()

browser.implicitly_wait(3)
browser.get("https://www.google.co.kr")
browser.save_screenshot("google.png")

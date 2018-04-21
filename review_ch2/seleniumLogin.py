import selenium.webdriver as webdriver 

userId= "dl57934"
userpw= "dltkdgns"


browser = webdriver.PhantomJS()
browser.implicitly_wait(3)
loginUrl = "https://nid.naver.com/nidlogin.login"
browser.get(loginUrl)
e = browser.find_element_by_id("id")
e.clear()
e.send_keys(userId)
e = browser.find_element_by_id("pw")
e.clear()
e.send_keys(userpw)
form = browser.find_element_by_css_selector("input.btn_global[type=submit]")
form.submit()

browser.get("https://mail.naver.com/?n=1523353242266&v=f")
mail = browser.find_elements_by_css_selector("a.article span")
for data in mail:
    print(data.text.encode("utf-8"))
browser.quit()


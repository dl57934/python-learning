from selenium import webdriver
import json
id = "dl57934@naver.com"
pw = "!dngmadl14"
browser = webdriver.PhantomJS()
browser.implicitly_wait(3)

url ="https://www.tistory.com/auth/login"

browser.get(url)

e= browser.find_element_by_id("loginId")
e.clear()
e.send_keys(id)
e = browser.find_element_by_id("loginPw")
e.clear()
e.send_keys(pw)
form = browser.find_element_by_css_selector("button.btn_login[type=submit]")
form.submit()

browser.get("http://hoony-gunputer.tistory.com/manage")

results = browser.find_elements_by_tag_name("dd")
for result in results:
    print(result.text)
browser.quit()

from selenium.webdriver import Chrome
import time
import requests
driver = Chrome("./Chromedriver")
# 打開網址
driver.get("https://www.youtube.com/view_all_playlists")
# find -> find_element
# find_all -> findelements
driver.find_element_by_id("identifierId").send_keys("sore9988@gmail.com")
driver.find_element_by_id("identifierNext").click()

time.sleep(2)

driver.find_element_by_class_name("whsOnd").send_keys("b99881612")
driver.find_element_by_id("passwordNext").click()

# while True:
#     jsCode = "window.scrollTo(0, document.body.scrollHeight);"
#     driver.execute_script(jsCode)
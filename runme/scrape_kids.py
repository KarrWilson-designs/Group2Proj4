import selenium
from selenium import webdriver
from seleniumbase import SB
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from time import sleep, strftime, time
from bs4 import BeautifulSoup

##### CHANGE ME TO SOMETHING DIFFERENT
age = 3


def tab_enter(times):
    for i in range(times):
        ActionChains(sb).send_keys(Keys.TAB).perform()
    ActionChains(sb).send_keys(Keys.ENTER).perform()


sb = webdriver.Chrome()


sb.get("https://youtubekids.com")

sleep(1)
parent_button = sb.find_element(By.ID, "parent-button")
parent_button.click()
sleep(1)
next_button = sb.find_element(By.ID, "next-button")
next_button.click()
sleep(1)
ActionChains(sb).send_keys("2001").perform()
sb.implicitly_wait(2)

submit_button = sb.find_element(By.ID, "submit-button")
sleep(1)
try:
    submit_button.click()
except Exception:
    ActionChains(sb).send_keys(Keys.ENTER).perform()

sleep(1)
show_text_button = sb.find_element(By.ID, "show-text-link")
show_text_button.click()
sleep(1)
show_button = sb.find_element(
    By.CLASS_NAME, "style-scope ytk-kids-flow-text-info-renderer"
)
show_button = show_button.find_element(By.ID, "next-button")
show_button.click()
sleep(1)
skip_button = sb.find_element(By.ID, "skip-button")
skip_button.click()
sleep(1)

agree_button = sb.find_element(
    By.CSS_SELECTOR,
    "ytk-kids-onboarding-parental-notice-page-renderer",
)
agree_button = agree_button.find_element(By.ID, "next-button")
agree_button.click()
sleep(1)
tab_enter(age)
select_link = sb.find_element(By.ID, "select-link")
sleep(1)
select_link.click()

tab_enter(1)
sleep(1)
tab_enter(2)
sleep(4)
footer = sb.find_element(By.ID, "grid-footer")
ActionChains(sb).scroll_to_element(footer).perform()
htmlPage = sb.page_source
sb.quit()


with open(f"./parsed_pages/{strftime('%Y-%m-%d_%H-%M-%S')}.html", "x", encoding="utf-8") as f:
    f.write(htmlPage)
    pass


#### Massive note the amount of recommendations changes based on how long you've been usng

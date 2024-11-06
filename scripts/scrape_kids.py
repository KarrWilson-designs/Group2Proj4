"""
Scrape Youtube Kids for recommended videos
Author: Kenneth
Date: CS299 2024
"""

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from time import sleep, strftime


def tab_enter(times):
    """Function to navigate to a button using tabs"""
    for i in range(times):
        ActionChains(sb).send_keys(Keys.TAB).perform()
    ActionChains(sb).send_keys(Keys.ENTER).perform()


for i in range(3):
    sb = webdriver.Chrome()
    sb.get("https://youtubekids.com")

    # all of the following code is navigating the pages
    sleep(5)
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
    tab_enter(i + 1)
    select_link = sb.find_element(By.ID, "select-link")
    sleep(1)
    select_link.click()

    tab_enter(2)
    sleep(1)
    tab_enter(2)
    sleep(4)
    # Scroll down to load all videos
    footer = sb.find_element(By.ID, "grid-footer")
    ActionChains(sb).scroll_to_element(footer).perform()
    # save the page
    htmlPage = sb.page_source
    sb.quit()

    with open(
        f"./parsed_pages/{i}_{strftime('%Y-%m-%d_%H-%M-%S')}_search.html", "x"
    ) as f:
        f.write(htmlPage)
        pass


#### Massive note the amount of recommendations changes based on how long you've been usng

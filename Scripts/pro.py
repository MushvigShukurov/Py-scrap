from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
url = 'https://www.youtube.com/@mushvigsh/videos'

browser = webdriver.Chrome()

browser.get(url=url)
sleep(5)
video = browser.find_element(By.XPATH,"/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-rich-grid-renderer/div[6]/ytd-rich-grid-row[1]/div/ytd-rich-item-renderer[1]/div/ytd-rich-grid-media/div[1]/div[2]/div[1]/h3/a/yt-formatted-string")
video.click()
sleep(10)
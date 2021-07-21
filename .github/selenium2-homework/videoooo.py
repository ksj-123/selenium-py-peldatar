from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:9999/videos.html")

    play_video = driver.find_element_by_id("html5video")
    play_video.click()
    play_video.send_keys(Keys.SPACE)
    time.sleep(4)
    play_video.screenshot('html5video.png')

    play_video = driver.find_element_by_id("video1")
    play = driver.find_element_by_xpath("/html/body/div/button[1]")
    play.click()
    time.sleep(4)
    play_video.screenshot('video1.png')

    play_video = driver.find_element_by_id("youtubeframe")
    play_video.click()
    time.sleep(4)
    play_video.screenshot('youtube.png')

    time.sleep(5)

finally:
    driver.close()

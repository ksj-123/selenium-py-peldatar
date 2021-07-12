import csv
import time

from selenium import webdriver

# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.common.exceptions import NoSuchElementException

# In order for ChromeDriverManager to work you must pip install it in your own environment.
# driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome()

try:
    driver.get("hhttp://localhost:9999/forms.html")

    nowutc = datetime.now(timezone.utc)
    print(nowutc)
    # "Date" mm/dd/yyyy
    driver.find_element_by_id("example-input-date").send_keys(nowutc.strftime("%m/%d/%Y"))
    # "Date / Time" yyyy.mm.dd hh:mm:ss:iii
    driver.find_element_by_id("example-input-date-time").send_keys()
    # "Date / Time local" dd/mm/yyyy hh:mm PM
    driver.find_element_by_id("example-input-date-time-local").send_keys()
    # "Month" month yyyy
    driver.find_element_by_id("example-input-month").send_keys()
    # "Week" week ww, yyyy
    driver.find_element_by_id("example-input-week").send_keys()
    # "Time" hh:mm AM
    driver.find_element_by_id("example-input-time").send_keys()

finally:
    driver.close()


# t = datetime.time(datetime.now())
import csv
import time

from selenium import webdriver

# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.common.exceptions import NoSuchElementException

# In order for ChromeDriverManager to work you must pip install it in your own environment.
# driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome()

try:
    driver.get("hhttp://localhost:9999/another_form.html")

    with open('table_in.csv') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader)
        for row in csvreader:
            print(row)
            name = driver.find_element_by_id("fullname")
            name.clear()
            name.send_keys(row[0])
            email = driver.find_element_by_id("email")
            email.clear()
            email.send_keys(row[1])
            dob = driver.find_element_by_id("dob")
            dob.clear()
            dob.send_keys(row[2])
            phone = driver.find_element_by_id("phone")
            phone.clear()
            phone.send_keys(row[3])
            driver.find_element_by_id('submit').click()
            time.sleep(3)
            output = driver.find_element_by_text('Export HTML table to CSV file')
            for outputs in output:
                print('', output.csv)
        assert 'table_in.csv' == 'output.csv'
finally:
    driver.close()

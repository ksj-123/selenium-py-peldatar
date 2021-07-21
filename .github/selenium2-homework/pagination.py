import csv
import time
import pprint
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

opt = Options()
opt.headless = False

driver = webdriver.Chrome()
extracted_data = []
try:
    driver.get("http://localhost:9999/pagination.html")
    time.sleep(2)
    while True:
        table = driver.find_element_by_xpath('//table[@id="contacts-table"]/tbody')
        rows = table.find_elements_by_tag_name('tr')
        for row in rows:
            data_row = {}
            cells = row.find_elements_by_tag_name('td')
            data_row["Id"] = cells[0].text
            data_row["First name"] = cells[1].text
            data_row["Second name"] = cells[2].text
            data_row["Surname"] = cells[3].text
            data_row["Second Surname"] = cells[4].text
            data_row["Birth date"] = cells[5].text
            if cells[1].text.startswith('A'):
               extracted_data.append(data_row)
        next_button = driver.find_element_by_id('next')
        if not next_button.is_enabled():
            break
        else:
            next_button.click()
    pprint.pprint(extracted_data)
    print(len(extracted_data))

with open("pagination.csv", "w", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(extracted_data)

finally:
driver.close()

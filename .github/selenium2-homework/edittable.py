import csv
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://localhost:9999/editable-table.html")



def find_and_clear_by_id(id):
    element = driver.find_element_by_id(id)
    element.clear()
    return element


add_button = driver.find_element_by_class_name("btn btn-success pull-right")

with open('table.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        print(row)
        driver.find_element_by_name("name").send_keys(row[0])
        driver.find_element_by_name("price").send_keys(row[0])
        driver.find_element_by_name("qty").send_keys(row[0])
        driver.find_element_by_name("category").send_keys(row[0])
        add_button.click()

# controll =

    # placeholder = "Search..."
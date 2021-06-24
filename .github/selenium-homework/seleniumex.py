from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://google.com")

q = driver.find_element_by_id("""<div id="nemletezik"></div""")

try:
    x = input("""<div id="nemletezik"></div""")
except ValueError:
    print("Oops!  That was no valid number.  Try again...")

driver.close()

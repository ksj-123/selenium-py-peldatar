from selenium import webdriver

driver = webdriver.Chrome()
driver.get("hhttp://localhost:9999/todo.html")

span = driver.find_span_by_xpath(/html/body/div/div/div/ul/li[2]/span)

finally:
    driver.close()

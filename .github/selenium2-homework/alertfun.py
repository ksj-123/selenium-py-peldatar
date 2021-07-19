from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

options = Options()
import time

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:9999/alert_playground.html")
    button_alert = driver.find_element_by_xpath("/html/body/div/div[2]/input[1]")
    button_alert.click()
    ref_alert_text = "I am alert"
    alert = driver.switch_to.alert
    assert (alert.text == ref_alert_text)
    print(alert.text)
    time.sleep(2)
    alert.accept()
    time.sleep(2)

    button_conf = driver.find_element_by_xpath("/html/body/div/div[2]/input[2]")
    button_conf.click()
    ref_conf_text = "I am confirm"
    conf = driver.switch_to.alert
    # assert (conf.text == ref_conf_text)
    # print(conf.text)
    # time.sleep(2)
    # alert.accept()  # hiányzik a "mégse" gomb megnyomása
    # time.sleep(2)

    button_prompt = driver.find_element_by_xpath("/html/body/div/div[2]/input[3]")
    button_prompt.click()
    ref_prompt_text = "I am prompt"
    prompt = driver.switch_to.alert
    assert (prompt == ref_prompt_text)
    print(prompt.text)
    time.sleep(2)
    alert.accept()  # hiányzik a szöveg beleírása és a "mégse" gomb megnyomása
    #    if text = "I am prompt"
    # demo = driver.find_element_by_id("demo")
    # ref_demo_text = "You entered: I am prompt"
    # assert (text == ref_demo_text)
    time.sleep(2)

    button_double = driver.find_element_by_id("double-click")
    button_double.click(2)
    ref_double_text = "You double clicked me!!!, You got to be kidding me"
    double = driver.switch_to.alert
    assert (double.text == ref_double_text)
    print(double.text)
    time.sleep(2)
    alert.accept()
    time.sleep(2)

finally:
    pass
    # driver.close()

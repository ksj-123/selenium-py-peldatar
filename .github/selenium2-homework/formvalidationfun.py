from selenium import webdriver
import time

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:9999/simplevalidation.html")

if
    # E-Mail Address (yardy@yarr.com will validate via ajax)
    driver.find_element_by_id("test-email")

    # 6-20 Characters
    driver.find_element_by_id("test-password")

    # Confirm Password
    driver.find_element_by_id("ConfirmPassword")

    # Number
    driver.find_element_by_id("test-customer-number")

    #4 Digits
    driver.find_element_by_id("test-dealer-number")

    # Optional, but if exists should contain the word "twelve"
    driver.find_element_by_id("test-random-field")

    # Format: YYYY-MM-DD
    driver.find_element_by_id("test-date-field")

    # Optionally enter a URL
    driver.find_element_by_id("test-url-field")

    # I heart textareas
    driver.find_element_by_id("test-random-textarea")

    # I heart textareas (" Visa, Master Card, American Express, Discover")
    driver.find_element_by_id("test-card-type")

    # 4111111111111111 will validate (16 chars)
    driver.find_element_by_id("test-card-number")

    # 3 or 4 Digits
    driver.find_element_by_id("test-card-cvv")

    # Select a month (January, February, ...., December)
    driver.find_element_by_id("test-card-month")

    # Select a year (2018, ...., 2027)
    driver.find_element_by_id("test-card-year")

    # Just a regular single checkbox
    driver.find_element_by_id("test-single-checkbox")

    # Receive E-Mail Updates?
    # Yes
    driver.find_element_by_id("test-save-email-yes")
        # or Not
    driver.find_element_by_id("test-save-email-no")

    # Agree to terms of service?
    driver.find_element_by_id("test-terms-sevice")

    # Agree to more stuff?
    driver.find_element_by_id("test-terms-service-more")


click.button("id=test-button")







from selenium import webdriver

# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.common.exceptions import NoSuchElementException

# In order for ChromeDriverManager to work you must pip install it in your own environment.
# driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome()

try:
    driver.get("http://localhost:9999")
    import re

    host = Selenium_PP(html, 'html')
    links = []
    for host in host.find_all(attrs={'href': re.compile("<a href=")}):
        links.append(host.get('href'))
    with open("link.txt", 'w') as out:
        out.write(html.read())
    print(links)

finally:
    driver.close()

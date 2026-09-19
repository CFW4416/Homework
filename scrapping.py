from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

try:
    driver.get("https://ru.wikipedia.org/wiki/%D0%94%D0%BE%D0%BC_%D0%9D%D0%B0%D1%80%D0%BA%D0%BE%D0%BC%D1%84%D0%B8%D0%BD%D0%B0")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "firstHeading"))
    )

    html_content = driver.page_source

    with open("rendered_page.html", "w", encoding="utf-8") as f:
        f.write(html_content)
        
    print("Page successfully saved!")

finally:
    driver.quit()

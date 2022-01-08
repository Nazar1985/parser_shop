from selenium.webdriver.firefox.service import Service
from selenium import webdriver
import settings
from settings.links import TO_SCRAP_CATEGORY
import time
import pickle


def get_favorites_with_auth():
    options = webdriver.FirefoxOptions()
    options.set_preference('general.useragent.override',
                           settings.USER_AGENT)
    service = Service("./geckodriver")
    driver = webdriver.Firefox(service=service, options=options)
    try:
        driver.get(TO_SCRAP_CATEGORY)
        time.sleep(2)
        for cookie in pickle.load(open(f"my_cookies", "rb")):
            driver.add_cookie(cookie)
        time.sleep(2)
        driver.refresh()
        time.sleep(2)
        with open("temp_and_personal_data/favorites_with_auth.html", 'w', encoding='utf-8') as file:
            file.write(driver.page_source)
    except Exception as ex:
        print('Except: ', ex)
    finally:
        driver.close()
        driver.quit()


if __name__ == "__main__":
    get_favorites_with_auth()

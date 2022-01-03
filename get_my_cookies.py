from selenium.webdriver.firefox.service import Service
from selenium import webdriver
import settings
import time
import pickle


def get_my_cookies():
    options = webdriver.FirefoxOptions()
    options.set_preference('general.useragent.override',
                           settings.USER_AGENT)
    service = Service("./geckodriver")
    driver = webdriver.Firefox(service=service, options=options)
    try:
        driver.get("https://www.ozon.ru/my/favorites")
        time.sleep(100)  # time for manual authentication
        pickle.dump(driver.get_cookies(), open(f"/temp_and_personal_data/my_cookies", "wb"))

    except Exception as ex:
        print('Except: ', ex)
    finally:
        driver.close()
        driver.quit()

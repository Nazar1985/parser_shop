import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import settings

def get_page(url):
    """
    Основной функционал поучения страницы указанной во входном параметре
    :param url:
    :return: None
    """
    options = webdriver.FirefoxOptions()
    options.set_preference('general.useragent.override',
                           settings.USER_AGENT)
    service = Service("./geckodriver")
    driver = webdriver.Firefox(service=service, options=options)
    try:
        driver.get(url=url)
        time.sleep(4)
        with open("temp_and_personal_data/index.html", 'w', encoding='utf-8') as file:
            file.write(driver.page_source)
    except Exception as ex:
        print('Except: ', ex)
    finally:
        driver.close()
        driver.quit()

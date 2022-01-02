import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service


def get_page(url):
    """
    Основной функционал поучения страницы указанной во входном параметре
    :param url:
    :return: None
    """
    options = webdriver.FirefoxOptions()
    # user_agent = UserAgent()
    # options.set_preference('general.useragent.override', user_agent.random)
    options.set_preference('general.useragent.override',
                           "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0")
    service = Service("/home/cody/PycharmProjects/parser_shop/geckodriver")
    driver = webdriver.Firefox(service=service, options=options)
    try:
        # driver = webdriver.Firefox(executable_path='geckodriver.exe', options=options)
        driver.get(url=url)
        time.sleep(4)

        with open("index.html", 'w', encoding='utf-8') as file:
            file.write(driver.page_source)

    except Exception as ex:
        print('Except: ', ex)
    finally:
        driver.close()
        driver.quit()

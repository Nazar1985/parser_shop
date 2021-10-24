from webdriver_manager.firefox import GeckoDriverManager


# Заголовки для запуска браузера. в текущей версии не используются
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0"
}

# from def get_page

# set proxy
proxy = "138.128.91.65:8000"
firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
firefox_capabilities["marionette"] = True
firefox_capabilities["proxy"] = {
    "proxyType": "MANUAL",
    "httpProxy": proxy,
    "ftpProxy": proxy,
    "sslProxy": proxy
}

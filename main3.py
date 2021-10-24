import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from multiprocessing import Pool
from fake_useragent import UserAgent


"""
Вручную сформированный словарь категорий (не полный перечень). 
В дальнейшем необходимо предусмотреть возможность получать автоматически весь словарь категорий и подкатегорий.
"""
category_list = {'a': ['Компьютерные технологии', 'kompyuternye-tehnologii-40020'],
                 'b': ['1C', '1s-33713'],
                 'c': ['Анализ данных', 'analiz-dannyh-33707'],
                 'd': ['Базы данных', 'bazy-dannyh-33708'],
                 'e': ['Веб разработка', 'veb-razrabotka-35675'],
                 'f': ['Графика и дизайн', 'grafika-i-dizayn-33706'],
                 'g': ['Интернет и социальные сети', 'internet-i-sotsialnye-seti-35678'],
                 'h': ['Информационная безопасность', 'informatsionnaya-bezopasnost-33711'],
                 'i': ['Компьютерные сети', 'kompyuternye-seti-33709'],
                 'j': ['Машинное обучение', 'mashinnoe-obuchenie-35674'],
                 'k': ['Языки программирования', 'yazyki-programmirovaniya-33705']
                 }
# Множество доступных букв для ограничения выбора категорий
# сформировано вручную, необходимо автоматизировать формирование из словаря выше.
alpha = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'}
url_category = 'https://www.ozon.ru/category/'
url_test_category = "https://www.ozon.ru/category/kompyuternye-tehnologii-40020/?page=100"
# https://www.ozon.ru/category/kompyuternye-tehnologii-40020/?page=2


def print_list_category():
    """
    Отображение спика категорий в терминале (нужно упковать в функцию, чтобы вызывать повторно).
    Как вариант можно внести в функцию select_category, но дядушка Боб будет ругаться ))
    """
    for k, v in category_list.items():
        print(k + ': ', v[0])


def print_pages_count(n):
    """
    Функция для корректного вывода количества страниц в категории с данными
    :param n:
    :return:
    """
    if n % 10 == 1 and n % 100 != 11:
        print('Найдена %s страница с товаром в выбранной категориии!' % n)
    elif n % 100 != 12 and n % 100 != 13 and n % 100 != 14 and (n % 10 == 2 or n % 10 == 3 or n % 10 == 4):
        print('Найдено %s страницы с товаром в выбранной категориии!' % n)
    else:
        print('Найдено %s страниц с товаром в выбранной категориии!' % n)


def select_category(category):
    """
    Функция выбора категории для сканирования из полученного списка
    категорий в виде словаря (см. category_list). Функция актуальна
    для ручного запуска через терминал или через телеграмм бот.
    :param category: получение словаря категорий.
    :return: возвращает ссылку на выбранную категорию.
    """
    print_list_category()  # Временное решение. При выводе запускаемых файлов переопределить место вызова
    while True:
        choice = input('Выберите категорию:').strip()
        if choice.isalpha() and choice in alpha:
            print('Вы выбрали категорию: ' + category[choice][0])
            return category[choice][1]


def list_links(url, category):
    """
    Генератор ссылок для категории
    :param url: Главная ссылка для всех категорий
    :param category: Выбранная категория
    :return: список категорий в виде генератора
    """
    links_list = []
    for n in range(1, 2):    # в целях отладки указал верхний предел 2, в дальнейшем поставить 500
        link = url + category + "/?page=" + str(n)
        links_list.append(link)
    return links_list


def get_page(url):
    """
    Основной функционал поучения страницы укзаанной во вхоном параметре
    :param url:
    :return:
    """
    options = webdriver.FirefoxOptions()
    # user_agent = UserAgent()
    # options.set_preference('general.useragent.override', user_agent.random)
    options.set_preference('general.useragent.override',
                           "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0")
    service = Service("geckodriver.exe")
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


def iter_of_pages(urls):
    """
    Получение страниц через ссылки полученные из генератора (list_links())
    :param urls:    ссылка сформированная генератором
    :return:
    """
    n_pages = 0
    text_error = '`Простите`, произошла ошибка'
    for url in urls:
        get_page(url)
        with open("index.html", encoding='utf-8') as file:
            src = file.read()
        if text_error in src:
            break
        get_link(src)
        get_info(get_all_items(src))
        n_pages += 1
    print_pages_count(n_pages)
    return 'a'


def get_all_items(src):
    """
    Функция для скрапинга данных из сохраненной страницы index.html
    :param src: открытый файл index.html
    :return: html разметку всех книг
    """
    soup = BeautifulSoup(src, 'lxml')
    books_on_list = soup.find_all("div", class_="bi1")
    return books_on_list


def get_info(books):
    """

    :param books:
    :return:
    """
    data_books = dict()
    for book in books:
        print(book)
        # Наименование книги
        # if book.find("span", class_='a7y a8a2 a8a6 a8b2'):
        book_name = book.find("span", class_='a7y a8a2 a8a6 a8b2')
        data_books['name'] = book_name  # .text.strip()
        # Цена со скидкой
        if book.find("span", class_='_2DV4 _17o0 _1v1b'):
            book_name1 = book.find("span", class_='_2DV4 _17o0 _1v1b')
        # Цена без скидки
        if book.find("span", class_='skSe _17o0'):
            book_name2 = book.find("span", class_='skSe _17o0')
        # Цена с купоном
        if book.find("span", class_='a7y a8a2 a8a6 a8b6'):
            book_name3 = book.find("span", class_='a7y a8a2 a8a6 a8b6')
        # Часть ссылки для перехода к книге
        if book.find("span", class_='a7y a8a2 a8a6 a8b2'):
            book_name4 = book.find("span", class_='a7y a8a2 a8a6 a8b2')
        # data_books[book] = 1
        print(data_books)


def get_link(src):
    soup = BeautifulSoup(src, 'lxml')
    book_cards = soup.find_all("div", class_="bj4 a8p1")
    for book_url in book_cards:
        book_url = "https://www.ozon.ru" + book_url.find("a").get("href")
        print(book_url)

def main():
    """
    Функция содержащая всю логику приложения. Точка запуска
    :return:
    """
    iter_of_pages(list_links(url_category, select_category(category_list)))
    # get_list_pages(url_grand)
    # get_page()
    # get_info(get_all_items())


if __name__ == '__main__':
    # p = Pool(processes=3)
    # p.map(get_page, list_links(url_category, select_category(category_list)))
    main()

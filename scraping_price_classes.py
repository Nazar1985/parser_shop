from get_page import get_page
from bs4 import BeautifulSoup, SoupStrainer


def scraper_prices():
    """
    Скрапинг классов цен для автоматического обновления.
    """
    url = "https://www.ozon.ru/category/kompyuternye-tehnologii-40020/"
    get_page(url)
    with open("index.html", encoding='utf-8') as file:
        src = file.read()
        only_class = SoupStrainer(class_="bi1")
        soup = BeautifulSoup(src, 'lxml', parse_only=only_class)
        cost_with_discount = soup.find("span")                                # ui-p9 ui-q1 ui-q4
        cost_without_discount = cost_with_discount.find_next_sibling("span")  # ui-q5 ui-q1

        class_cost_with_discount = " ".join(cost_with_discount["class"])
        class_cost_without_discount = " ".join(cost_without_discount["class"])
        class_cost_full = " ".join(cost_with_discount["class"][:-1])
        return class_cost_with_discount, class_cost_without_discount, class_cost_full


if __name__ == '__main__':
    scraper_prices()


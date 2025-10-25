import time
from selenium.webdriver.common.by import By


def test_guest_should_see_add_to_basket_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    
    # Для визуальной проверки языка (по требованию задания)
    time.sleep(30)

    # Проверяем наличие кнопки "Добавить в корзину"
    add_to_basket_button = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
    assert add_to_basket_button.is_displayed(), "Button 'Add to basket' is not present on the page"
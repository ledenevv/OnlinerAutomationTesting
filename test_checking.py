import re
import time
from playwright.sync_api import Page, expect

def test_get_started_link(page: Page):
    page.goto("https://catalog.onliner.by/")

    # Click the get started link.
    page.locator("text=' Вход '").click()

    element_locator = page.locator(".auth-wrapper")

    # Проверка, что элемент с классом существует
    expect(element_locator).to_be_visible()  # Проверка видимости элемента

def test_comparing(page: Page):
    page.goto("https://catalog.onliner.by/mobile")
    checkboxes = page.query_selector_all('.catalog-form__checkbox-label')
    checkboxes[0].click()
    page.locator("#submit-button").click()
    element_locator = page.locator(".catalog-interaction__inner-container_visible")
    expect(element_locator).to_be_visible()

def test_comparing_menu(page: Page):
    page.goto("https://catalog.onliner.by/mobile")
    checkboxes = page.query_selector_all('.catalog-form__checkbox-label')
    checkboxes[0].click()
    page.locator("#submit-button").click()
    product = page.query_selector_all(".catalog-form__link.catalog-form__link_primary-additional.catalog-form__link_base-additional.catalog-form__link_font-weight_semibold.catalog-form__link_nodecor")
    product1 = product[0].inner_text().strip()
    print(product1)
    page.locator(".catalog-interaction__inner-container_visible").click()
    page.wait_for_selector(".product-summary__caption")    
    product_result = page.query_selector_all(".product-summary__caption")
    if len(product_result) > 0:
        product2 = product_result[0].text_content().strip()
        print(product2)
        expect(product1).to_have_text(product2)
    else:
        print("Нет результатов продукта.")
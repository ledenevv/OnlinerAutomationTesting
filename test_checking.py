import re
import time
import requests
import asyncio
import pytest
from playwright.async_api import async_playwright
from playwright.sync_api import Page, expect


# def test_get_started_link(page: Page):
#     page.goto("https://catalog.onliner.by/")

#     # Click the get started link.
#     page.locator("text=' Вход '").click()

#     element_locator = page.locator(".auth-wrapper")

#     # Проверка, что элемент с классом существует
#     expect(element_locator).to_be_visible()  # Проверка видимости элемента

# def test_comparing(page: Page):
#     page.goto("https://catalog.onliner.by/mobile")
#     checkboxes = page.query_selector_all('.catalog-form__checkbox-label')
#     checkboxes[0].click()
#     page.locator("#submit-button").click()
#     element_locator = page.locator(".catalog-interaction__inner-container_visible")
#     expect(element_locator).to_be_visible()

# def test_comparing_menu(page: Page):
#     page.goto("https://catalog.onliner.by/mobile")
#     checkboxes = page.query_selector_all('.catalog-form__checkbox-label')
#     checkboxes[0].click()
#     # page.locator("#submit-button").click()
#     product1 = page.locator(".catalog-form__link.catalog-form__link_primary-additional.catalog-form__link_base-additional.catalog-form__link_font-weight_semibold.catalog-form__link_nodecor").first
#     element = product1.get_attribute("href")
#     print(element)
#     page.locator(".catalog-interaction__inner-container_visible").click()
#     page.wait_for_selector(".product-summary__caption")
#     element1 = page.locator(".product-summary__figure").first
#     element2 = element1.get_attribute("href")
#     print(element)
#     print(element2)
#     assert element == element2

# @pytest.mark.asyncio
# async def test_check_product_json():
#     response = requests.get("https://catalog.onliner.by/sdapi/catalog.api/search/mobile")
#     data = response.json()
#     url = "https://catalog.onliner.by/mobile"
    
#     parameters_dict = await extract_parameters(url)
#     print(parameters_dict)
    
#     assert parameters_dict == 1 

# async def extract_parameters(url):
#     async with async_playwright() as p:
#         browser = await p.chromium.launch()
#         page = await browser.new_page()
#         await page.goto(url)

#         parameter_elements = await page.query_selector_all('.catalog-form__parameter-part')
        
#         parameters = {}

#         for idx, element in enumerate(parameter_elements):
#             text = await element.inner_text()
#             parameters[f'parameter_{idx + 1}'] = text
        
#         await browser.close()
#         return parameters

def test_nav_check_news(page: Page):
    page.goto("https://catalog.onliner.by/")
    element = page.locator(".b-main-navigation__text").and_(page.get_by_text("Новости"))
    element.hover()
    assert page.locator(".b-main-navigation__dropdown.b-main-navigation__dropdown_visible").is_visible()

def test_nav_check_autosale(page: Page):
    page.goto("https://catalog.onliner.by/")
    element = page.locator(".b-main-navigation__text").and_(page.get_by_text("Автобарахолка"))
    element.hover()
    assert page.locator(".b-main-navigation__dropdown.b-main-navigation__dropdown_visible").is_visible()

def test_nav_check_houses_and_flats(page: Page):
    page.goto("https://catalog.onliner.by/")
    element = page.locator(".b-main-navigation__text").and_(page.get_by_text("Дома и квартиры"))
    element.hover()
    assert page.locator(".b-main-navigation__dropdown.b-main-navigation__dropdown_visible").is_visible()


import re
import time
import requests
import asyncio
import pytest
from playwright.async_api import async_playwright
from playwright.sync_api import Page, expect


# def test_get_started_link(page: Page):
#     page.goto("https://catalog.onliner.by/")
#     page.locator("text=' Вход '").click()
#     element_locator = page.locator(".auth-wrapper")
#     expect(element_locator).to_be_visible() 

# def test_comparing(page: Page):
#     page.goto("https://catalog.onliner.by/mobile")
#     checkboxes = page.query_selector_all('.catalog-form__checkbox-label')
#     checkboxes[0].click()
#     # page.locator("#submit-button").click()
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

# def test_nav_check_news(page: Page):
#     page.goto("https://catalog.onliner.by/")
#     element = page.locator(".b-main-navigation__text").and_(page.get_by_text("Новости"))
#     element.hover()
#     assert page.locator(".b-main-navigation__dropdown.b-main-navigation__dropdown_visible").is_visible()

# def test_nav_check_autosale(page: Page):
#     page.goto("https://catalog.onliner.by/")
#     element = page.locator(".b-main-navigation__text").and_(page.get_by_text("Автобарахолка"))
#     element.hover()
#     assert page.locator(".b-main-navigation__dropdown.b-main-navigation__dropdown_visible").is_visible()

# def test_nav_check_houses_and_flats(page: Page):
#     page.goto("https://catalog.onliner.by/")
#     element = page.locator(".b-main-navigation__text").and_(page.get_by_text("Дома и квартиры"))
#     element.hover()
#     assert page.locator(".b-main-navigation__dropdown.b-main-navigation__dropdown_visible").is_visible()

# def test_offers(page: Page):
#     page.goto("https://catalog.onliner.by/mobile")
#     redirection = page.query_selector(".button-style.button-style_secondary.button-style_small-alter.catalog-form__button.catalog-form__button_min-width_xxxss")
#     redirection.click()
#     page.wait_for_selector(".offers-list__item, .offers-list__item.offers-list__item_highlighted")
#     offer = page.query_selector(".offers-list__item")
#     highlighted_offer = page.query_selector(".offers-list__item.offers-list__item_highlighted")
#     assert  offer.is_visible() or highlighted_offer.is_visible()

# def test_offers_info_marker(page: Page):
#     page.goto("https://catalog.onliner.by/mobile/xiaomi/x14tp12512bt/prices")
#     page.query_selector("span.button-style.button-style_another.button-style_base.offers-form__button").click()
#     info_marker = page.query_selector("span.offers-list__popover-handle")
#     info_marker.click()
#     element = page.locator(".popover-style__handle_visible")
#     assert element.is_visible()

def test_offers_filtering_checkboxes(page: Page):
    page.goto("https://catalog.onliner.by/mobile/xiaomi/x14tp12512bt/prices")
    element = page.locator("label.offers-form__bonus-item.offers-form__bonus-item_primary div.i-checkbox.offers-form__checkbox.offers-form__checkbox_base-alter div.i-checkbox__faux")
    element.check()
    assert element.is_checked()

def test_offers_filtering_message(page: Page):
    page.goto("https://catalog.onliner.by/mobile/xiaomi/x14tp12512bt/prices")
    checkbox = page.locator("label.offers-form__bonus-item.offers-form__bonus-item_primary div.i-checkbox.offers-form__checkbox.offers-form__checkbox_base-alter div.i-checkbox__faux")
    checkbox.check()
    element = page.locator(".offers-list__tag-item")
    assert element.is_visible()

def test_closing_offers_filtering_message(page: Page):
    page.goto("https://catalog.onliner.by/mobile/xiaomi/x14tp12512bt/prices")
    checkbox = page.locator("label.offers-form__bonus-item.offers-form__bonus-item_primary div.i-checkbox.offers-form__checkbox.offers-form__checkbox_base-alter div.i-checkbox__faux")
    checkbox.check()
    element = page.locator(".offers-list__tag-item")
    if element.is_visible():
        element.click()
        assert element.is_hidden()


    

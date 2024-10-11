import re
import time
import requests
import asyncio
import pytest
from playwright.async_api import async_playwright
from playwright.sync_api import Page, expect

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

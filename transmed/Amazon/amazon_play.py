from playwright.sync_api import sync_playwright
import re

with sync_playwright() as p:
    browser = p.chromium.launch()  # Or use firefox.launch() or webkit.launch()
    page = browser.new_page()

    try:
        page.goto("https://www.amazon.ae/Energizer-E92Bp12-Alkaline-Batteries-Pieces/dp/B006T9DS0A/ref=sr_1_1?crid=1NVUFI9EFR8N6&dib=eyJ2IjoiMSJ9.W93UX_p2_VWUdTOE-pj_Ig.7fmPst0OnsxOfRJiR_XQS33kvP_GfUnNhw6w_e6BGh0&dib_tag=se&keywords=B006T9DS0A&qid=1709647089&sprefix=b006t9ds0a%2Caps%2C253&sr=8-1&th=1")
        best_sellers_list = page.query_selector('ul.a-unordered-list:nth-child(4) > li:nth-child(1) > span:nth-child(1)').inner_text()
        best_sellers_list = re.findall(r"#(\d+)", best_sellers_list)
        catgroup_best_sellers_rank = best_sellers_list[0]
        category_best_sellers_rank = best_sellers_list[1]

    except Exception as e:
        print(f"{e} - No se pudo extraer el Best Seller Rank")

    browser.close()
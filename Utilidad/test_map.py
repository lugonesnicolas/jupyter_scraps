import requests
import time
from bs4 import BeautifulSoup
import concurrent.futures

# Proxy 
username = 'Ec0m37ry'
password = 'fK7Ulvdm8zSVnyn22+'
proxy = f"http://{username}:{password}@ar.smartproxy.com:10000"

def scrape_product_info(url):
    """Fetches product information from the given URL."""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0',
        # ... other headers as needed
    }

    try:
        response = requests.get(url, headers=headers, proxies = {'https': proxy})
        response.raise_for_status()  # Raise an exception for non-2xx status codes
        html_content = response.text
        soup = BeautifulSoup(html_content, "html.parser")
        title = soup.select_one("div h1.product_page").text.strip()
        print(f"Title: {title}")
        print(f"URL: {url}\n")
    except requests.exceptions.RequestException as e:
        print(f"Error scraping URL {url}: {e}")

def main():
    """Executes parallel scraping for two URLs."""
    urls = [
        "https://www.cotodigital3.com.ar/sitios/cdigi/producto/-mini-torta-dulce-de-leche-chocolate-genio-70g/_/A-00562292-00562292-200",
        "https://www.cotodigital3.com.ar/sitios/cdigi/producto/-alfajor-fruta-sol-serrano-fwp-40-grm/_/A-00523603-00523603-200",
        "https://www.cotodigital3.com.ar/sitios/cdigi/producto/-papas-fritas-sabor-queso-crema-y-cebolla-lays-34g/_/A-00567599-00567599-200",
        "https://www.cotodigital3.com.ar/sitios/cdigi/producto/-papas-fritas-jamon-serrano-lays-34g/_/A-00567588-00567588-200",
        "https://www.cotodigital3.com.ar/sitios/cdigi/producto/-papas-fritas-queso-crema-y-cebolla-lays-77g/_/A-00567600-00567600-200",
        "https://www.cotodigital3.com.ar/sitios/cdigi/producto/-alfajor-fruta-sol-serrano-fwp-40-grm/_/A-00523603-00523603-200",
        "https://www.cotodigital3.com.ar/sitios/cdigi/producto/-gaseosa-pepsi----lata-354-cc-/_/A-00006664-00006664-200",
        "https://www.cotodigital3.com.ar/sitios/cdigi/producto/-gaseosa-cola-black-pepsi-2000cc/_/A-00580664-00580664-200",
        "https://www.cotodigital3.com.ar/sitios/cdigi/producto/-gaseosa-cola-pepsi-250-ml/_/A-00544038-00544038-200",
        "https://www.cotodigital3.com.ar/sitios/cdigi/producto/-gaseosa-coca-cola-zero-354-ml/_/A-00179844-00179844-200"
    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(scrape_product_info, urls)

if __name__ == "__main__":
    inicio = time.time()
    main()
    fin = time.time()
    tiempo_total = fin - inicio
    print("El código tardó:", tiempo_total, "segundos")
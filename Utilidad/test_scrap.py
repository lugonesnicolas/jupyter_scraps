import requests
import time
from bs4 import BeautifulSoup

# Proxy 
username = 'Ec0m37ry'
password = 'fK7Ulvdm8zSVnyn22+'
proxy = f"http://{username}:{password}@ar.smartproxy.com:10000"

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

payload = {}
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8',
  'Accept-Language': 'es-AR,es;q=0.8,en-US;q=0.5,en;q=0.3',
  'Accept-Encoding': 'gzip, deflate, br, zstd',
  'Referer': 'https://www.cotodigital3.com.ar/sitios/cdigi/browse/catalogo-almac^%^C3^%^A9n-golosinas-alfajores/_/N-1njwjm5',
  'DNT': '1',
  'Sec-GPC': '1',
  'Connection': 'keep-alive',
  'Cookie': 'userPrefLanguage=es_AR; cookiesession1=678A3E0D19A04FF2F18097FD4C5AE0A9; _ga_6XM8K9GD1N=GS1.1.1729200866.7.1.1729200877.49.0.0; _ga=GA1.1.641347817.1720100443; _gcl_gs=2.1.k1$i1725026119; JSESSIONID=nxacZoOl4Zy7CX1jrUpM_vhVj2UFi3SBAtm9_K9lKV1zUKWyi76T^!-350122699; _gcl_au=1.1.836238390.1729200866; prophetsec_cookie=^%^7B^%^22enterName^%^22^%^3A^%^22cotodigital3^%^22^%^2C^%^22clientId^%^22^%^3A^%^221907df9d44249b-096abf0fe51762-e525627-1fa400-1907df9d443a26^%^22^%^2C^%^22^%^24prevtransid^%^22^%^3A^%^5B1729200878895^%^2C^%^221929c67456292d-0e972d38511dcf-f545721-1fa400-1929c674563950^%^22^%^2C1729200866657^%^5D^%^2C^%^22transId^%^22^%^3A^%^221929c67456292d-0e972d38511dcf-f545721-1fa400-1929c674563950^%^22^%^2C^%^22^%^24transid^%^22^%^3A^%^5B1729200880567^%^2C^%^221929c67456292d-0e972d38511dcf-f545721-1fa400-1929c674563950^%^22^%^2C1729200866657^%^5D^%^2C^%^22transLabel^%^22^%^3A^%^22telemetry^%^22^%^7D; userPrefLanguage=es_AR; JSESSIONID=YwecZ0FYSQsH1Rb9KncnleTUuzzObNFYyamatpzMS3OOicP9YzTT!-350122699',
  'Upgrade-Insecure-Requests': '1',
  'Sec-Fetch-Dest': 'document',
  'Sec-Fetch-Mode': 'navigate',
  'Sec-Fetch-Site': 'same-origin',
  'Sec-Fetch-User': '?1',
  'Priority': 'u=0, i'
}

def get_data(url):
    response = requests.request("GET", url, headers=headers, data=payload, proxies = {'https': proxy})

    html_content = response.text
    soup = BeautifulSoup(html_content, "html.parser")
    title = soup.select_one("div h1.product_page").text.strip()
    print(f"Title: {title}")
    print(f"URL: {url}\n")

if __name__ == "__main__":
    inicio = time.time()
    for url in urls:
        get_data(url)
        
    fin = time.time()
    tiempo_total = fin - inicio
    print("El código tardó:", tiempo_total, "segundos")
import scrapy
from selenium import webdriver
import BeOnFastCode as fc
from selenium.webdriver.common.by import By
from time import sleep
import BeOnScrapingSettings as ss
import time

class ProductosSpider(scrapy.Spider):
    name = 'productos'
    allowed_domains = ['www.supermercado.laanonimaonline.com']
    start_urls = ['https://supermercado.laanonimaonline.com/']

    def __init__(self):
        self.driver = webdriver.Chrome(options = ss.set_chrome_options( headless_status=False,
                                                                        proxy_status=True,
                                                                        proxy_country="ar",
                                                                        proxy_port=10000,
                                                                        useragent_status=False,
                                                                        full_screen=True))
        self.driver.get(self.start_url)
        time.sleep(3)
        fc.click(driver=self.driver, css="#popup-envio > div > div:nth-child(3) > div")
        time.sleep(5)
        fc.click(driver=self.driver, css="#notificacion-btn-cerrar")
        time.sleep(2)
        #Click en agragar ubicacion
        fc.click(driver=self.driver, css=".local_actual")
        time.sleep(2)
        #Selector provincia
        fc.click(driver=self.driver, css="#sel_provincia")
        fc.click(driver=self.driver, css="#sel_provincia > option:nth-child(6)")
        #Selector localidad
        fc.click(driver=self.driver, css="#sel_localidad_3")
        fc.click(driver=self.driver, css="#sel_localidad_3 > option:nth-child(3)")
        #Selector sucursal
        fc.click(driver=self.driver, css="#sel_sucursal_3")
        fc.click(driver=self.driver, css="#sel_sucursal_3 > option:nth-child(2)")
        #Confirmar
        fc.click(driver=self.driver, css=".estandar")
        time.sleep(1)

    def parse(self, response):
        # Esperar a que la página cargue completamente (ajusta el tiempo según sea necesario)
        sleep(3)

        final_price = fc.scrap_text(response=response, css="div.precio-promo div.precio.destacado")
        old_price = fc.scrap_text(response=response, css="div#detalle_producto div.precio_complemento.aux1 div.precio.anterior")

        yield {
            'final_price': final_price,
            'old_price': old_price
        }

    def closed(self, reason):
        self.driver.quit()
import allure
from locators import LogoPageLocators
from pages.base_page import BasePageScooter
from data.urls import URLS

class LogoPageScooter(BasePageScooter):

   #Метод перехода по логотипу Самоката
   @allure.step("Нажимаем на логотип Самоката")
   def go_to_logo_scooter(self):
      self.wait_element_to_be_clickable(LogoPageLocators.LOGO_SCOOTER).click()
      self.wait_url_contains(URLS.SCOOTER_MAIN_URL)

   #Метод перехода по логотипу Яндекса
   @allure.step("Нажимаем на логотип Яндекса")
   def go_to_logo_yandex(self):
      self.wait_element_to_be_clickable(LogoPageLocators.LOGO_YANDEX).click()
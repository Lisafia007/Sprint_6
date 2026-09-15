import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import LogoPageLocators
from pages.base_page import BasePageScooter
from data.urls import URLS

class LogoPageScooter(BasePageScooter):

   #Метод проверки содержания элемента в url страницы
   @allure.step("Проверяем, что элемент содержится в url страницы")
   def wait_url_page(self, loc_path, wait_time = 10):
      WebDriverWait(self.driver, wait_time).until(expected_conditions.url_contains(loc_path))

   #Метод перехода по логотипу Самоката
   @allure.step("Нажимаем на логотип Самоката")
   def go_to_logo_scooter(self):
      self.wait_element_to_be_clickable(LogoPageLocators.LOGO_SCOOTER).click()
      self.wait_url_page(URLS.SCOOTER_MAIN_URL)

   #Метод перехода по логотипу Яндекса
   @allure.step("Нажимаем на логотип Яндекса")
   def go_to_logo_yandex(self):
      self.wait_element_to_be_clickable(LogoPageLocators.LOGO_YANDEX).click()
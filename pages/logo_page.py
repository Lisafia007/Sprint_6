import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import LogoPageLocators
from pages.base_page import BasePageScooter

class LogoPageScooter(BasePageScooter):

   #Метод перехода по логотипу Самоката
   @allure.step("Нажимаем на логотип Самоката")
   def go_to_logo_scooter(self):
      WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(LogoPageLocators.LOGO_SCOOTER)).click()
      WebDriverWait(self.driver, 5).until(expected_conditions.url_to_be("https://qa-scooter.praktikum-services.ru/"))

   #Метод перехода по логотипу Яндекса
   @allure.step("Нажимаем на логотип Яндекса")
   def go_to_logo_yandex(self):
      WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(LogoPageLocators.LOGO_YANDEX)).click()
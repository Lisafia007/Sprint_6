import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import OrderButtonLocators
from pages.base_page import BasePageScooter


class OrderButtonScooter(BasePageScooter):

   #Метод нажатия на кнопку "Заказать"
   @allure.step("Нажимаем на кнопку 'Заказать'")
   def click_order_button(self, locator):
      self.wait_element_to_be_clickable(locator).click()
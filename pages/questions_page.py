import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import QuestionsPageLocators
from pages.base_page import BasePageScooter


class QuestionsPageScooter(BasePageScooter):

   def __init__(self, driver):
        self.driver = driver

   #Метод для перехода к разделу с вопросами
   @allure.step("Перезодим к разделу с вопросами")
   def go_to_questions_section(self):
      elements_questions_section = self.driver.find_element(*QuestionsPageLocators.QUESTIONS_SECTION)
      self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", elements_questions_section)

   #Метод для ожидания появления раздела с вопросами
   @allure.step("Ожидаем появления раздела с вопросами")
   def wait_for_questions_sectiion(self):
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(QuestionsPageLocators.QUESTIONS_SECTION))

   #Объединение методов в шаг для перехода к разделу с вопросами
   @allure.step("Объединям методы для перехода к разделу с вопросами в шаг")
   def section(self):
      self.go_to_questions_section()
      self.wait_for_questions_sectiion()

   #Метод нажатия на стрелку
   @allure.step("Нажимаем на стрелку у вопроса")
   def check_arrow(self, index):
      arrow = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(QuestionsPageLocators.ARROWS[index]))
      self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", arrow)
      self.driver.execute_script("arguments[0].click();", arrow) 
       
   #Метод ожидания отображения соответствующего текста
   @allure.step("Отображение соответствующего текста для вопроса")
   def check_text(self, index):
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(QuestionsPageLocators.TEXTS[index]))

   #Объединение методов в шаг для открытия текста соответсвующего вопросу
   @allure.step("Объединение методов в шаг для открытия текста соответсвующего вопросу")
   def text_check_after_click(self, index):
      self.check_arrow(index)
      self.check_text(index)
import allure
from locators import QuestionsPageLocators
from pages.base_page import BasePageScooter


class QuestionsPageScooter(BasePageScooter):

   #Метод для перехода к разделу с вопросами
   @allure.step("Переходим к разделу с вопросами")
   def go_to_questions_section(self):
      elements_questions_section = self.element(QuestionsPageLocators.QUESTIONS_SECTION)
      self.scroll_to_element(elements_questions_section)

   #Метод для ожидания появления раздела с вопросами
   @allure.step("Ожидаем появления раздела с вопросами")
   def wait_for_questions_section(self):
      self.wait_element_visibility(QuestionsPageLocators.QUESTIONS_SECTION)

   #Объединение методов в шаг для перехода к разделу с вопросами
   @allure.step("Объединям методы для перехода к разделу с вопросами в шаг")
   def section(self):
      self.go_to_questions_section()
      self.wait_for_questions_section()

   #Метод нажатия на стрелку
   @allure.step("Нажимаем на стрелку у вопроса")
   def check_arrow(self, index):
      arrow = self.wait_element_to_be_clickable(QuestionsPageLocators.ARROWS[index])
      self.scroll_to_element(arrow)
      self.click_js(arrow) 
       
   #Метод ожидания отображения соответствующего текста
   @allure.step("Отображение соответствующего текста для вопроса")
   def check_text(self, index):
      self.wait_element_visibility(QuestionsPageLocators.TEXTS[index])

   #Объединение методов в шаг для открытия текста соответсвующего вопросу
   @allure.step("Объединение методов в шаг для открытия текста соответсвующего вопросу")
   def text_check_after_click(self, index):
      self.check_arrow(index)
      self.check_text(index)
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import BasePageLocators, OrderButtonLocators


class BasePageScooter():

   def __init__(self, driver):
      self.driver = driver

   def wait_element_visibility(self, loc_path, wait_time = 10):
      return WebDriverWait(self.driver, wait_time).until(expected_conditions.visibility_of_element_located(loc_path))

   def wait_element_to_be_clickable(self, loc_path, wait_time = 10):
      return WebDriverWait(self.driver, wait_time).until(expected_conditions.element_to_be_clickable(loc_path))

   def element(self, loc_path):
      return self.driver.find_element(*loc_path)

   #Метод перезагрузки данных
   @allure.step("Перезагружаем данные объекта")
   def refresh(self):
      self.driver.refresh()

   #Метод нажатия на кнопку "Да все привыкли" для закрытия плашки о куках
   @allure.step("Нажимаем на кнопку 'Да все привыкли' для закрытия плашки о куках" )
   def close_cookie(self):
      self.wait_element_visibility(BasePageLocators.COOKIE_FIELD)
      cookie_button = self.element(BasePageLocators.COOKIE_CLOSE_BUTTON)
      cookie_button.click()

   #Метод ожидания загрузки формы 'Для кого самокат'
   @allure.step("Ожидаем загрузки заголовка формы 'Для кого самокат'" )
   def wait_for_data_form(self):
      self.wait_element_visibility(BasePageLocators.HEADER_DATA_FORM)

   #Метод введения данных в поле Имя
   @allure.step("Вводим данные в поле Имя")
   def input_name(self, data):
      self.element(BasePageLocators.NAME_FIELD).click()
      self.element(BasePageLocators.NAME_FIELD).send_keys(data["name_field"])

   #Метод введения данных в поле Фамилия 
   @allure.step("Вводим данные в поле Фамилия")
   def input_surname(self, data):
      self.element(BasePageLocators.SURNAME_FIELD).click()
      self.element(BasePageLocators.SURNAME_FIELD).send_keys(data["surname_field"])

   #Метод введения данных в поле Адрес
   @allure.step("Вводим данные в поле Адрес")
   def input_address(self, data):
      self.element(BasePageLocators.ADDRESS_FIELD).click()
      self.element(BasePageLocators.ADDRESS_FIELD).send_keys(data["address_field"])

   #Метод выбора станции метро
   @allure.step("Выбираем станцию метро из списка")
   def choose_metro(self, data):
      self.element(BasePageLocators.METRO_FIELD).click()
      metro = data['metro_name']
      self.wait_element_to_be_clickable((By.XPATH, f"//div[text()='{metro}']")).click()

   #Метод введения данных в поле Телефон
   @allure.step("Вводим данные в поле Телефон")
   def input_phone(self, data):
      self.element(BasePageLocators.PHONE_FIELD).click()
      self.element(BasePageLocators.PHONE_FIELD).send_keys(data["phone_field"])

   #Метод для перехода к следующей странице
   @allure.step("Переходим к следующей странице после заполнения формы на странице 'Для кого самокат'")
   def go_to_page(self):
      self.element(BasePageLocators.NEXT_BUTTON).click()

   #Объединение методов для заполнения формы данных заказа в шаг
   @allure.step("Объединям методы для заполнения формы данных заказа в шаг")
   def filling_out_form(self, data):
      self.input_name(data)
      self.input_surname(data)
      self.input_address(data)
      self.choose_metro(data)
      self.input_phone(data)
      self.go_to_page()

   #Метод выбора дня
   @allure.step("Выбираем день аренды самоката")
   def choose_day(self, data):
      self.element(BasePageLocators.DATA_DAY_FIELD).click()
      day = (data["data_day"])
      select_day = (By.XPATH, f"//div[contains(@class, 'react-datepicker__day') and text()='{day}']")
      self.wait_element_to_be_clickable(select_day).click()

   #Метод выбора срока аренды
   @allure.step("Выбираем срок аренды")
   def choose_rental_time(self, data):
      self.element(BasePageLocators.RENTAL_TIME_FIELD).click()
      rental_days = data['rental_time']
      self.wait_element_to_be_clickable((By.XPATH, f"//div[text()='{rental_days}']")).click()

   #Метод выбора цвета самоката
   @allure.step("Выбираем цвета самоката")
   def choose_color(self, data):
      self.element(BasePageLocators.CHOOSE_COLOR_SCOOTER).click()
      color_button = data['color']
      self.wait_element_to_be_clickable((By.ID, color_button)).click()

   #Метод для перехода к подтверждению заказа
   @allure.step("Переходим к подтверждению заказа")
   def go_to_confirm(self):
      self.element(BasePageLocators.ORDER_BUTTON).click()

   #Объединение методов для заполнения формы Про аренду в шаг
   @allure.step("Объединям методы для заполнения формы Про аренду в шаг")
   def filling_about_renting(self, data):
      self.choose_day(data)
      self.choose_rental_time(data)
      self.choose_color(data)
      self.go_to_confirm()

   #Метод подтверждения заказа
   @allure.step("Подтверждаем заказ")
   def confirm_order(self):
      self.wait_element_visibility(BasePageLocators.CONFIRM_WINDOW)
      self.element(BasePageLocators.YES_BUTTON).click()

   #Метод появления окна с успешным заказом
   @allure.step("Появление окна с успешным заказом")
   def show_success_order(self):
      self.wait_element_visibility(BasePageLocators.ORDER_PLACED_WINDOW)

   #Метод перехода по кнопке Посмотреть статус
   @allure.step("Нажимаем на кнопку Посмотреть статус")
   def show_status(self):
      self.wait_element_to_be_clickable(BasePageLocators.STATUS_BUTTON)
      self.element(BasePageLocators.STATUS_BUTTON).click()

   #Метод проверки отображения элемента на странице 
   @allure.step("Проверяем, отображается ли элемент на странице")
   def is_element_displayed(self, loc_path):
      return self.element(loc_path).is_displayed()

   #Метод открытия страницы 
   @allure.step("Открываем url")
   def open(self, url):
      self.driver.get(url)

   #Метод удаления всех куки 
   @allure.step("Удаляем cookies")
   def delete_cookies(self):
      self.driver.delete_all_cookies()

   #Метод проверки текущей открытой страницы 
   @allure.step("Проверяем текущий url страницы")
   def get_current_url(self):
      return self.driver.current_url

   #Метод перехода к новому окну 
   @allure.step("Переходим на новое открывшееся окно")
   def switch_to_new_window(self, windows_before, timeout=10):
      WebDriverWait(self.driver, timeout).until(
      expected_conditions.new_window_is_opened(windows_before)
    )
      self.driver.switch_to.window(self.driver.window_handles[-1])

   #Метод получения открытых окон
   @allure.step("Получаем список открытых окон")
   def get_window_handles(self):
      return self.driver.window_handles

   #Метод прокрутки к элементу 
   @allure.step("Прокручиваем траницу до элемента")
   def scroll_to_element(self, element):
      self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

   #Метод нажатия на элемент через JS 
   @allure.step("Нажимаем на элемент через JavaScript")
   def click_js(self, element):
      self.driver.execute_script("arguments[0].click();", element)

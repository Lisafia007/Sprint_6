from selenium.webdriver.common.by import By

class OrderButtonLocators():
   
   #Кнопка "Заказать" вверху страницы
   TOP_ORDER_BUTTON = (By.CLASS_NAME, "Button_Button__ra12g")

   #Кнопка "Заказать" внизу страницы
   BOTTOM_ORDER_BUTTON = (By.CLASS_NAME, "Button_Middle__1CSJM")
from selenium.webdriver.common.by import By

class BasePageLocators():

   #Кнопка для принятия куки "Да все привыкли"
   COOKIE_CLOSE_BUTTON = (By.ID, 'rcc-confirm-button')

   #Поле с куками
   COOKIE_FIELD = (By.CLASS_NAME, 'App_CookieConsent__1yUIN')

   #Заголовок формы данных "Для кого самокат"
   HEADER_DATA_FORM = (By.CLASS_NAME, "Order_Header__BZXOb")

   #Поле Имя
   NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")

   #Поле Фамилия
   SURNAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")

   #Поле Адрес
   ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")

   #Список Станция метро
   METRO_FIELD = (By.CLASS_NAME, "select-search__input")

   #Поле Телефон
   PHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")

   #Кнопка Далее на странице "Для кого самокат"
   NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

   #Заголовок формы данных "Про аренду"
   HEADER_ABOUT_RENTING = (By.XPATH, "//div[contains(text(), 'Про аренду')]")

   #Поле Когда привести самокат
   DATA_DAY_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")

   #Поле Срок аренды
   RENTAL_TIME_FIELD = (By.CSS_SELECTOR, ".Dropdown-placeholder")

   #Поле Цвет самоката
   CHOOSE_COLOR_SCOOTER = (By.CLASS_NAME, "Checkbox_Input__14A2w")
   
   #Кнопка Заказать на странице про аренду
   ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Middle__1CSJM') and text()='Заказать']") 

   #Окно подтверждения заказа "Хотите оформить заказ?"
   CONFIRM_WINDOW = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")

   #Кнопка подтверждения заказа "Да"
   YES_BUTTON = (By.XPATH, "//button[text()='Да']")

   #Окно об успешном подверждении заказа
   ORDER_PLACED_WINDOW = (By.XPATH, "//div[text()='Заказ оформлен']")

   #Кнопка Посмотреть статус
   STATUS_BUTTON = (By.XPATH, "//button[text()='Посмотреть статус']")


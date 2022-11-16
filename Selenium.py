from selenium import webdriver #Підключаємо бібліотеку Selenium
driver = webdriver.Chrome() #Обираємо браузер який буде відкриватись
driver.get("http://rozetka.com.ua/") #Посилання, котре відкриється
driver.quit() 
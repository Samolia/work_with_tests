import time
from selenium import webdriver


def login_to_yandex(login: str, password: str):
    driver = webdriver.Chrome(executable_path='../chromedriver.exe')
    url = 'https://passport.yandex.ru/auth/'
    driver.get(url)
    login_window = driver.find_elements_by_class_name('Textinput-Control')[0]
    login_window.send_keys(login)
    login_button = driver.find_elements_by_class_name(
        'Button2.Button2_size_l.Button2_view_action.Button2_width_max.Button2_type_submit')[0]
    login_button.click()
    time.sleep(1)
    password_window = driver.find_elements_by_class_name('Textinput-Control')[0]
    password_window.send_keys(password)
    password_button = driver.find_elements_by_class_name(
        'Button2.Button2_size_l.Button2_view_action.Button2_width_max.Button2_type_submit')[0]
    password_button.click()
    time.sleep(5)


if __name__ == '__main__':
    login = 'your_login'
    password = 'your_password'
    login_to_yandex(login, password)

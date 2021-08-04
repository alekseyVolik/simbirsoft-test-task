import allure
from settings import DRIVER_PATH
from selenium import webdriver
from page import LoginPage, PasswordPage, MainPage, NewMessagePage


class TestYandexMailPage:

    starting_page = "https://passport.yandex.ru/auth?from=mail&origin=hostroot_homer" + \
                    "_auth_ru&retpath=https%3A%2F%2Fmail.yandex.ru%2F&backpath=https" + \
                    "%3A%2F%2Fmail.yandex.ru%3Fnoretpath%3D1"

    @allure.step("Step 1: Open browser and get starting page")
    def _starting_browser(self):
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities={
                'browserName': 'chrome',
                'javascriptEnabled': True
            }
        )
        self.driver.implicitly_wait(30)
        self.driver.get(TestYandexMailPage.starting_page)

    @allure.step("Step 2: Set login ['{login}'] in login field")
    def _set_login(self, login):
        ya_login_page = LoginPage(self.driver)
        ya_login_page.set_login(login)
        ya_login_page.accept_login()

    @allure.step("Step 3: Set password ['{password}'] in password field")
    def _set_password(self, password):
        ya_password_page = PasswordPage(self.driver)
        ya_password_page.set_password(password)
        ya_password_page.accept_password()

    @allure.step("Step 4: Count message with topic ['{topic}'] in messages")
    def _count_and_create(self, topic):
        ya_main_page = MainPage(self.driver)
        msg_with_topic = ya_main_page.messages_with_topic(topic)
        ya_main_page.create_new_message()
        return msg_with_topic

    @allure.step("Step 5: Create message and send it to recipient ['{recipient}']")
    def _write_and_send(self, recipient, topic, content):
        ya_new_message = NewMessagePage(self.driver)
        ya_new_message.set_recipient(recipient)
        ya_new_message.set_topic(topic)
        ya_new_message.set_content(content)
        ya_new_message.send_message()

    def _close_browser(self):
        self.driver.close()

    @allure.title("Authorization, find messages with topic, send message")
    def test_case_1(self):
        try:
            login = 'simbirsoft-test-cases'
            password = '-$BnLDipiJ4_,6D'
            target_topic = 'Simbirsoft Тестовое задание'
            recipient = 'volikjob@gmail.com'
            topic = 'Greeting message'
            content = 'Сообщений с заголовком {topic}: {number}'
            self._starting_browser()
            self._set_login(login)
            self._set_password(password)
            num = self._count_and_create(target_topic)
            message = content.format(topic=topic, number=num)
            self._write_and_send(recipient, topic, message)
        finally:
            self._close_browser()

    @allure.title("Authorization, find messages with topic, send message")
    def test_case_2(self):
        try:
            login = 'simbirsoft-test-cases'
            password = '-$BnLDipiJ4_,6D'
            target_topic = 'Simbirsoft Тестовое задание'
            recipient = 'simbirsoft-test-cases@yandex.ru'
            topic = 'Greeting message'
            content = 'Сообщений с заголовком [{topic}]: {number}'
            self._starting_browser()
            self._set_login(login)
            self._set_password(password)
            num = self._count_and_create(target_topic)
            message = content.format(topic=topic, number=num)
            self._write_and_send(recipient, topic, message)
        finally:
            self._close_browser()

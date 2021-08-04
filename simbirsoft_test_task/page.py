from settings import ElementLocator
from page_elements import SingleElement
from page_elements import MultiElement
from selenium.webdriver.common.keys import Keys


class CommonPage:

    def __init__(self, driver):
        self.driver = driver


class YandexMailPage(CommonPage):
    pass


class LoginPage(YandexMailPage):

    login = SingleElement(*ElementLocator.YA_LOGIN_FIELD)

    def set_login(self, login):
        self.login.send_keys(login)

    def accept_login(self):
        self.login.send_keys(Keys.ENTER)


class PasswordPage(YandexMailPage):

    password = SingleElement(*ElementLocator.YA_PASWD_FIELD)

    def set_password(self, password):
        self.password.send_keys(password)

    def accept_password(self):
        self.password.send_keys(Keys.ENTER)


class MainPage(YandexMailPage):

    message_topics = MultiElement(*ElementLocator.YA_MSG_TOPICS)
    new_msg_btn = SingleElement(*ElementLocator.YA_BUTTON_NEW_MSG)

    def create_new_message(self):
        self.new_msg_btn.click()

    def messages_with_topic(self, topic=''):
        n = 0
        for message_topic in self.message_topics:
            if message_topic.text == topic:
                n += 1
        return n


class NewMessagePage(YandexMailPage):

    recipient = SingleElement(*ElementLocator.YA_NEW_MSG_TO)
    topic = SingleElement(*ElementLocator.YA_NEW_MSG_TOPIC)
    content = SingleElement(*ElementLocator.YA_NEW_MSG_CONTENT)
    send_button = SingleElement(*ElementLocator.YA_BUTTON_SEND_MSG)

    def set_recipient(self, recipient):
        self.recipient.send_keys(recipient)

    def set_topic(self, topic):
        self.topic.send_keys(topic)

    def set_content(self, content):
        self.content.send_keys(content)

    def send_message(self):
        self.send_button.click()

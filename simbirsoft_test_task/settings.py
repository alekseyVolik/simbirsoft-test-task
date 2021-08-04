from selenium.webdriver.common.by import By


DRIVER_PATH = {
    'Chrome': r'drivers/chrome/chromedriver.exe',
}


class ElementLocator:

    YA_LOGIN_FIELD = (
        By.ID,
        "passp-field-login"
    )

    YA_PASWD_FIELD = (
        By.ID,
        "passp-field-passwd"
    )

    YA_MSG_TOPICS = (
        By.XPATH,
        "//span[@class='mail-MessageSnippet-Item mail-MessageSnippet-Item_subject']/span"
    )

    YA_BUTTON_NEW_MSG = (
        By.XPATH,
        "//a[@class='mail-ComposeButton js-main-action-compose']"
    )

    YA_NEW_MSG_TO = (
        By.XPATH,
        "//div[@class='MultipleAddressesDesktop-Field ComposeYabblesField']/div"
    )

    YA_NEW_MSG_TOPIC = (
        By.XPATH,
        "//input[@class='composeTextField ComposeSubject-TextField']"
    )

    YA_NEW_MSG_CONTENT = (
        By.XPATH,
        "//div[@placeholder='Напишите что-нибудь']"
    )

    YA_BUTTON_SEND_MSG = (
        By.XPATH,
        "//div[@class='ComposeControlPanelButton ComposeControlPanel-Button " +
        "ComposeControlPanel-SendButton ComposeSendButton ComposeSendButton_desktop']/button"
    )

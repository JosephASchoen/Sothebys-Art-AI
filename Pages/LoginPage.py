import Util


class LoginPage(object):
    def __init__(self, driver, config_data) -> None:
        self.driver = driver
        self.config_data = config_data

    def go_to_home_page(self) -> None:
        Util.click_item(
            driver=self.driver,
            wait_time=self.config_data['WAIT_TIME_SMALL'],
            x_path=self.config_data['LOGIN_X_PATHS']['LOG_IN_FINISH_BUTTON']
        )

    def login(self) -> None:
        """login to authenticate"""
        username_password = open('Config/password_id', mode='r')
        username = username_password.readline().strip()
        password = username_password.readline().strip()

        Util.send_data(
            driver=self.driver,
            wait_time=self.config_data['WAIT_TIME_SMALL'],
            x_path=self.config_data['LOGIN_X_PATHS']['USERNAME_TEXT_BOX'],
            data=username
        )

        Util.send_data(
            driver=self.driver,
            wait_time=self.config_data['WAIT_TIME_SMALL'],
            x_path=self.config_data['LOGIN_X_PATHS']['PASSWORD_TEXT_BOX'],
            data=password
        )

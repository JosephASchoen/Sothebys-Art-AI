import Util


class HomePage(object):
    def __init__(self, driver, config_data) -> None:
        self.driver = driver
        self.config_data = config_data

    def get_page(self) -> None:
        self.driver.get(self.config_data['LINKS']['START_LINK'])

        Util.click_item(
            driver=self.driver,
            wait_time=self.config_data['WAIT_TIME_SMALL'],
            x_path='//*[@id="onetrust-close-btn-container"]/button'
        )

    def go_to_login_page(self) -> None:
        Util.click_item(
            driver=self.driver,
            wait_time=self.config_data['WAIT_TIME_SMALL'],
            x_path=self.config_data['LOGIN_X_PATHS']['LOG_IN_START_BUTTON']
        )

    def go_to_results_page(self) -> None:
        """get to the result page of the Sothebys website"""

        Util.perform_action_chain(
            driver=self.driver,
            wait_time=self.config_data['WAIT_TIME_SMALL'],
            x_path=self.config_data['GO_TO_RESULTS_X_PATHS']['X_PATH_LINK_1']
        )

        Util.perform_action_chain(
            driver=self.driver,
            wait_time=self.config_data['WAIT_TIME_SMALL'],
            x_path=self.config_data['GO_TO_RESULTS_X_PATHS']['X_PATH_LINK_2']
        )

        Util.click_item(
            driver=self.driver,
            wait_time=self.config_data['WAIT_TIME_SMALL'],
            x_path=self.config_data['GO_TO_RESULTS_X_PATHS']['X_PATH_LINK_3']
        )

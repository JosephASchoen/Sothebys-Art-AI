from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from bs4 import BeautifulSoup
import json
from Pages import HomePage, LoginPage, ResultsPage
from typing import List
from Entities import Collection
from functools import reduce


"""
# apt update
# apt upgrade


# wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

# dpkg -i google-chrome-stable_current_amd64.deb

# google-chrome --version
Google Chrome 117.0.5938.132

# pip3 install selenium
# pip3 install webdriver-manager
"""

with open('Config/config.json') as file:
    config_data = json.load(file)


# todo make summary pages show lots
# todo scrape images
# todo comment code
# todo get category of art
# todo make work on aws ec2

def set_up_chromedriver():
    #service = Service(executable_path='chromedriver.exe')
    service = Service(ChromeDriverManager().install())
    options = Options()
    #options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("start-maximized")

    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    driver = webdriver.Chrome(service=service, options=options)
    return driver


def make_selenium_work(driver):
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
        Object.defineProperty(navigator, 'webdriver', {
          get: () => undefined
        })
      """
    })

    driver.execute_cdp_cmd("Network.enable", {})
    driver.execute_cdp_cmd('Network.setUserAgentOverride', {
        "userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})


def get_results(_results_page: ResultsPage, _url: str, start_page: int, end_page: int) -> List[Collection]:
    results = list(
        map(
            lambda n:
            _results_page.get_page_results(_url+'&p='+str(n)),
            range(start_page, end_page+1)
        )
    )
    results = list(reduce(lambda i, j: i + j, results, []))
    return results


def main(start_page=1, number_of_pages=1) -> List[Collection]:
    driver = set_up_chromedriver()
    make_selenium_work(driver=driver)

    home_page = HomePage.HomePage(driver=driver, config_data=config_data)
    home_page.get_page()
    home_page.go_to_login_page()

    login_page = LoginPage.LoginPage(driver=driver, config_data=config_data)
    login_page.login()
    login_page.go_to_home_page()

    home_page.go_to_results_page()
    results_page = ResultsPage.ResultsPage(driver=driver, config_data=config_data)

    html = driver.page_source
    soup = BeautifulSoup(html, parser='html.parser', features="lxml")
    max_number_of_pages = int(soup.find("li", class_="SearchModule-pageCounts").find_all('span')[1].text)
    print(max_number_of_pages)

    results_link = config_data['LINKS']['RESULTS_LINK']
    end_page = start_page + number_of_pages
    results = get_results(results_page, results_link, start_page, min(end_page, max_number_of_pages))
    return results


if __name__ == '__main__':
    main()

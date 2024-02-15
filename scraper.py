from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import json
from Pages import HomePage, LoginPage, ResultsPage


with open('Config/config.json') as file:
    config_data = json.load(file)

# todo make summary pages show lots
# todo scrape images
# todo comment code
# todo get category of art


def set_up_chromedriver():
    service = Service(executable_path='Config/chromedriver.exe')
    options = webdriver.ChromeOptions()
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


def get_results(_results_page: ResultsPage, _url: str, start_page: int, end_page: int):
    results = list(map(lambda n: _results_page.get_page_results(_url+'&p='+str(n)), range(start_page, end_page+1)))
    return results


def main(start_page=1, number_of_pages=1):
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
    get_results(results_page, results_link, start_page, min(end_page, max_number_of_pages))


if __name__ == '__main__':
    main()